'''class book:
    bookCount=0
    def __init__(self,title,author,publsher):
        self.title=title
        self.author=author
        self.publsher=publsher
        bookCount+=1
    def del(self):
        del self
    def __str__(self):
        return "{} {} {}".format(self.title,self.author,self.publsher)
    def bookcount(self):
        return bookCount
book1=book("julius ceaser","william shakesphere","oxford")
book2=book("gulliver's travel","gulliver","cambridge")
print(bookcount)'''
'''class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    printed_rep = "*"

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def graph(self):
        rows = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size-1) :
            if (j+1) == int(self.y):
                special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                rows.append(special_row)
            else:
                rows.append(str((j+1) % 10))
        rows.reverse()  # put higher values of y first
        x_axis = ""
        for i in range(size):
            x_axis += str(i % 10)
        rows.append(x_axis)

        return "\n".join(rows)


p1 = Point(2, 3)
p2 = Point(3, 12)
print(p1.graph())
print()
print(p2.graph())'''
'''a=[0,1,2,3]
for a[-1] in a:
    print(a[-1])'''
'''import pyttsx3
engine=pyttsx3.init()
engine.say("something in the way")
engine.runAndWait()
'''
mylist=[1,2,3]
mylist.insert(1,'abc')
for x in mylist:
    print(x)
mylist.remove(1)
for x in mylist:
    print(x)