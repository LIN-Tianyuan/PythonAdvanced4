import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts, InitOpts, AxisOpts, LegendOpts

# Traitement des données
with open("America.txt", 'r') as f:
    us_data = f.read()

# print(us_data)
# Suppression des démarreurs non JSON
us_data = us_data.replace("jsonp_1629344292311_69436(", "")

# Suppression des terminaisons non JSON
us_data = us_data[:-2]
# print(type(us_data))
# JSON vers dictionnaire Python
us_python_data = json.loads(us_data)
# print(us_python_data)
us_list_data = us_python_data['data']
dict_data = us_list_data[0]
trend_data = dict_data['trend']
# print(trend_data)
update_date = trend_data['updateDate']
list_data = trend_data['list']
# print(update_date.index("12.31"))
# Obtenir des données de date pour l'axe des x, prendre l'année 2022
x_data = update_date[:314]
dict_list = list_data[0]
# Obtenir des données de confirmation pour l'axe des y, prendre l'année 2022
y_data = dict_list['data'][:314]

# init_opts: Définir la largeur et la hauteur
line = Line(init_opts=InitOpts(width="1600px", height="800px"))
line.add_xaxis(x_data)
line.add_yaxis("2022 Covid", y_data)
line.set_global_opts(
    # Titre
    title_opts=TitleOpts(title="2022 Covid"),
    # X axis titre
    xaxis_opts=AxisOpts(name="Date"),
    # Y axis titre
    yaxis_opts=AxisOpts(name="Number of confirmed cases in the USA"),
    # Position
    legend_opts=LegendOpts(pos_left='70%')
)
line.render()
