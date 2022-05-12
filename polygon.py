import turtle as t
import random as rd

def generate_polygon():
    polyturtle = t.Turtle()
    t.bgcolor('black')
    colors = ['aquamarine2', 'azure3', 'bisque1', 'blue2', 'brown1', 'CadetBlue3', 'chartreuse', 'coral4', 'CornflowerBlue', 'cornsilk1', 'DarkOrange3', 'DarkOrchid2', 'DeepPink', 'DodgerBlue', 'firebrick', 'honeydew', 'HotPink', 'IndianRed', 'khaki', 'lavender', 'LawnGreen', 'LimeGreen', 'magenta', 'maroon', 'MistyRose', 'MintCream', 'navy', 'orange', 'orchid', 'purple', 'red', 'RoyalBlue', 'SpringGreen', 'thistle', 'tomato', 'violet', 'yellow']
    sides = int(input('How many sides do you want the polygon to have?'))
    polyturtle.width(10)
    polyturtle.pencolor(rd.choice(colors))
    for i in range(0, sides):
        turn = 360/sides
        polyturtle.forward(1000/sides)
        polyturtle.right(turn)
    t.done()

def house():
    houset = t.Turtle()
    houset2 = t.Turtle()
    t.bgcolor('black')
    colors = ['aquamarine2', 'azure3', 'bisque1', 'blue2', 'brown1', 'CadetBlue3', 'chartreuse', 'coral4', 'CornflowerBlue', 'cornsilk1', 'DarkOrange3', 'DarkOrchid2', 'DeepPink', 'DodgerBlue', 'firebrick', 'honeydew', 'HotPink', 'IndianRed', 'khaki', 'lavender', 'LawnGreen', 'LimeGreen', 'magenta', 'maroon', 'MistyRose', 'MintCream', 'navy', 'orange', 'orchid', 'purple', 'red', 'RoyalBlue', 'SpringGreen', 'thistle', 'tomato', 'violet', 'yellow']
    houset.pencolor(rd.choice(colors))
    houset2.pencolor(rd.choice(colors))
    houset.width(10)
    houset2.width(10)
    houset.forward(65)
    houset2.backward(65)
    houset.left(90)
    houset2.left(90)
    houset.forward(75)
    houset2.forward(75)
    houset.right(90)
    houset2.left(90)
    houset.forward(30)
    houset2.forward(30)
    houset.left(135)
    houset2.right(135)
    houset.forward(136)
    houset2.forward(136)
    houset.hideturtle()
    houset2.hideturtle()
    t.done()

def star():
    pen = t.Turtle()
    colors = ['aquamarine2', 'azure3', 'bisque1', 'blue2', 'brown1', 'CadetBlue3', 'chartreuse', 'coral4', 'CornflowerBlue', 'cornsilk1', 'DarkOrange3', 'DarkOrchid2', 'DeepPink', 'DodgerBlue', 'firebrick', 'honeydew', 'HotPink', 'IndianRed', 'khaki', 'lavender', 'LawnGreen', 'LimeGreen', 'magenta', 'maroon', 'MistyRose', 'MintCream', 'navy', 'orange', 'orchid', 'purple', 'red', 'RoyalBlue', 'SpringGreen', 'thistle', 'tomato', 'violet', 'yellow']
    t.bgcolor('black')
    pen.width(10)
    for i in range(5):
        pen.pencolor(rd.choice(colors))
        pen.forward(200)
        pen.right(144)
    pen.hideturtle()
    t.done

# generate_polygon()
# house()
star()