from sklearn import tree
features = [[7, 0.6, 40], [7, 0.6, 41], [37, 600, 37], [37, 600, 38]]
#labels = [chicken, chicken, horse, horse]
labels = [0, 0, 1, 1]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)

print("El programa determina por medio del peso y altura si es un caballo o pollo")
print("Altura +37 pulgadas")
print("Temperatura entre 37-38")
print("Peso mas de 600kg")
print classif.predict([[38, 600, 37.5]])
print("horse")


print("Altura 7 pulgadas")
print("Temperatura entre 40-41")
print("Peso menos de 1kg")
print classif.predict([[7, 0.6, 41]])
print("chicken")
