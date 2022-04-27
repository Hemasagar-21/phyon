'''class cookie:
    def __init__(self,color):
        self.color=color
    def getcolor(self):
        return self.color
    def setcolor(self,color):
        self.color=color
co=cookie("blue")
print(co.getcolor())
co.setcolor("green")
print(co.getcolor())'''
num1=11
num2=num1
num2=22
print(id(num1))
print(id(num2))
