class Reviews:
    contents = []
    ratings = []
    classes = []
    
    def load(self, contents: str, ratings: str, classes: str):
      with open(contents) as f:
        self.contents.extend(f.read().splitlines())
      with open(ratings) as f:
        self.ratings.extend(f.read().splitlines())
      with open(classes) as f:
        self.classes.extend(f.read().splitlines())
        
    def getData(self):
      print(len(self.contents))
      print(len(self.ratings))
      print(len(self.classes))
      return self.contents