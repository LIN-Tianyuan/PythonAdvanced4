# 1.Ouverture du fichier, en mode a
f = open('python.txt', 'a')
# 2.Ecriture du fichier
f.write('hello world')
# 3.Rafraîchissement du contenu
f.flush()
f.close()