import turtle as t
import random as rd

def generate_polygon():
    polyturtle = t.Turtle()
    colors = ['aquamarine2', 'azure3', 'bisque1', 'blue2', 'brown1', 'CadetBlue3', 'chartreuse', 'coral4', 'CornflowerBlue', 'cornsilk1', 'DarkOrange3', 'DarkOrchid2', 'DeepPink', 'DodgerBlue', 'firebrick', 'honeydew', 'HotPink', 'IndianRed', 'khaki', 'lavender', 'LawnGreen', 'LimeGreen', 'magenta', 'maroon', 'MistyRose', 'MintCream', 'navy', 'orange', 'orchid', 'purple', 'red', 'RoyalBlue', 'SpringGreen', 'thistle', 'tomato', 'violet', 'yellow']
    sides = int(input('How many sides do you want the polygon to have?'))
    polyturtle.width(10)
    polyturtle.pencolor(rd.choice(colors))
    for i in range(0, sides):
        turn = 360/sides
        polyturtle.forward(1000/sides)
        polyturtle.right(turn)
    t.done()

generate_polygon()
