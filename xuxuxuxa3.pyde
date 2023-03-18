x = 50
z = 50
def setup():
    size(600,600)
def draw():
    clear()
    if mousePressed:
        global x,z
        ellipse(300,300,x,z)
        x += 3
        z += 3
