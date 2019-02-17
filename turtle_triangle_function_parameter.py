import turtle

josh = turtle.Turtle()

def makeTriangle(myLenght):
  for i in range(1,4):
    print(i)
    josh.forward(myLenght)
    josh.left(120)

makeTriangle(100)
makeTriangle(50)
makeTriangle(20)

turtle.done()
