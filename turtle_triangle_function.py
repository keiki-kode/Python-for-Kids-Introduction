import turtle

josh = turtle.Turtle()

def makeTriangle():
  for i in [1, 2, 3]:
    print(i)
    josh.forward(100)
    josh.left(120)

makeTriangle()
josh.left(120)
makeTriangle()
josh.left(120)
makeTriangle()

turtle.done()
