x = 50
z = 50
def setup():
    size(600,600)
def draw():
    background(100)
    global x,z
    ellipse(300,300,x,z)
    x += 3
    z += 3
def mouseClicked():
    global x,z
    x = 50
    z = 50
