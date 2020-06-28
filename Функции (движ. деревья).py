from arcade import *

"""
ОПИСАНИЕ ФУНКЦИЙ
"""

def Tree1(x_coord,y_coord):
    #Создаёт круглое дерево
    draw_rectangle_filled(x_coord,y_coord,35,80,color=(107,58,58))
    draw_circle_filled(x_coord,y_coord+70,45,color=(78, 117, 30))

def Tree2(x_coord,y_coord):
    #Создаёт овальное дерево
    draw_rectangle_filled(x_coord,y_coord,35,80,color=(107,58,58))
    draw_ellipse_filled(x_coord,y_coord+70,75,95,color=(78, 117, 30))

def Tree3(x_coord,y_coord):
    #Создаёт куполообразное дерево
    draw_rectangle_filled(x_coord,y_coord,35,80,color=(107,58,58))
    draw_arc_filled(x_coord,y_coord+25,75,135,color=(78, 117, 30), start_angle=0, end_angle=180)

def Tree4(x_coord,y_coord):
    #Создаёт треугольное дерево
    draw_rectangle_filled(x_coord,y_coord,35,80,color=(107,58,58))
    draw_triangle_filled(x_coord, y_coord+100,x_coord-40,y_coord-10,x_coord+40,y_coord-10,color=(78, 117, 30))

def Tree5(x_coord,y_coord):
    #Создаёт пятиугольное дерево
    draw_rectangle_filled(x_coord,y_coord,35,80,color=(107,58,58))
    draw_polygon_filled(((x_coord,y_coord+100),(x_coord-27,y_coord+30),(x_coord-35,y_coord-10),(x_coord+35,y_coord-10),(x_coord+27,y_coord+30)), color=(78, 117, 30))

def draw_world():
    #Создаёт небо и землю
    draw_lrtb_rectangle_filled(0,1000,550,220,color=(149, 245, 229))
    draw_lrtb_rectangle_filled(0,1000,220,0,color=(45, 194, 55))

def draw_sun():
    #Создаёт солнце
    draw_circle_filled(850, 500, 40, color=(237,227,33))
    #Прямые лучи
    draw_line(770, 500, 930, 500, color=(237,227,33), line_width=3)
    draw_line(850, 580, 850, 420, color=(237,227,33), line_width=3)
    #Диагональные лучи
    draw_line(800, 550, 900, 450, color=(237,227,33), line_width=3)
    draw_line(800, 450, 900, 550, color=(237,227,33), line_width=3)
    
def on_draw(delta_time):
    #Начинает рендер
    start_render()
    #Рисует окружение
    draw_world()
    draw_sun()
    draw_text('''Оживший лес!''', 315,380, color=(235,128,23), font_size=28, font_name='C:/Windows/Fonts/segoesc')
    #Рисует деревья и изменяет их координату - смотри main()
    Tree5(on_draw.Tree5_x,90)
    Tree4(on_draw.Tree4_x,90)
    Tree3(on_draw.Tree3_x,90)
    Tree2(on_draw.Tree2_x,90)
    Tree1(450,90)
    on_draw.Tree5_x -= 1
    on_draw.Tree4_x += 1
    on_draw.Tree3_x += 2
    on_draw.Tree2_x -= 2
#Начальное положение деревьев (по оси X)
on_draw.Tree5_x = 650    
on_draw.Tree4_x = 250
on_draw.Tree3_x = 50
on_draw.Tree2_x = 850

def main():
    #Создаёт окно
    open_window(900,550, "Оживший лес")
    #Перерисовывает экран раз в 1/360 секунды
    schedule(on_draw, 1/360)
    #Запускает программу
    run()

""""""
main()
""""""
