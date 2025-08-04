import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
# print(load_iris())
classifier = DecisionTreeClassifier()
iris = load_iris() 
classifier.fit(iris.data, iris.target)
plt.figure(figsize = (15,10) )
tree.plot_tree(classifier,filled = True)
plt.show()

