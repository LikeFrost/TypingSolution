import numpy as np
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts


class Node(object):
    def __init__(self,name=None,value=None):
        self._name=name
        self._value=value
        self._left=None
        self._right=None
        self._codevalue='0'

class HuffmanTree(object):
    def __init__(self,char_weights):
        self.codeway = {}
        self.huffList=[]
        self.a=[Node(part[0],part[1]) for part in char_weights]
        while len(self.a)!=1:
            self.a.sort(key=lambda node:node._value,reverse=True)
            c=Node(value=(self.a[-1]._value+self.a[-2]._value))
            c._left=self.a.pop(-1)
            c._right=self.a.pop(-1)
            self.a.append(c)
        self.root=self.a[0]

    def pre(self, tree, length,l):
        if l==0:
            self.b=[0]*length
        node = tree
        if (not node):
            return
        elif node._name:
            s=str()
            for i in range(l):
                s=s+str(self.b[i])
            self.huffList.append([node._name,l,s,node._value])
            return
        self.b[l] = 0
        self.pre(node._left, length,l + 1)
        self.b[l] = 1
        self.pre(node._right,length,l + 1)

    def pr(self):
        return (self.huffList)

if __name__=='__main__':
    a={('a', 1), ('ai', 6), ('an', 8), ('ao', 1), ('ba', 53), ('bai', 9), ('ban', 33), ('bang', 4), ('bao', 30), ('bei', 64), ('ben', 59), ('beng', 1), ('bi', 41), ('bian', 50), ('biao', 21), ('bie', 15), ('bing', 33), ('bo', 25), ('bu', 272), ('cai', 62), ('can', 3), ('cang', 2), ('cao', 3), ('ceng', 15), ('cha', 7), ('chan', 490), ('chang', 53), ('chao', 6), ('che', 5), ('chen', 3), ('cheng', 112), ('chi', 15), ('chong', 15), ('chou', 3), ('chu', 73), ('chuan', 9), ('chuang', 12), ('chui', 1), ('chun', 11), ('chuo', 1), ('ci', 48), ('cong', 35), ('cu', 6), ('cui', 9), ('cun', 43), ('cuo', 5), ('da', 67), ('dai', 90), ('dan', 60), ('dang', 83), ('dao', 103), ('de', 1392), ('deng', 38), ('di', 104), ('dian', 12), ('diao', 17), ('ding', 15), ('dong', 121), ('dou', 45), ('du', 97), ('duan', 37), ('dui', 109), ('dun', 4), ('duo', 33), ('e', 6), ('er', 106), ('fa', 135), ('fan', 71), ('fang', 63), ('fei', 27), ('fen', 51), ('feng', 32), ('fo', 4), ('fou', 1), ('fu', 50), ('gai', 30), ('gan', 11), ('gang', 4), ('gao', 9), ('ge', 213), ('gei', 9), ('gen', 6), ('geng', 15), ('gong', 271), ('gou', 13), ('gu', 35), ('guai', 2), ('guan', 106), ('guang', 5), ('gui', 23), ('guo', 195), ('ha', 2), ('hai', 5), ('han', 2), ('hang', 5), ('hao', 14), ('he', 228), ('hen', 9), ('heng', 6), ('hong', 1),('hou', 40), ('hu', 37), ('hua', 38), ('huai', 6), ('huan', 47), ('huang', 8), ('hui', 213), ('hun', 3), ('huo', 81), ('ji', 606), ('jia', 88), ('jian', 142), ('jiang', 15), ('jiao', 57), ('jie', 438), ('jin', 87), ('jing', 88), ('jiu', 118), ('ju', 52), ('juan', 3), ('jue', 22), ('jun', 15), ('kai', 25), ('kan', 26), ('kang', 6), ('kao', 4), ('ke', 50), ('ken', 2), ('kong', 13), ('kou', 8), ('ku', 3), ('kua', 2), ('kuai', 5), ('kuang', 9), ('kui', 1), ('kun', 3), ('kuo', 10), ('la', 5), ('lai', 125), ('lan', 4), ('lao', 46), ('le', 176), ('lei', 7), ('leng', 4), ('li', 267), ('lian', 26), ('liang', 29), ('liao', 8), ('lie', 12), ('ling', 27), ('liu', 8), ('long', 3), ('lou', 2), ('lu', 15), ('luan', 2), ('lun', 20), ('luo', 11), ('lv', 17), ('lve', 2), ('ma', 13), ('mai', 23), ('man', 13), ('mang', 3), ('mao', 11), ('mei', 48), ('men', 214), ('meng', 6), ('mi', 9), ('mian', 49), ('miao', 1), ('mie', 57), ('min', 64), ('ming', 73), ('mo', 7), ('mou', 7), ('mu', 19), ('na', 43), ('nan', 6), ('nang', 1), ('nei', 21), ('neng', 53), ('ni', 39), ('nian', 20), ('nie', 1), ('ning', 1), ('nong', 25), ('nu', 16), ('nuo', 1), ('nv', 8), ('ou', 7), ('pai', 17), ('pan', 10), ('pang', 2), ('pao', 4), ('pei', 7), ('peng', 2), ('pi', 17), ('pian', 5), ('pie', 2), ('pin', 25), ('ping', 12), ('po', 21), ('pu', 12), ('qi', 135), ('qia', 1), ('qian', 25), ('qiang', 12), ('qiao', 2), ('qie', 87), ('qin', 2), ('qing', 10), ('qiu', 18), ('qu', 79), ('quan', 47), ('que', 18), ('qun', 5), ('ran', 31), ('rang', 4), ('rao', 1), ('re', 2), ('ren', 231), ('ri', 14), ('rong', 9), ('ru', 22), ('rui', 2), ('ruo', 1), ('sa', 2), ('sai', 2), ('san', 7), ('se', 7), ('seng', 5), ('sha', 2), ('shan', 6), ('shang', 68), ('shao', 16), ('she', 164), ('shen', 51), ('sheng', 161), ('shi', 731), ('shou', 67), ('shu', 42), ('shuang', 1), ('shui', 10), ('shuo', 49), ('si', 44), ('su', 14), ('suan', 2), ('sui', 24), ('suo', 87), ('ta', 239), ('tai', 16), ('tan', 12), ('tang', 3), ('tao', 7), ('te', 16), ('ti', 51), ('tian', 10), ('tiao', 42), ('tie', 3), ('ting', 16), ('tong', 166), ('tou', 3), ('tu', 28), ('tuan', 3),( 'tui', 11), ('tun', 1), ('tuo', 4), ('wa', 7), ('wai', 10), ('wan', 22), ('wang', 17), ('wei', 152), ('wen', 50), ('weng', 1), ('wo', 38), ('wu', 151), ('xi', 95), ('xia', 38), ('xian', 121), ('xiang', 97), ('xiao', 113), ('xie', 68), ('xin', 49), ('xing', 121), ('xiong', 4), ('xiu', 3), ('xu', 40), ('xuan', 10), ('xue', 45), ('xun', 5), ('ya', 13), ('yan', 31), ('yang', 51), ('yao', 93), ('ye', 136), ('yi', 539), ('yin', 64), ('ying', 37), ('yong', 77), ('you', 232), ('yu', 120), ('yuan', 37), ('yue', 42), ('yun', 39), ('zai', 229), ('zan', 3), ('zao', 28), ('ze', 15), ('zen', 3), ('zeng', 18), ('zha', 6), ('zhai', 1), ('zhan', 79), ('zhang', 17), ('zhao', 47), ('zhe', 267), ('zhen', 22), ('zheng', 193), ('zhi', 352), ('zhong', 221), ('zhou', 14), ('zhu', 134), ('zhua', 1), ('zhuan', 14), ('zhuang', 18), ('zhun', 4), ('zhuo', 1), ('zi', 357), ('zong', 29), ('zou', 4), ('zu', 77), ('zui', 39), ('zun', 5), ('zuo', 54)}
    tree=HuffmanTree(a)
    length=len(a)
    tree.pre(tree.root,length,0)
    huffList=tree.pr()
    for i in huffList:
        s=str()
        letter=str()
        j=i[1]
        while j>=5:
            #print(i[2][j-4:j])
            letter=letter+chr(int(i[2][j-4:j],2)+97)
            s=s+str(int(i[2][j-4:j],2))
            s=s+' '
            j=j-4
        letter = letter + chr(int(i[2][0:j], 2)+97)
        s=s+str(int(i[2][0:j],2))
        s=s+' '
        #s = s[::-1]
        letter=letter[::-1]
        i.append(s)
        i.append(letter)
    print(huffList)
    headers=['拼音','哈夫曼编码位数','哈夫曼编码','次数','转化为BCD码（倒序）','转化为拼音（正序）']
    c = (
        Table()
            .add(headers, huffList)
            .set_global_opts(
            title_opts=ComponentTitleOpts(title="拼音的哈夫曼编码")
        )
    ).render("拼音哈夫曼编码.html")