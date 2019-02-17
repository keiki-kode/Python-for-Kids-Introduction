import turtle

josh = turtle.Turtle()

def makeTriangle():
  for i in range(1,4):
    print(i)
    josh.forward(100)
    josh.left(120)

makeTriangle()
josh.left(120)
makeTriangle()
josh.left(120)
makeTriangle()

turtle.done()
