import turtle
import random
import time
print("Merhabalar")
time.sleep(5)
print("MKYLisans Ürünüdür")
time.sleep(5)
print("Oyun Yükleniyor")
time.sleep(5)
print("Lütfen Ekrandaki Değerleri Giriniz.")

screen = turtle.Screen()

screen.bgcolor("light blue")
screen.title("MKYLisans Oyun V1.0")
FONT_1 = ('TimesNewRoman', 30, 'normal')
score_mky = 0
#turtle list
turtle_list=[]
grid_size_1= input("Kaplumbağ aralığı için sayı olarak çarpan giriniz(İdeal:100): ")
grid_size_2 = int(grid_size_1)
countdown_turtle = turtle.Turtle()
game_over = False


#score_turtle
score_turtle = turtle.Turtle()
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("red")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y_screen_oranı=input("% score ekranı için değer giriniz (İdeal:90): ")
    y_screen_oran1 = int(y_screen_oranı)
    y_1 = y_screen_oran1
    y_11= top_height * int(y_1) /100
    y_12=int(y_11)
    score_turtle.setpos(0,y_12)
    score_turtle.write("Score:0", move=False, align="center", font=FONT_1)


def make_turtle(x,y):
    t_1 = turtle.Turtle()
    def handle_click(x,y):
        global score_mky
        score_mky += 1
        score_turtle.clear()
        score_turtle.write(f"Score: {score_mky}", move=False, align="center", font=FONT_1)

        #print(x,y)
    t_1.onclick(handle_click)
    t_1.penup()
    t_1.shape("turtle")
    t_1.shapesize(2,2)
    t_1.color("dark orange")
    t_1.goto(x* grid_size_2,y* grid_size_2)
    turtle_list.append(t_1)

x_coordinates_1_MkyLisans= [-2,-1,0,1,2]
y_coordinates_1_MkyLisans= [-2,-1,-0,1,2]

def Mky_Lisans_turtles():
    for x in x_coordinates_1_MkyLisans:
        for y in y_coordinates_1_MkyLisans:
            make_turtle(x,y)

def hide_turtles_mky():
    for t_1 in turtle_list:
        t_1.hideturtle()

#udemyde yapılan
#recursive function
#def show_turtles_randomly():
    #hide_turtles_mky()
   #random.choice(turtle_list).showturtle()
    #screen.ontimer(show_turtles_randomly, 1000)
#benim yaptığım:
sanise_mky = None


def show_turtles_randomly():
    if not game_over:
        global sanise_mky
        hide_turtles_mky()
        random.choice(turtle_list).showturtle()
        if sanise_mky is None:
            sanise_mky1 = input("istediğiniz saniseyi giriniz(ideal : 1000): ")
            sanise_mky = int(sanise_mky1)
        sanise_mky += 1
        screen.ontimer(show_turtles_randomly, sanise_mky)

def countdown(time):
    global  game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("yellow")
    countdown_turtle.penup()
    top_height =screen.window_height() /2
    y = top_height * 0.9
    countdown_turtle.setposition(0,y - 30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT_1)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles_mky()
        countdown_turtle.write(arg="Game Over", move=False, align="center", font=FONT_1)


turtle.tracer(0)
setup_score_turtle()
Mky_Lisans_turtles()
hide_turtles_mky()
show_turtles_randomly()

countdown_1 = input("Kaç Saniye Süre İstersiniz(İdeal:10): ")
countdown_2 = int(countdown_1)
countdown(countdown_2)
turtle.tracer(1)
number_mky = 10
while number_mky > 0:
    print(number_mky)
    time.sleep(1)
    number_mky -= 1








turtle.mainloop()