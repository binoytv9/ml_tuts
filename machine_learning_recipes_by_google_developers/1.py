from sklearn import tree

#smooth=1
#bumpy=0
#apple=0
#orange=1

features = [[140, 1], [130, 1], [150, 0], [170, 0] ]
labels = [ 0, 0, 1, 1 ]

clf = tree.DecisionTreeClassifier()
clf = clf.fit( features, labels )

print clf.predict( [[150, 0]] )

