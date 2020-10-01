from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["A", "B", "C", "D"])
bar.add_yaxis("random Data", [1, 2, 3, 4])
bar.render("bar.html")