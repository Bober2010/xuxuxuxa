x = 300
napr = "p"

def setup():
    size(600,600)

def draw():
    
    global x, napr
    clear()
    ellipse(x, 300, 100,100)
    if mousePressed:
        if napr == "p":
            x += 1
        else:
            x -= 1
    
    if x ==550:
        napr = "l"
    elif x == 50:
        napr = "p"
