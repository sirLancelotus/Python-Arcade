from arcade import *
open_window(600,600,"Шедевр")
set_background_color(color=(112,33,191))
start_render()
'''Прямоугольники'''
draw_lrtb_rectangle_filled(0, 599, 300, 0, color=(124,232,42))
draw_lrtb_rectangle_filled(150, 449, 450, 150, color=(204,97,10))
draw_rectangle_filled(300,300,50,50,color=(49,222,222))
'''Маленький красный квадрат'''
draw_rectangle_outline(300,300,20,20,color=(240,10,10),border_width=5)
'''Жёлтый круг'''
draw_circle_filled(370,400,45,color=(240,223,38))
'''Голубой овал'''
draw_ellipse_outline(200,460,60,85,color=(112,224,150),border_width=6)
'''Три синие загогулины'''
draw_arc_filled(300,80,50,100,color=(12,22,135),start_angle=0,end_angle=180)
draw_arc_filled(400,80,50,100,color=(12,22,135),start_angle=0,end_angle=90)
draw_arc_filled(200,80,100,50,color=(12,22,135),start_angle=0,end_angle=90, tilt_angle=90)
'''Серый "Wi-Fi"'''
draw_arc_filled(300,480,100,100,color=(62,70,100),start_angle=45,end_angle=135)
'''Бежевый треугольник'''
draw_triangle_filled(55,120,90,240,125,120, color=(181,151,74))
# А вот это должна была быть звезда:
draw_polygon_filled(((475,225),(500,250),(525,275),(550,250),(575,225),(550,200),(563,150),(525,175),(513,150),(500,200)),color=(128,25,6))
# Но я не рассчитал, как работает заливка
# Поэтому оставляю как есть. Наверное, придётся склеивать из нескольких треугольников/полигонов...
'''Линия'''
draw_line(45,550,554,550,color=(245,176,27),line_width=6)
'''Ломаная'''
draw_line_strip(((45,35),(90,25),(135,35),(180,45),(225,35),(270,25),(315,35),(360,45),(405,35)),color=(207,148,21),line_width=6)
finish_render()
run()
