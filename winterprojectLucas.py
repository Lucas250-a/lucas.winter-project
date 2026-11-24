import turtle as t

t.setup(1000,800)
t.bgcolor("#91B3E3")   
t.title("Lucas's winter project")
t.tracer(0)

pen=t.Turtle()
pen.shape("triangle")
pen.color("#000000")   #白色画笔 #ffffff

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
    lefeye=(350,20)
    righeye=(370,20)
    #nose
    toptri=(360,0)
    leftri=(355,-5)
    rightri=(365,-5)
    #mouth
    topleft=(350,-10)
    topright=(370,-10)
    downleft=(350,-20)
    downrigh=(370,-20)
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
    pen.pendown()
    pen.circle(4)
    pen.end_fill()
    pen.penup()
    pen.goto(righeye)
    pen.fillcolor("#000000")
    pen.pendown()
    pen.circle(4)
    pen.end_fill()
    
    





def draw_tree():
    #trunk 树干 正确顺序
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
    pen.goto(top_left)   #移动到图形起点

    pen.fillcolor("#7A4827") #填充颜色
    pen.begin_fill()         #开启填充！在pendown之前

    pen.pendown()

    pen.goto(top_right)
    pen.goto(bot_right)
    pen.goto(bot_left)
    pen.goto(top_left)  #回到起点闭合图形

    pen.end_fill() #结束填充
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










    
    

def rocket():
    
    #火箭机身坐标点
    g=(-300,200)
    h=(-350,100)
    i=(-250,100)
    v=(-350,-100)
    w=(-250,-100)

    #火焰外层坐标
    m=(-320,-100)
    n=(-280,-100)
    o=(-320,-130)
    l=(-300,-150)
    p=(-280,-130)
    #火焰内层坐标
    u=(-290,-110)
    r=(-290,-130)
    s=(-310,-130)
    tt=(-310,-110)
    q=(-300,-140)

    pen.penup()
    pen.goto(g)
    pen.pendown()

   
    pen.fillcolor("#707070") #机身灰色 hex色号
    pen.begin_fill()         #开始填充
    pen.goto(h)
    pen.goto(v)
    pen.goto(w)
    pen.goto(i)
    pen.goto(g)              #回到起点，闭合多边形
    pen.end_fill()           #结束填充
    # =============================

    #外层红色火焰
    pen.penup()
    pen.goto(m)
    pen.color("#ff2222") #红色hex
    pen.fillcolor("#ff2222")
    pen.begin_fill()
    pen.pendown()
    pen.goto(o)
    pen.goto(l)
    pen.goto(p)
    pen.goto(n)
    pen.end_fill()

    #内层橙色火焰
    pen.penup()
    pen.goto(tt)
    pen.color("#ff9900") #橙色hex
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
    pen.color("#ffffff") #恢复画笔白色
    pen.pendown()
    pen.goto(h)


def line():
    """画底部水平参考线"""
    pen.penup()
    pen.goto(-500,-200)
    pen.pendown()
    pen.goto(500,-200)


pen.color("#ffffff")
rocket()
line()
draw_tree()
snow_man()
ground()


t.update()
t.done()
