'''
Модуль для основных операций над комплексными числами [+, -, *, /]
на вход поступают два числа комплексных и возdращается комплексное число

Комплексное число z=x+i*y храниться в виде кортежа (x, y)

Пояснение. Комплексное число – это двумерное число. Оно имеет вид
z = x + i*y, # хранится кортежем (x, y)

где  "x", "y" – действительные числа, "i" –  мнимая единица (i^2 = -1) 
Число "x" называется действительной частью (Re z) комплексного числа "z" (ось Ох).
Число "y" называется мнимой частью (Im z) комплексного числа 'z" (ось Оу).


Подробнее по ссылке ниже:
https://emirs.miet.ru/oroks-miet/upload/ftp/pub/orioks3/2017/5/TFKP_Lektsiya_1.pdf
'''
def sub_compl(z_left_side:tuple, z_right_side:tuple)-> tuple:   #z1 = (x1, y1)  z2 = (x2, y2)
    '''
    вычетание двух комплексных чисел: из "z1" вычесть "z2"
    вход :  2 числа в виде кордежа: z1 = (x1, y2), z2 = (x2, y2) <-> z = x + i*y                            
    выход : 1 число в виде кортежа: z3 = (x3, y3)  <-> z = x + i*y 
        Для того чтобы вычесть два комплексных числа 
        нужно вычесть их действительные и мнимые части (переставлять нельзя):
        z1 = x1 + i*y1  и   z2 = x2 + i*y2
        result = (x1 - x2) + (y1 - y2)*i
    '''
    re_z = z_left_side[0] - z_right_side[0] # дейсвительная часть
    im_z = z_left_side[1] - z_right_side[1] # мнимая часть
    return tuple(re_z, im_z)

def sum_compl(z_left_side:tuple, z_right_side:tuple)-> tuple:   #z1 = (x1, y1)  z2 = (x2, y2)
    '''
    сложение двух комплексных чисел
    вход :  2 числа в виде кордежа: z1 = (x1, y2), z2 = (x2, y2) <-> z = x + i*y                            
    выход : 1 число в виде кортежа: z3 = (x3, y3)  <-> z = x + i*y 
        Для того чтобы сложить два комплексных числа 
        нужно сложить их действительные и мнимые части:
        z1 = x1 + i*y1  и   z2 = x2 + i*y2
        result = (x1 + x2) + (y1 + y2)*i

    '''
    re_z = z_left_side[0] + z_right_side[0] # дейсвительная часть
    im_z = z_left_side[1] + z_right_side[1] # мнимая часть
    return tuple(re_z, im_z)

def mult_compl(z_left_side:tuple, z_right_side:tuple)-> tuple:   #z1 = (x1, y1)  z2 = (x2, y2)
    '''
    умножение двух комплексных чисел
    Умножение комплексных чисел производится, как умножение многочленов с учётом свойства числа i (i^2 = -1)
    z1 * z2 = (x1*x2 - y1*y2) + (y1*x2 + x1*y2)*i
    '''
    re_z = z_left_side[0] + z_right_side[0] # (x1*x2 - y1*y2) дейсвительная часть
    im_z = z_left_side[1] + z_right_side[1] # (y1*x2 + x1*y2) мнимая часть
    return tuple(re_z, im_z)

def div_compl(z_left_side:tuple, z_right_side:tuple)-> tuple:   #z1 = (x1, y1)  z2 = (x2, y2)
    '''
    деление двух комплексных чисел:"z1" разделить на "z2"
    Деление на произвольное комплексное число z2 не= 0
    можно свести к делению на действительное число, домножив и числитель, и знаменатель на число,
    комплексно сопряжённое знаменателю
    Примечание. Сопряжённое числу z2 = (x2, y2) будет число z2_sopr = (x2, -y2)
                                      x2 + y2*i                       x2 - y2*i
    '''
    epsilon = 0.0000000001
    if (abs(z_right_side[0] + z_right_side[0]) < epsilon):
        raise ZeroDivisionError # вызов исключения - деления на ноль
    elif (-epsilon < z_right_side[1] < +epsilon): # деление на действительное второе число z2 = x2 = x2 + 0*i
        re_z = z_left_side[0]  / z_right_side[0] # ~ x1 / x2
        im_z = z_left_side[1]  / z_right_side[0] # ~ y1 / x2
    else:
        mudul_z2_qwadrat = z_right_side[0] ** 2 + z_right_side[1] ** 2  # квадрат модуля делителя
        sopr_z2 = ( z_right_side[0], -z_right_side[1])                  # сопряжённое делителю
        chslitel = mult_compl(z_left_side, sopr_z2)                     # числитель: произведение левого_числа на сопряжённое делителю
    return tuple(chslitel[0] / mudul_z2_qwadrat, chslitel[1] / mudul_z2_qwadrat) # числитель разделить на квадрат модуля делителя