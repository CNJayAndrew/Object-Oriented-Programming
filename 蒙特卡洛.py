class Mcmethod :
    import random
    global random
    def __init__ (self,times) :
        self.times = times

    def points(self) :
        self.x = []
        self.y = []
        for i in range(self.times) :
            self.x.append(random.random())
            self.y.append(random.random())
        return self.x , self.y

    def judge(self) :
        
        self.outcount = 0
        self.incount = 0
        for i in range(self.times) :
            self.points()
            if ((self.x[i]-0)**2+(self.y[i]-0)**2)**0.5 < 1 :
                self.incount += 1
            else :
                self.outcount += 1
        return self.incount , self.outcount

    def pi(self) :
        self.judge()
        pis = (self.incount/(self.incount + self.outcount))*4
        return print(pis)


pi1 = Mcmethod(10000)
pi1.pi()
