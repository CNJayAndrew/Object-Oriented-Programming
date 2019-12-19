class student() :
    def __init__ (self,name) :
        self.name = name
        self.heigh = 0

a=student ("韩杰")
b=student ("宋云龙")
c= student ("郭鸿博")
d= student ("夏祥铭")
e= student ("任皓宇")
f= student ("徐奚嘉")

a.heigh = 185
b.heigh = 176
c.heigh = 180
d.heigh = 177
e.heigh = 178
f.heigh = 175

max_height = 0
max_people = "unknown"

for i in [a,b,c,d,e,f] :
    if i.heigh > max_height :
        max_height = i.heigh
        max_people = i.name

print (max_people,max_height)