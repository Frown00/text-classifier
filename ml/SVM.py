from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold
import nltk
import sklearn
import numpy as np
import sklearn.svm as svm

class SVM:
  def __init__(self, data, labels, minDf=10, maxFeatures=None, ngram=(1, 1)):
    self.data = data
    self.labels = labels
    if(maxFeatures):
      self.vectorizer = CountVectorizer(
        min_df=minDf, 
        tokenizer=nltk.word_tokenize, 
        stop_words="english", 
        max_features=maxFeatures,
        ngram_range=ngram
      )
    else:
      self.vectorizer = CountVectorizer(
        min_df=minDf, 
        tokenizer=nltk.word_tokenize, 
        stop_words="english",
        ngram_range=ngram
      )
    self.reviewTfmer = TfidfTransformer()
    self.categoryNames = ["Negative", "Neutral", "Positive"]
    
  
  def train(
    self, 
    k, 
    penalty='l2', 
    loss='squared_hinge', 
    dual=True, 
    tol=0.0001, 
    C=1.0, 
    multi_class='ovr', 
    fit_intercept=True, 
    intercept_scaling=1,
    class_weight=None,
    verbose=0,
    max_iter=100
  ):
    self.classifier = svm.LinearSVC(
      penalty=penalty, 
      loss=loss, 
      dual=dual, 
      tol=tol, 
      C=C, 
      multi_class=multi_class, 
      fit_intercept=fit_intercept, 
      intercept_scaling=intercept_scaling, 
      class_weight=class_weight, 
      verbose=verbose, 
      random_state=None, 
      max_iter=max_iter
    )
    self.doc_transformed = self.vectorizer.fit_transform(self.data)
    print(len(self.vectorizer.get_feature_names()))
    docs_tfidf = self.reviewTfmer.fit_transform(self.doc_transformed)
    X = docs_tfidf
    y = np.array(self.labels)
    kf = KFold(n_splits=k, shuffle=True)
    testingMetrics = []
    for train_index, test_index in kf.split(X):
      X_train, X_test = X[train_index], X[test_index]
      y_train, y_test = y[train_index], y[test_index]
      self.classifier.fit(X_train, y_train)
      y_pred = self.classifier.predict(X_test)
      metrics = sklearn.metrics.accuracy_score(y_test, y_pred)
      testingMetrics.append(metrics)
    print("Accuracy: ", np.average(testingMetrics))
    return
  
  def predict(self, newReviews):
    reviews = self.vectorizer.transform(newReviews)
    reviewsTfidf = self.reviewTfmer.transform(reviews)
    pred = self.classifier.predict(reviewsTfidf)
    for review, category in zip(newReviews, pred):
      print("%r => %s" % (review, self.categoryNames[int(category)]))
    return
  