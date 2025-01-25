# 1.Ouverture du fichier
f = open('python.txt', 'w')
# 2.Ecriture du fichier
f.write('hello world')
# 3.Rafraîchissement du contenu
f.flush()
f.close()