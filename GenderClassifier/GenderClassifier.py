from sklearn import tree
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#classifiers
treeClf = tree.DecisionTreeClassifier()
svmClf = SVC()
gaussClf = GaussianProcessClassifier()
nlpClf = MLPClassifier()
naiveClf = GaussianNB()


#height,weight,shoe-size
#training data
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

#training of classifiers on our data
treeClf = treeClf.fit(X,Y)
nlpClf = nlpClf.fit(X,Y)
gaussClf = gaussClf.fit(X,Y)
svmClf = svmClf.fit(X,Y)
naiveClf = naiveClf.fit(X,Y)

#testing data
_X =[[184,84,44],[198,92,48],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
_Y =['male','male','male','female','female','female','male','male']


#prediction
prediction1 = treeClf.predict(_X)
prediction2 = nlpClf.predict(_X)
prediction3 = gaussClf.predict(_X)
prediction4 = svmClf.predict(_X)
prediction5 = naiveClf.predict(_X)

#accuracy
accuracy1 = accuracy_score(_Y,prediction1)
accuracy2 = accuracy_score(_Y,prediction2)
accuracy3 = accuracy_score(_Y,prediction3)
accuracy4 = accuracy_score(_Y,prediction4)
accuracy5 = accuracy_score(_Y,prediction5)


#compare their results and print the best one!
print(prediction1)
print(prediction2)
print(prediction3)
print(prediction4)
print(prediction5)

print(accuracy1)
print(accuracy2)
print(accuracy3)
print(accuracy4)
print(accuracy5)

