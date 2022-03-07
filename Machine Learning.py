# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 07:18:00 2022

@author: zyoas
"""

# Author: placeboXego
#    Date: 3/2/22
# Subject: Machine Learning Tutorial
#
#  Source: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

"""
This project is a good project because it is so well understood. 

 - Attributes are numeric so you have to figure out how to load and handle data
 - It is a classification problem, allow you to practice with perhaps an easier
   type of supervised learning algorithm. 
 - It is a muli-class classification problem (multi-nominal) that may require 
   some specialized handling
 - It only has 4 attributes and 150 rows, meaning it is small and easily fits
   into memory (and a screen)
 - All of the numeric attributes are in the same units and the same scale
   not requiring any special scaling or transforms to get started. 
   
   
HIGH LEVEL SUMMARY
- Install Python and SciPy platforms
- Load the data set
- Summarize the data set
- Visulaizing the data set
- Evaluating some algorithms
- Making some predictions

"""

#%% Install Python and SciPy Platforms
# Check the versions of libraries
 
# Python version
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

# Import Libaries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#%% Load, Inspect, and Stat Summary of Data

#-----------------------------------------------------------------------------
# Loading the Data (from the web)
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
# names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# dataset = read_csv(url, names=names)

# Loading the Data (from the locally)
url = "Z:\Secondary\Data Science\Python\Machine Learning Data Sets\iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
#-----------------------------------------------------------------------------



# Take a look at the data shape (size) and a peek of the data
print(dataset.shape)
print(dataset.head(20))

# Statistical Summary
print(dataset.describe())

# Class Distribution
print(dataset.groupby('class').size())



#%% Data Visualization

# Now that we have a general sense of the data, we can extend our understanding
# with graphical visualizations

# ============
# Box and Whisker Plot (gives an idea of distribution)

#data being ploted      Type          Subplots      Layout         Share common X          Share common Y
#dataset.plot(          kind='box', subplots=True, layout=(2,2),      sharex=False,       sharey=False)
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

# ===========
# Histogram Plot (gives an idea of the distribution )
dataset.hist()
pyplot.show()

# ===========
# Look at scatterplots of all pairs of attributes. This can be helpful to spot
# structured relationships between input variables
scatter_matrix(dataset)
pyplot.show()

#%% Evaulate some algorithms

# HIGH LEVEL OVERVIEW
#  - Separate out a validation dataset
#  - Set-up the test harness to use 10-fold cross validation
#  - Build multiple different models to predict species from flower measurements
#  - Select the best model

# We need to know the model we create is good

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

# https://machinelearningmastery.com/index-slice-reshape-numpy-arrays-machine-learning-python/ 


# Testing multiple algorithms
#  - Logistic Regression (LR)
#  - Linear Discriminant Analysis (LDA)
#  - K-Nearest Neighbors (KNN)
#  - Classificaiton and Regression Trees (CART)
#  - Gaussian Naive Bayes (NB)
#  - Support Vector Machines (SVM)

# This is a good mixture of simplier linear (LR, LDA), nonlinear (KNN, CART,
# NB, and SVM) algorithms

# Now lets build and evaluate our models

models = []
models.append(('LR',LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA',LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB',GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# Evaluate each model in turn
results=[]
names =[]
for name, model in models:
    kfold = StratifiedKFold(n_splits=10,random_state=1, shuffle=True)
    cv_results = cross_val_score(model,X_train,Y_train,cv=kfold,scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# A useful way to compare the samples of results of each algorithm is to 
# create a box and whisker plot for each distribution and compare the 
# distributions.

# Compare Algorithms
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

#%% Predictions

# We must now choose an algorithm to use to make our predictions
# The previous section suggests SVM is the most accurate model. Now we'd like
# to get the accuracy of the model with the validation set.

# *** It is valuable to keep a validation set just in case you made a slip
#     during training, such as an overfitting to the traing set or a data leak.

model = SVC(gamma = 'auto')
model.fit(X_train,Y_train)
predictions = model.predict(X_validation)


# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

