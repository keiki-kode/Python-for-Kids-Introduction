import turtle

josh = turtle.Turtle()

def makeTriangle(myLenght):
  for i in [1, 2, 3]:
    print(i)
    josh.forward(myLenght)
    josh.left(120)

makeTriangle(100)
josh.left(120)
makeTriangle(50)
josh.left(120)
makeTriangle(20)

turtle.done()
