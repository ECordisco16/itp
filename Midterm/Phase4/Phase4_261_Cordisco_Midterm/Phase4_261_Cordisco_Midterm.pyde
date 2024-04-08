def setup():
    size(400, 400)
    noStroke()
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    #background(204)
    #fill(255)
    ellipse(50, 25, 30, 30)
    fill(0)
    
    triangle(30, 80, 50, 40, 70, 80)
    fill(0)
    
    fill (250)
    rect(25, 50,  20, 2) 
    rect(55, 50,  20, 2) 
    rect(55, 80, 2, 15) 
    rect(42, 80, 2 , 15) 
    pop()
    
def draw():
    drawObject(0,0,1)
    drawObject(0,10,2)
    
    x = width
    y = height
    for i in range (400,400):
        for j in range (400,400)

    #for (int i=0, i<5, i+1) 
    #draw(0+i*25, 0, 1)
