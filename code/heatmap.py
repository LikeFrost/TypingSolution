import pdfplumber
import pinyin
from pyecharts import options as opts
from pyecharts.charts import HeatMap
from pyecharts.commons.utils import JsCode

#计算每个单词出现的次数
def countLetters():
    with pdfplumber.open("txt.pdf") as pdf:
        code=str()
        for page in pdf.pages:
            code=code+pinyin.get(page.extract_text(), format='strip')
    b = {}
    list="abcdefghijklmnopqrstuvwxyz"
    for i in list:
        b[i]=code.count(i)
    return(b,code)

#画热力图
def heatMap():
    [b,code] = countLetters()
    x_axis=["0","1","2","3","4","5","6","7","8","9"]
    y_axis=["0","1","2"]
    value=[[0,2,b['q']],[1,2,b['w']],[2,2,b['e']],[3,2,b['r']],[4,2,b['t']],[5,2,b['y']],[6,2,b['u']],[7,2,b['i']],[8,2,b['o']],[9,2,b['p']],
           [0,1,b['a']],[1,1,b['s']],[2,1,b['d']],[3,1,b['f']],[4,1,b['g']],[5,1,b['h']],[6,1,b['j']],[7,1,b['k']],[8,1,b['l']],[9,1,0],
           [0,0,0],[1,0,b['z']],[2,0,b['x']],[3,0,b['c']],[4,0,b['v']],[5,0,b['b']],[6,0,b['n']],[7,0,b['m']],[8,0,0],[9,0,0]]

    c = (
        HeatMap(init_opts= opts.InitOpts(height="400px", width="1200px"))
        .add_xaxis(x_axis)
        .add_yaxis(
            "字母出现次数",
            y_axis,
            value,
            label_opts=opts.LabelOpts(is_show=True, position="inside", formatter=JsCode(
                "function (params) {name='qwertyuiopasdfghjkl00zxcvbnm0';return name[params.data[0]+(2-params.data[1])*10];}"
            ),font_size=20,font_weight='bold'),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="《共产党宣言》中全拼字母热力图"),
            visualmap_opts=opts.VisualMapOpts(max_=7463,min_=0,range_color=["#F0FFF0", "#006000"]),
            tooltip_opts=opts.TooltipOpts(formatter=JsCode(
                "function (params) {name='qwertyuiopasdfghjkl00zxcvbnm0';return name[params.data[0]+(2-params.data[1])*10]+' : '+params.data[2];}"
            ),),
            legend_opts=opts.LegendOpts(is_show=False)
        )
        .render("初始按键热力图.html")
    )
heatMap()
