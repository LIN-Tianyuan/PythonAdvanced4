# Graphique linéaire
from pyecharts.charts import Line

# Obtenir un objet graphique linéaire
line = Line()
# Ajouter les données de l'axe des x
line.add_xaxis(["France", "America", "China"])
# Ajouter les données de l'axe des y
line.add_yaxis("GDP", [30, 20, 10])
# Générer des graphiques
line.render()
