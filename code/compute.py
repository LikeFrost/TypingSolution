import math
import re
import pdfplumber
import pinyin
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import heatmap
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts import options as opts
import numpy as np

#计算每个字母出现的次数、频率
def letterRate():
    [times,c]=heatmap.countLetters()
    letter="abcdefghijklmnopqrstuvwxyz"
    total=0
    rate={}
    total_hx=0
    for i in letter:
        total=total+times[i]
    for i in letter:
        rate[i]=times[i]/total
    return(times,rate)

#画次数直方图
def letterRate_pic():
    [times,rate]=letterRate()
    y_axis1=[]
    for i in times.values():
        y_axis1.append(i)
    print("旧编码方案字母使用平均值", np.mean(y_axis1))
    print("旧编码方案字母使用标准差", np.std(y_axis1))
    x_axis=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    c = (
        Bar({"theme": ThemeType.MACARONS})
        .add_xaxis(x_axis)
        .add_yaxis(
            "字母出现次数",y_axis1
        )
        .set_global_opts(
        title_opts={"text": "字母出现次数直方图"}
        )
        .set_series_opts(
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="average",name="平均值")
                ]
            )
        )
        .render("字母出现次数直方图.html")
    )
letterRate_pic()

#计算编码中1的比例
def numRate():
    [times,rate]=letterRate()
    total=0
    for i in range(97,122):
        c = bin(i).count('1')
        total=total+c*rate[chr(i)]
    print(total/8)
#numRate()

#将字母按手指分类
def letterSort():
    disl1={'qa':1.118,'aq':1.118,'az':1.118,'za':1.118,'qz':1.236,'zq':2.236}
    disl2= {'ws': 1.118, 'sw': 1.118, 'sx': 1.118, 'xs': 1.118, 'wx': 1.236, 'xw': 2.236, }
    disl3= {'ed': 1.118, 'de': 1.118, 'dc': 1.118, 'cd': 1.118, 'ec': 1.236, 'ce': 2.236, }
    disl4= {'rf': 1.118, 'rv': 2.236, 'rt': 1, 'rg': 1.803, 'rb': 2.828, 'fr': 1.118, 'fv': 1.118, 'ft': 1.118, 'fg': 1,'fb': 1.803,
         'vr': 2.236, 'vf': 1.118, 'vt': 2, 'vg': 1.118, 'vb': 1, 'tr': 1, 'tf': 1.118, 'tv': 2, 'tg': 1.118,'tb': 2.236,
         'gr': 1.803, 'gf': 1, 'gv': 1.118, 'gt': 1.118, 'gb': 1.118, 'br': 2.828, 'bf': 1.803, 'bv': 1, 'bt': 2.236,'bg': 1.118, }
    disr1= {'yh': 1.118, 'yn': 2.236, 'yu': 1, 'yj': 1.803, 'ym': 2.828, 'hy': 1.118, 'hn': 1.118, 'hu': 1.118, 'hj': 1,'hm': 1.803,
            'ny': 2.236, 'nh': 1.118, 'nu': 2, 'nj': 1.118, 'nm': 1, 'uy': 1, 'uh': 1.118, 'un': 2, 'uj': 1.118,'um': 2.236,
            'jy': 1.803, 'jh': 1, 'jn': 1.118, 'ju': 1.118, 'jm': 1.118, 'my': 2.828, 'mh': 1.803, 'mn': 1,'mu': 2.236, 'mj': 1.118, }
    disr2= {'ik': 1.118, 'ki': 1.118}
    disr3= {'lo':1.118,'ol':1.118}
    [b,code]=heatmap.countLetters()
    left1 = ''.join(re.findall("[qaz]",code))
    left2 = ''.join(re.findall("[wsx]", code))
    left3 = ''.join(re.findall("[edc]", code))
    left4 = ''.join(re.findall("[rfvtgb]", code))
    right1 = ''.join(re.findall("[yhnujm]", code))
    right2 = ''.join(re.findall("[ik]", code))
    right3 = ''.join(re.findall("[ol]", code))
    totDis=[]
    temp=0
    for k,v in disl1.items():
        temp=temp+left1.count(k)*v
    totDis.append(temp)

    temp = 0
    for k, v in disl2.items():
        temp = temp + left2.count(k) * v
    totDis.append(temp)

    temp = 0
    for k, v in disl3.items():
        temp = temp + left3.count(k) * v
    totDis.append(temp)

    temp = 0
    for k, v in disl4.items():
        temp = temp + left4.count(k) * v
    totDis.append(temp)

    temp = 0
    for k, v in disr1.items():
        temp = temp + right1.count(k) * v
    totDis.append(temp)

    temp = 0
    for k, v in disr2.items():
        temp = temp + right2.count(k) * v
    totDis.append(temp)

    temp = 0
    for k, v in disr3.items():
        temp = temp + right3.count(k) * v
    totDis.append(temp)
    return(totDis)
#letterSort()

#画出按手指分类的直方图
def fingerDis_pic():
    totDis=letterSort()
    totDis.append(0)
    [times, rate] = letterRate()
    y_axis=[]
    y_axis.append(times['q']+times['a']+times['z'])
    y_axis.append(times['w'] + times['s'] + times['x'])
    y_axis.append(times['e'] + times['d'] + times['c'])
    y_axis.append(times['r'] + times['f'] + times['v']+times['t'] + times['g'] + times['b'])
    y_axis.append(times['y'] + times['h'] + times['n'] + times['u'] + times['j'] + times['m'])
    y_axis.append(times['i'] + times['k'] )
    y_axis.append(times['o'] + times['l'] )
    y_axis.append(times['p'] )
    x_axis=["左手小指","左手无名指","左手中指","左手食指","右手食指","右手中指","右手无名指","右手小指"]
    c = (
        Bar({"theme": ThemeType.MACARONS})
        .add_xaxis(x_axis)
        .add_yaxis(
            "手指移动距离",totDis
        )
        .add_yaxis(
            "手指敲击次数",y_axis
        )
        .set_global_opts(
        title_opts={"text": "手指移动距离直方图"}
        )
        .set_series_opts(
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="average",name="平均值")
                ]
            )
        )
        .render("手指移动距离直方图.html")
    )
fingerDis_pic()

def getH_x():
    with pdfplumber.open("txt.pdf") as pdf:
        code=str()
        for page in pdf.pages:
            code=code+pinyin.get(page.extract_text(), format='strip',delimiter=' ')
    code = re.sub("[\d+\.\!\/_,$%^*(+\"\-\']+|[+——！“”，。？；．、~@：#￥%……&*《》()（）]", "", code)
    code_list=list(set(code.split()))
    code = code.split()
    code_list.sort()
    code_num=[]
    totWord=0
    totLen=0
    for i in code_list:
        temp = code.count(i)
        totWord = totWord + temp
        code_num.append(temp)
        totLen = totLen + temp * len(i)
    print("平均码长为",totLen/totWord)
    headers=['拼音','个数','出现概率','信息熵']
    code_list=np.array(code_list)
    code_num = np.array(code_num)
    rows = dict(zip(code_list,code_num))
    row=[]
    tot_hx=0
    for k,v in rows.items():
        p=v/totWord
        hx=-p*math.log2(p)
        tot_hx=tot_hx+hx
        row.append([k,v,p,hx])
    print('总信息熵为',tot_hx)
    print('总词数为',totWord)
    print(rows)
    c=(
        Table()
        .add(headers,row)
        .set_global_opts(
            title_opts=ComponentTitleOpts(title="拼音使用表")
        )
    ).render("拼音使用表.html")

getH_x()