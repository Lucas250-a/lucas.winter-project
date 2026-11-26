import turtle as t

t.setup(1000,800)
t.bgcolor("#91B3E3")
t.title("Lucas's winter project")
t.tracer(0)

pen=t.Turtle()
pen.shape("triangle")
pen.color("#000000")


is_flying=False
base_gx=-300
base_gy=200
rocket_offset_y=0

def ground():
    a=(-500,-200)
    b=(500,-200)
    e=(-500,-400)
    f=(500,-400)
    pen.penup()
    pen.goto(a)
    pen.fillcolor("#EEEEEE")
    pen.begin_fill()
    pen.pendown()
    pen.goto(b)
    pen.goto(f)
    pen.goto(e)
    pen.goto(a)
    pen.end_fill()

def snow_man():
    #body
    fircir=(360,-200)
    seccir=(360,-90)
    thrcir=(360,0)
    #face
    lefeye=(345,50)
    righeye=(375,50)
    #nose
    toptri=(360,40)
    leftri=(355,35)
    rightri=(365,35)
    #mouth
    topleft=(350,25)
    topright=(370,25)
    downleft=(350,15)
    downrigh=(370,15)
    pen.penup()

    pen.goto(fircir)
    pen.fillcolor("#EEEEEE")
    pen.begin_fill()
    pen.pendown()
    pen.circle(60)
    pen.end_fill()

    pen.penup()
    pen.goto(seccir)
    pen.fillcolor("#EEEEEE")
    pen.begin_fill()
    pen.pendown()
    pen.circle(50)
    pen.end_fill()

    pen.penup()
    pen.goto(thrcir)
    pen.fillcolor("#EEEEEE")
    pen.begin_fill()
    pen.pendown()
    pen.circle(40)
    pen.end_fill()

    pen.penup()
    pen.goto(lefeye)
    pen.fillcolor("#000000")
    pen.begin_fill()
    pen.pendown()
    pen.circle(4)
    pen.end_fill()

    pen.penup()
    pen.goto(righeye)
    pen.fillcolor("#000000")
    pen.begin_fill()
    pen.pendown()
    pen.circle(4)
    pen.end_fill()

    pen.penup()
    pen.goto(toptri)
    pen.fillcolor("#DE4121")
    pen.begin_fill()
    pen.pendown()
    pen.goto(leftri)
    pen.goto(rightri)
    pen.goto(toptri)
    pen.end_fill()

    pen.penup()
    pen.goto(topleft)
    pen.fillcolor("#000000")
    pen.begin_fill()
    pen.pendown()
    pen.goto(topright)
    pen.goto(downrigh)
    pen.goto(downleft)
    pen.goto(topleft)
    pen.end_fill()

def draw_tree():
    top_left = (0,0)
    top_right = (80,0)
    bot_right = (80,-200)
    bot_left = (0,-200)
    #tri1
    b1=(-100,0)
    c1=(200,0)
    d1=(50,150)
    #tri2
    e1=(-100,100)
    f1=(200,100)
    g1=(50,250)

    pen.penup()
    pen.goto(top_left)

    pen.fillcolor("#7A4827")
    pen.begin_fill()

    pen.pendown()
    pen.goto(top_right)
    pen.goto(bot_right)
    pen.goto(bot_left)
    pen.goto(top_left)

    pen.end_fill()
    pen.penup()
    pen.goto(c1)
    pen.fillcolor("#008000")
    pen.begin_fill()

    pen.pendown()
    pen.goto(b1)
    pen.goto(d1)
    pen.goto(c1)
    pen.end_fill()

    pen.penup()
    pen.goto(f1)
    pen.fillcolor("#008000")
    pen.begin_fill()
    pen.pendown()
    pen.goto(g1)
    pen.goto(e1)
    pen.goto(f1)
    pen.end_fill()


def rocket(offset_y=0):
    g=(base_gx, base_gy + offset_y)
    h=(-350,100+offset_y)
    i=(-250,100+offset_y)
    v=(-350,-100+offset_y)
    w=(-250,-100+offset_y)

    m=(-320,-100+offset_y)
    n=(-280,-100+offset_y)
    o=(-320,-130+offset_y)
    l=(-300,-150+offset_y)
    p=(-280,-130+offset_y)

    u=(-290,-110+offset_y)
    r=(-290,-130+offset_y)
    s=(-310,-130+offset_y)
    tt=(-310,-110+offset_y)
    q=(-300,-140+offset_y)

    pen.penup()
    pen.goto(g)
    pen.pendown()

    pen.fillcolor("#707070")
    pen.begin_fill()
    pen.goto(h)
    pen.goto(v)
    pen.goto(w)
    pen.goto(i)
    pen.goto(g)
    pen.end_fill()

    pen.penup()
    pen.goto(m)
    pen.color("#ff2222")
    pen.fillcolor("#ff2222")
    pen.begin_fill()
    pen.pendown()
    pen.goto(o)
    pen.goto(l)
    pen.goto(p)
    pen.goto(n)
    pen.end_fill()

    pen.penup()
    pen.goto(tt)
    pen.color("#ff9900")
    pen.fillcolor("#ff9900")
    pen.begin_fill()
    pen.pendown()
    pen.goto(s)
    pen.goto(q)
    pen.goto(r)
    pen.goto(u)
    pen.end_fill()

    pen.penup()
    pen.goto(i)
    pen.color("#ffffff")
    pen.pendown()
    pen.goto(h)


def rocket_fly():
    global is_flying,rocket_offset_y
    is_flying=True

    
    while rocket_offset_y<600:
        rocket_offset_y+=2
        pen.clear()
        ground()
        line()
        draw_tree()
        snow_man()
        rocket(rocket_offset_y)
        t.update()


    wait_frame=0
    wait_max=120   
    while wait_frame<wait_max:
        wait_frame+=1
        pen.clear()
        ground()
        line()
        draw_tree()
        snow_man()
        rocket(rocket_offset_y)
        t.update()


    while rocket_offset_y>0:
        rocket_offset_y-=2
        pen.clear()
        ground()
        line()
        draw_tree()
        snow_man()
        rocket(rocket_offset_y)
        t.update()

    rocket_offset_y=0
    is_flying=False


def screen_click(mx,my):
    global is_flying
    if is_flying:
        return
    left  = -350
    right = -250
    bot_y=-100+rocket_offset_y
    top_y=200+rocket_offset_y
    if left<=mx<=right and bot_y<=my<=top_y:
        rocket_fly()

t.onscreenclick(screen_click)

def line():
    pen.penup()
    pen.goto(-500,-200)
    pen.pendown()
    pen.goto(500,-200)


pen.color("#ffffff")

ground()
line()
draw_tree()
snow_man()
rocket(0)

t.update()
t.done()
