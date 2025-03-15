# Import libraries
from pyecharts.charts import Map, Page
from pyecharts.globals import ThemeType


import pandas as pd
from pyecharts.options import InitOpts, VisualMapOpts, LegendOpts, LabelOpts, TitleOpts, TextStyleOpts

# import data
dataset = pd.read_csv('owid-covid-data.csv')
# print(dataset.head())
# print(dataset.columns)
# Changer la date du type de données objet en type de données datetime
dataset['date'] = pd.to_datetime(dataset['date'])
# Trier les données par date
df = dataset.sort_values(by=['date'], ascending=False)
map_df = df[df['date']=='2022-08-01']
map_df.reset_index(drop=True, inplace=True)

country = list(map_df['location'])
total_cases = list(map_df['total_cases'])
# print(f"country -> {country}")
# print(f"total_cases -> {total_cases}")

# Générer la carte
# Préparer les données
list_data = []
for i in range(len(country)):
    list1 = []
    list1.append(country[i])
    list1.append(total_cases[i])
    list_data.append(list1)
# print(list_data)

map_1 = Map(init_opts=InitOpts(width="1000px", height="600px", theme=ThemeType.ROMANTIC))
# Supprimer les points de la carte
map_1.add('Total Confirmed Cases', list_data, maptype='world', is_map_symbol_show=False)
# Aucune étiquette affiché (nom du pays)
map_1.set_series_opts(label_opts=LabelOpts(is_show=False))
map_1.set_global_opts(
    visualmap_opts=VisualMapOpts(max_=1100000, is_piecewise=True,
                                 pieces=[
                                     {"min": 500000},
                                     {"min": 200000, "max": 499999},
                                     {"min": 100000, "max": 199999},
                                     {"min": 50000, "max": 99999},
                                     {"min": 10000, "max": 49999},
                                     {"max": 9999}
                                 ]),
    # Ajouter un titre et un sous-titre à la carte
    title_opts=TitleOpts(
        title='Covid-19 Worldwide Total Cases',
        subtitle='Till August 1st, 2022',
        pos_left='center',
        padding=0,
        item_gap=2, # gap between title and subtitle
        title_textstyle_opts=TextStyleOpts(color='darkblue',
                                           font_weight='bold',
                                           font_family='Courier New',
                                           font_size=30),
        subtitle_textstyle_opts=TextStyleOpts(color='grey',
                                           font_weight='bold',
                                           font_family='Courier New',
                                           font_size=13),
    ),
    legend_opts=LegendOpts(is_show=False)
)

# map_1.render()
page = Page(layout=Page.SimplePageLayout)
page.add(map_1)
page.render()



