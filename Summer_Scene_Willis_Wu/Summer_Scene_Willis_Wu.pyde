import random
add_library('minim')
timer = False
timer_1 = 2100
timer_c = False
x1= 0
x2 =0
x3 =300
xa= random.randint(0,400)#random ints for the confettis
xb= random.randint(0,400)
xc=random.randint(0,400)
xd=random.randint(0,400)
xe=random.randint(0,400)
xf=random.randint(0,400)
y=0
backgroundcounter = 0
con = False
con_c = 300
add1 = 1
def setup():
    global background1, timer, timer_1, timer_c, x1, x2, x3, cl1, cl2, cl3, sun, moon, face,xa,y,xb,xc,xd,xe,xf, backgroundcounter,con, con_c
    size(494,692) 
    minim=Minim(this)#setting up for music
    music = minim.loadFile('music1.mp3')
    global music
    fill('#FF0000')
    background1 = loadImage('istockphoto-187444286-170667a.jpg')#loading images
    cl1 = loadImage('cl1.png')
    cl2 = loadImage('cl2.png')
    cl3 = loadImage('cl3.png')
    sun = loadImage('Sun.png')
    moon = loadImage('moon.jpg')
    face = loadImage('Capture.PNG')
    cl1.resize(50,30)#resizing 
    cl2.resize(60,40)
    cl3.resize(40,20)
    sun.resize(150,150)
    moon.resize(150,150)
    face.resize(50,70)
    background1.resize(988,692)                #resizing image
    image(background1,-494,0)
    
def keyPressed():#music control 
    global music
    music.loop()
    if key == 'p':
        music.play()
    elif key == 'a':
        music.pause()
    elif key == 'b':
        music.rewind()
    
def confetti():
    global xa, y, xb,xc,xd,xe,xf, backgroundcounter,con, con_c, add1
    
    rect(xa,y,8,20)#drawing different confettis
    rect(xb,y,8,20)
    rect(xc,y,8,20)
    rect(xd,y,8,20)
    rect(xe,y,8,20)
    rect(xf,y,8,20)
    xa+=add1#confettis that move in different directions
    xb+=add1
    xc+=add1
    xd-=add1
    xe-=add1
    xf-=add1

    if xa == 494:#sets a border for the confettis
        xa= 0
    elif xb == 494:
        xb= 0
    elif xc == 494:
        xc= 0
    elif xd == 0:
        xd= 494
    elif xe == 0:
        xe= 494
    elif xf == 0:
        xf= 494
    if y == 500:
        add1 = 0
        if con == False:
            con_c -=1
            if con_c == 0:
                con_c = 300
                con = True
        elif con == True:
            y = 0
            add1 = 1
            con = False
        
    if y>=200 and y <= 400:#changes colour
        fill('#00FFFF')
    if y>400:
        fill('#FF0000')
    y+=add1
def draw():
    global background1, timer, timer_1, timer_c, x1, x2, x3, cl1, cl2, cl3, sun, moon, face,xa,y,xb,xc,xd,xe,xf, backgroundcounter,con, con_c
    if timer == False:                         #detects if it needs the timer
        timer_1 -= 1
        if timer_1 == 0:                       #if timer count down ends
            timer_1 = 2100
            timer = True
        if timer_c == False:                   #detects which background to use
            image(background1,-494,0)
        elif timer_c == True:                  #detects which background to use
            image(background1,0,0)
    if timer == True:                          #detects if it needs to change the background
        if timer_c == False:                   #detects which background to use
            image(background1,-494,0)
            timer_c = True
        elif timer_c == True:                  #detects which background to use
            image(background1,0,0)
            timer_c = False
        timer = False
        timer_1 = 2100
        backgroundcounter += 1
    if backgroundcounter == 3:
        text("Have a restful summer and enjoy some good books!",x2,150)
    #sets a border for clouds, allows them to move accross the screen infinitly
    if x1 > width:
        x1 = 0
    image(cl1,x1,0)
    x1+=1
    if x2 < 0:
        x2 = width
    image(cl2,x2,45)
    x2-=1
    if x3 > width:
        x3 = 0
    image(cl3,x3,90)
    x3+=1
    #SUN AND MOON WITH MY FACE ON IT
    if timer_c == False:                   #detects which background to use
        fill('#808080')
        circle(70,60,150)
        image(face,50,40)
        confetti()
    elif timer_c == True:                  #detects which background to use
        fill('#FFFF00')
        circle(70,60,150)
        image(face,50,40)
        confetti()
    
    #making confetti
    confetti()
