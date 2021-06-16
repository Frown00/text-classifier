from ml.SVM import SVM
from ml.Bayesian import Bayesian
from data.Reviews import Reviews;

Object = lambda **kwargs: type("Object", (), kwargs)

reviewsData = [
  Object(
    contents = './data/scaledata/Dennis+Schwartz/subj.Dennis+Schwartz', 
    ratings = './data/scaledata/Dennis+Schwartz/rating.Dennis+Schwartz',
    classes = './data/scaledata/Dennis+Schwartz/label.3class.Dennis+Schwartz'
  ),
  Object(
    contents = './data/scaledata/James+Berardinelli/subj.James+Berardinelli', 
    ratings = './data/scaledata/James+Berardinelli/rating.James+Berardinelli',
    classes = './data/scaledata/James+Berardinelli/label.3class.James+Berardinelli'
  ),
  Object(
    contents = './data/scaledata/Scott+Renshaw/subj.Scott+Renshaw', 
    ratings = './data/scaledata/Scott+Renshaw/rating.Scott+Renshaw',
    classes = './data/scaledata/Scott+Renshaw/label.3class.Scott+Renshaw'
  ),
  Object(
    contents = './data/scaledata/Steve+Rhodes/subj.Steve+Rhodes', 
    ratings = './data/scaledata/Steve+Rhodes/rating.Steve+Rhodes',
    classes = './data/scaledata/Steve+Rhodes/label.3class.Steve+Rhodes'
  ),
]

reviews = Reviews()

for data in reviewsData:
  reviews.load(contents=data.contents, ratings=data.ratings, classes=data.classes)

reviews.divideByRating()
crossValidation = 10
newReviews = [
  'Pictures, story and sound were amazing', 
  'Movie about some casual story',
  'This movie was terrible!'
]
# reviews.printStats(nFrequentWords=10, wordsMinLength=5)
def bayesian():
  bayesian = Bayesian(
    reviews.contents, 
    reviews.classes, 
    minDf=1, 
    ngram=(1, 2),
    maxFeatures=5000
  )
  bayesian.train(crossValidation, alpha=1, fit_prior=False)
  bayesian.predict(newReviews)

def svm():
  svm = SVM(
    reviews.contents, 
    reviews.classes, 
    minDf=1,
    ngram=(1, 2),
    maxFeatures=5000
  )
  svm.train(
    k=crossValidation, 
    tol=0.0001, 
    C=1, 
    max_iter=1000
  )
  svm.predict(newReviews)

# Execute
bayesian()
svm()
