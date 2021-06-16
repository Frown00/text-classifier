import statistics
from collections import Counter

class ContentFeatures:
  classId = None

  def __init__(self, classId):
      self.classId = classId
      self.contents = []
  
  def appendContent(self, content: str):
    self.contents.append(content)
    
  def getCount(self):
    return len(self.contents)
    
  def getCommonLength(self):
    lengths = []
    for c in self.contents:
      lengths.append(len(c))
    common = round(statistics.median(lengths))
    return common
  
  def getMostFrequentWords(self, n=None, wordLen=3):
    words = []
    for c in self.contents:
      newWords = c.split()
      longerWords = filter (lambda word: len (word) >= wordLen, newWords)
      words.extend(longerWords)
    vocabulary = Counter(words)
    top = []
    if(n == None):
      top = vocabulary.most_common()
    else:
      top = vocabulary.most_common(n)
    topWords = []
    for tuple in top:
      topWords.append(tuple[0])
    return topWords
  
  def getLeastFrequentWords(self, n=1, wordLen=3):
    words = []
    for c in self.contents:
      newWords = c.split()
      longerWords = filter (lambda word: len (word) >= wordLen, newWords)
      words.extend(longerWords)
    vocabulary = Counter(words)
    low = vocabulary.most_common()[:-n-1:-1]
    lowWords = []
    for tuple in low:
      lowWords.append(tuple[0])
    return lowWords


class Reviews:

    def __init__(self):
      self.ratings = []
      self.classes = []
      self.contents = []
      self.allContent = ContentFeatures('-1')
      self.positive = ContentFeatures('2')
      self.neutral = ContentFeatures('1')
      self.negative = ContentFeatures('0')
    
    def load(self, contents: str, ratings: str, classes: str):
      with open(contents) as f:
        self.contents.extend(f.read().splitlines())
      with open(ratings) as f:
        self.ratings.extend(f.read().splitlines())
      with open(classes) as f:
        self.classes.extend(f.read().splitlines())
      
      i = 0
      while i < len(self.classes):
        self.classes[i] = int(self.classes[i])
        i+=1
        
     
        
    def divideByRating(self):
      i = 0
      while i < len(self.contents):
        classId = self.classes[i]
        self.allContent.appendContent(self.contents[i])
        if(classId == '0'):
          self.negative.appendContent(self.contents[i])
        elif(classId == '1'):
          self.neutral.appendContent(self.contents[i])
        else:
          self.positive.appendContent(self.contents[i])
        i+= 1
    
    def getPositive(self):
      return self.positive
    
    def getNeutral(self):
      return self.neutral
    
    def getNegative(self):
      return self.negative
    
    def getCommonLength(self):
      return self.allContent.getCommonLength()
    
    def printStats(self, nFrequentWords=3, wordsMinLength=3):
      n = nFrequentWords
      wordLen = wordsMinLength
      print("POSITIVE")
      print("Count:", self.positive.getCount())
      print("Common Leangth:", self.positive.getCommonLength())
      print("Most frequent Words")
      print(self.positive.getMostFrequentWords(n, wordLen))
      print("Least frequent words")
      print(self.positive.getLeastFrequentWords(n, wordLen))
      print("\nNEUTRAL")
      print("Count:", self.neutral.getCount())
      print("Common Leangth:", self.neutral.getCommonLength())
      print("Most frequent Words")
      print(self.neutral.getMostFrequentWords(n, wordLen))
      print("Least frequent words")
      print(self.neutral.getLeastFrequentWords(n, wordLen))
      print("\nNEGATIVE")
      print("Count:", self.negative.getCount())
      print("Common Leangth:", self.negative.getCommonLength())
      print("Most frequent Words")
      print(self.negative.getMostFrequentWords(n, wordLen))
      print("Least frequent words")
      print(self.negative.getLeastFrequentWords(n, wordLen))
      
