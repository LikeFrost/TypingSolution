from pyecharts import options as opts
from pyecharts.charts import HeatMap
from pyecharts.commons.utils import JsCode

#画标准打字键位图
def useMap():
    x_axis=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]
    y_axis=["0","1","2"]
    value=[[0,2,4],[1,2,4],[2,2,3],[3,2,3],[4,2,2],[5,2,2],[6,2,1],[7,2,1],[8,2,1],[9,2,1],[10,2,2],[11,2,2],[12,2,2],[13,2,2],[14,2,3],[15,2,3],[16,2,4],[17,2,4],[18,2,5],[19,2,5],
           [0,1,0],[1,1,4],[2,1,4],[3,1,3],[4,1,3],[5,1,2],[6,1,2],[7,1,1],[8,1,1],[9,1,1],[10,1,1],[11,1,2],[12,1,2],[13,1,2],[14,1,2],[15,1,3],[16,1,3],[17,1,4],[18,1,4],[19,1,0],
           [0,0,0],[1,0,0],[2,0,4],[3,0,4],[4,0,3],[5,0,3],[6,0,2],[7,0,2],[8,0,1],[9,0,1],[10,0,1],[11,0,1],[12,0,2],[13,0,2],[14,0,2],[15,0,2],[16,0,0],[17,0,0],[18,0,0],[19,0,0]]

    c = (
        HeatMap(init_opts= opts.InitOpts(height="400px", width="1200px"))
        .add_xaxis(x_axis)
        .add_yaxis(
            "使用键位图",
            y_axis,
            value,
            label_opts=opts.LabelOpts(is_show=True, position="inside", formatter=JsCode(
                "function (params) {name='QQWWEERRTTYYUUIIOOPP0AASSDDFFGGHHJJKKLL000ZZXXCCVVBBNNMM00';return name[params.data[0]+(2-params.data[1])*20];}"
            ),font_size=20,font_weight='bold'),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="标准打字键位图"),
            visualmap_opts=opts.VisualMapOpts(max_=5,min_=0,range_color=["#F0FFF0", "#006000"],is_show=False),
            tooltip_opts=opts.TooltipOpts(formatter=JsCode(
                "function (params) {name='QQWWEERRTTYYUUIIOOPP0AASSDDFFGGHHJJKKLL000ZZXXCCVVBBNNMM00';return name[params.data[0]+(2-params.data[1])*10]+' : '+params.data[2];}"
            ),),
            legend_opts=opts.LegendOpts(is_show=False),

        )
        .render("标准打字键位图.html")
    )
useMap()