class Animal():
    def __init__(self,weight,mood):
        self.weight = weight
        self.mood =mood
    def feed(self):
        pass
    def walk(self):
        pass
    def bath(self):
        pass
class Dogs(Animal):
    def __init__(self,weight,mood):
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
    def printf(self,n_feed,n_walk,n_bath):
        for i in range(0,n_feed):
            self.feed()
        for i in range(0,n_walk):
            self.walk()
        for i in range(0,n_bath):
            self.bath()
        print("狗狗現在的體重= "+str(self.weight)+" kg "+"心情 "+str(+self.mood))
class Shiba(Dogs):
    def __init__(self, weight, mood):
        self.weight = weight
        self.mood = mood
    def feed(self):
        self.weight +=0.3
        self.mood +=5
    def printf(self, n_feed, n_walk, n_bath):
        for i in range(0,n_feed):
            self.feed()
        for i in range(0,n_walk):
            self.walk()
        for i in range(0,n_bath):
            self.bath()
        print("柴犬現在的體重= "+str(round(self.weight,1))+" kg "+"心情 "+str(+self.mood))
    def mood_constraint(self, constraint):
        print ("mood最高只能為="+str(constraint))
        if self.mood >= constraint:
            print("所以，柴犬現在的心情"+str(constraint))
shiba = Shiba(5, 70) 
shiba.printf(20, 12, 3) 
shiba.mood_constraint(300)
