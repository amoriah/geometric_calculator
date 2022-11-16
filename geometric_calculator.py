from math import cos, sin, sqrt, pi, radians
import matplotlib.patches as pat
import matplotlib.pyplot as plt

def my_print_bye(P, S):
    print('Периметр фигуры =', P, 'Площадь фигуры =', S)
    print('До свидания!')

def my_square(a):
    P = a * 4
    S = a ** 2
    c = pat.Rectangle((a/4, a/4), a, a, angle = 0, facecolor= 'magenta', edgecolor='black', linewidth=2, alpha=0.4)
    ax = plt.axes()
    ax.set_xlim(0, a + a/2)
    ax.set_ylim(0, a + a/2)
    ax.add_patch(c)
    my_print_bye(P, S)

def my_rectangle(a, b):
    P = 2 * (a + b)
    S = a * b
    m = max(a, b)
    c = pat.Rectangle((a/2, a/2), a, b, angle = 0, facecolor= 'magenta', edgecolor='black', linewidth=2, alpha=0.4)
    ax = plt.axes()
    ax.set_xlim(0,m + m)
    ax.set_ylim(0, m + m)
    ax.add_patch(c)
    my_print_bye(P, S)

def my_triangle(a, b, al):
    P = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(al)) + a + b 
    S = (a * b * sin(al))/2
    c = sqrt(b ** 2 + a ** 2 - 2 * b * a * cos(al))
    print(c)
    m = max(a, b, c)
    by = b * cos(al)
    bx = b * sin(al)
    p = pat.Polygon(((0, 0), (0, a), (bx, by)), facecolor= 'magenta', edgecolor='black', linewidth=2, alpha=0.4)
    ax = plt.axes()
    ax.set_xlim(0, m + m/2)
    ax.set_ylim(0, m + m/2)
    ax.add_patch(p)
    my_print_bye(P, S)

def my_parallelogram(a, l, al):
    P = 2 * (a + l)
    S = a * l * sin(al)
    h = a * sin(al)
    b = sqrt((a ** 2) - (h ** 2))
    m = max(a, l)
    if al >= 1.5708:
        c = pat.Polygon(((0.3, 0.3), ( 0.3 + b, a), ( 0.3 + b + l, a), ( 0.3 + l,  0.3)), facecolor= 'magenta', edgecolor='black', linewidth=2, alpha=0.4)
    else:
        c = pat.Polygon(((0.3, a + 0.3), (0.3 + b, 0.3), (0.3 + b + l, 0.3), (0.3 + l, 0.3 + a)), facecolor= 'magenta', edgecolor='black', linewidth=2, alpha=0.4)
    ax = plt.axes()
    ax.set_xlim(0, m + m/2)
    ax.set_ylim(0, m + m/2)
    ax.add_patch(c)
    my_print_bye(P, S)

def my_rhombus(a, al):
    P = 4 * a
    S = a ** 2 * sin(al)
    h = a * sin(al)
    b = sqrt((a ** 2) - (h ** 2))
    c = pat.Polygon(((0.3, a + 0.3), ( 0.3 + b, 0.3), ( 0.3 + b + b, a + 0.3), ( 0.3 + b, 0.3 + a + a)), facecolor= 'magenta', edgecolor='black', linewidth=2, alpha=0.4)
    ax = plt.axes()
    ax.set_xlim(0, a + a + a/2)
    ax.set_ylim(0, a + a + a/2)
    ax.add_patch(c)
    my_print_bye(P, S)

def my_circle(r):
    P = 2 * pi * r
    S = (pi * r) ** 2
    c = pat.Circle((r + r/4, r+ r/4), r, facecolor= 'magenta', edgecolor='black', linewidth=2, alpha=0.4)
    ax = plt.axes()
    ax.set_xlim(0, r + r + r/2)
    ax.set_ylim(0, r + r + r/2)
    ax.set_aspect('equal')
    ax.add_patch(c)
    my_print_bye(P, S)

def my_ellipse(d1, d2):
    m = max(d1, d2)
    c = pat.Ellipse((d2 + d2/4, d1+ d1/4), d2, d1, 30, facecolor= 'magenta', edgecolor='black', linewidth=2, alpha=0.4)
    ax = plt.axes()
    ax.set_xlim(0, m + m)
    ax.set_ylim(0, m + m)
    ax.set_aspect('equal')
    ax.add_patch(c)
    P = 2 * pi * sqrt(((d1 / 2) * 2 + (d2 / 2) * 2)/2)
    S = pi * (d1/2 * d2/2)
    my_print_bye(P, S)

figure = int(input('Здравствуйте! Выберите фигуру, для этого введите соответствующую ей цифру:\n 1.Квадрат 2.Прямоугольник  3.Треугольник  4.Параллелограмм  5.Ромб  6.Круг  7.Эллипс'))
if figure > 7 or figure < 1: print ('Фигуры не существует. Завершение программы.')
elif figure == 1:
    a = int(input('Введите длину стороны a:'))
    my_square(a)
elif figure == 2:
    a = int(input('Введите длину стороны a:'))
    b = int(input('Введите длину стороны b:'))
    my_rectangle(a, b)
elif figure == 3 or figure == 4:
    a = int(input('Введите длину стороны a:'))
    b = int(input('Введите длину стороны b:'))
    al = int(input('Введите угол между ними:'))
    if figure == 3: my_triangle(a, b, radians(al))
    elif figure == 4: my_parallelogram(a, b, radians(al))
elif figure == 5:
    a = int(input('Введите длину стороны a:'))
    al = int(input('Введите угол a:'))
    my_rhombus(a, al)
elif figure == 6:
    r = float(input('Введите длину радиуса r:'))
    my_circle(r)
elif figure == 7:
    d1 = int(input('Введите длину максимального диаметра:'))
    d2 = int(input('Введите длину минимального диаметра:'))
    my_ellipse(d1, d2)
