from arcade import *

open_window(250,55,"Text")
set_background_color(color=(0,0,0))

start_render()

#Оказывается, удобнее прописывать расположение файла со шрифтом в папке Windows на компе, чем писать его название вручную
#Название шрифта срабатывает не всегда, тк функция чувствительна к регистру, количеству слов в названии и тд
#Поэтому вместо указания "нормального" названия шрифта, можно указывать его имя в системе
#Заходим в папку "C:\\Windows\\Fonts", находим нужный шрифт, смотрим свойства (иногда шрифтов в семействе несколько, тогда надо открыть их как папку)
#Вбиваем найденное название, не забываем указать папку (см ниже)
#Например, вместо " font_name='Blackadder ITC' ", которое не работает, мы впишем " font_name='C:/Windows/Fonts/ITCBLKAD' "

draw_text('''My small text''',10,10,color=(255,255,255),font_size=24,font_name='C:/Windows/Fonts/VINERITC')



finish_render()

run()
