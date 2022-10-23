class Animal():#建立父類別
    def __init__(self,weight,mood):
        self.weight = weight
        self.mood =mood
    def feed(self):
        pass
    def walk(self):
        pass
    def bath(self):
        pass
class Dogs(Animal):#建立子類別
    def __init__(self,weight,mood):#建構屬性
        self.weight = weight
        self.mood = mood
    def feed(self):
        self.weight +=0.2
        self.mood +=1
    def walk(self):
        self.weight -=0.2
        self.mood +=2
    def bath(self):
        self.mood -=2
    def printf(self,n_feed,n_walk,n_bath):#一個月內做的事情
        for i in range(0,n_feed):
            self.feed()
        for i in range(0,n_walk):
            self.walk()
        for i in range(0,n_bath):
            self.bath()
        print("狗狗現在的體重= "+str(self.weight)+" kg "+"心情 "+str(+self.mood))
class Cats(Animal):#建立子類別
    def __init__(self,weight,mood):
        self.weight = weight
        self.mood = mood
    def feed(self):
        self.weight +=0.1
        self.mood +=1
    def walk(self):
        self.weight -=0.1
        self.mood -=1
    def bath(self):
        self.mood -=2
    def printf(self,n_feed,n_walk,n_bath):#一個月內做的事情
        for i in range(0,n_feed):
            self.feed()
        for i in range(0,n_walk):
            self.walk()
        for i in range(0,n_bath):
            self.bath()
        f = round (self.mood,2)
        print("貓貓現在的體重= "+str(round(self.weight,1))+" kg "+"心情 "+str(f))
dog =Dogs(4.8,65)
dog.printf(18,10,4)
cat = Cats(8.2, 60) 
cat.printf(40, 7, 1) 


