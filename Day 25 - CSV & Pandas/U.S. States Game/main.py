import turtle

canvas = turtle.Screen()
canvas.title("U.S. States Game")
image = "blank_states_img.gif"
canvas.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

