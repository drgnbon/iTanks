# подключение библиотек\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

game = True
tanks = False  # цикл игрового процесса
menu = True
gameover = False
while game:
    import pygame
    pygame.init()  # инициализация pygame
    window = pygame.display.set_mode((1000, 800))  # установка размеров окна
    # присвоение название игре
    pygame.display.set_caption(
        "iTanksX 1.0 beta      all rights reserved by Evgeniy")
    import time
    # инициализация картинок\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    yellow = (255, 255,   0)
    green = (0, 128,   0)
    red = (255,   0,   0)
    red2 = (29,   15,   51)
    mario = pygame.font.Font(r'C:\10852.otf', 40)
    mario2 = pygame.font.Font(r'C:\10852.otf', 150)
    walkRight = [pygame.image.load(r'D:\iTanks\datamages\right_1.png'), pygame.image.load(
        r'D:\iTanks\datamages\right_2.png')]
    walkLeft = [pygame.image.load(r'D:\iTanks\datamages\left_1.png'), pygame.image.load(
        r'D:\iTanks\datamages\left_2.png')]
    walkUp = [pygame.image.load(r'D:\iTanks\datamages\up_1.png'), pygame.image.load(
        r'D:\iTanks\datamages\up_2.png')]
    walkDown = [pygame.image.load(r'D:\iTanks\datamages\down_1.png'), pygame.image.load(
        r'D:\iTanks\datamages\down_2.png')]

    walkRight2 = [pygame.image.load(r'D:\iTanks\datamages\right_1 yellow.png'), pygame.image.load(
        r'D:\iTanks\datamages\right_2 yellow.png')]
    walkLeft2 = [pygame.image.load(r'D:\iTanks\datamages\left_1 yellow.png'), pygame.image.load(
        r'D:\iTanks\datamages\left_2 yellow.png')]
    walkUp2 = [pygame.image.load(r'D:\iTanks\datamages\up_1 yellow.png'), pygame.image.load(
        r'D:\iTanks\datamages\up_2 yellow.png ')]
    walkDown2 = [pygame.image.load(r'D:\iTanks\datamages\down_1 yellow.png'), pygame.image.load(
        r'D:\iTanks\datamages\down_2 yellow.png')]

    walkDR = [pygame.image.load(r'D:\iTanks\datamages\down_right.png'), pygame.image.load(
        r'D:\iTanks\datamages\down_right.png')]
    walkDL = [pygame.image.load(r'D:\iTanks\datamages\down_left.png'), pygame.image.load(
        r'D:\iTanks\datamages\down_left.png')]
    walkUR = [pygame.image.load(r'D:\iTanks\datamages\up_right.png'), pygame.image.load(
        r'D:\iTanks\datamages\up_right.png')]
    walkUL = [pygame.image.load(r'D:\iTanks\datamages\up_left.png'), pygame.image.load(
        r'D:\iTanks\datamages\up_left.png')]
    walkDR2 = [pygame.image.load(r'D:\iTanks\datamages\down_right yellow.png'), pygame.image.load(
        r'D:\iTanks\datamages\down_right.png')]
    walkDL2 = [pygame.image.load(r'D:\iTanks\datamages\down_left yellow.png'), pygame.image.load(
        r'D:\iTanks\datamages\down_left.png')]
    walkUR2 = [pygame.image.load(r'D:\iTanks\datamages\up_right yellow.png'), pygame.image.load(
        r'D:\iTanks\datamages\up_right.png')]
    walkUL2 = [pygame.image.load(r'D:\iTanks\datamages\up_left yellow.png'), pygame.image.load(
        r'D:\iTanks\datamages\up_left.png')]

    shot = pygame.image.load(r'D:\iTanks\datamages\shot.png')
    shot2 = pygame.image.load(r'D:\iTanks\datamages\shot2.png')
    home1 = pygame.image.load(r'D:\iTanks\datamages\home1.png')
    home2 = pygame.image.load(r'D:\iTanks\datamages\home2.png')

    shotleft = pygame.image.load(r'D:\iTanks\datamages\leftfire.png')
    shotright = pygame.image.load(r'D:\iTanks\datamages\rightfire.png')
    shotdown = pygame.image.load(r'D:\iTanks\datamages\downfire.png')
    shotup = pygame.image.load(r'D:\iTanks\datamages\upfire.png')

    shotleft2 = pygame.image.load(r'D:\iTanks\datamages\leftfire yellow.png')
    shotright2 = pygame.image.load(r'D:\iTanks\datamages\rightfire yellow.png')
    shotdown2 = pygame.image.load(r'D:\iTanks\datamages\downfire yellow.png')
    shotup2 = pygame.image.load(r'D:\iTanks\datamages\upfire yellow.png')

    p1 = pygame.image.load(r'D:\iTanks\datamages\play.png')
    pt2 = pygame.image.load(r'D:\iTanks\datamages\play2.png')

    background = pygame.image.load(r'D:\iTanks\datamages\Background.png')
    menu2 = pygame.image.load(r'D:\iTanks\datamages\menu.png')
    gm = pygame.image.load(r'D:\iTanks\datamages\gm.png')

    lefttank = pygame.image.load(r'D:\iTanks\datamages\left_1.png')
    righttank = pygame.image.load(r'D:\iTanks\datamages\right_1.png')
    uptank = pygame.image.load(r'D:\iTanks\datamages\up_1.png')
    downtank = pygame.image.load(r'D:\iTanks\datamages\down_1.png')

    lefttank2 = pygame.image.load(r'D:\iTanks\datamages\left_1 yellow.png')
    righttank2 = pygame.image.load(r'D:\iTanks\datamages\right_1 yellow.png')
    uptank2 = pygame.image.load(r'D:\iTanks\datamages\up_1 yellow.png')
    downtank2 = pygame.image.load(r'D:\iTanks\datamages\down_1 yellow.png')
    play = pygame.image.load(r'D:\iTanks\datamages\play.png')

    UL = pygame.image.load(r'D:\iTanks\datamages\up_left.png')
    UR = pygame.image.load(r'D:\iTanks\datamages\up_right.png')
    DR = pygame.image.load(r'D:\iTanks\datamages\down_right.png')
    DL = pygame.image.load(r'D:\iTanks\datamages\down_left.png')
    UL2 = pygame.image.load(r'D:\iTanks\datamages\up_left yellow.png')
    UR2 = pygame.image.load(r'D:\iTanks\datamages\up_right yellow.png')
    DR2 = pygame.image.load(r'D:\iTanks\datamages\down_right yellow.png')
    DL2 = pygame.image.load(r'D:\iTanks\datamages\down_left yellow.png')
    frame1 = pygame.image.load(r'D:\iTanks\datamages\frame-1.png')
    frame2 = pygame.image.load(r'D:\iTanks\datamages\frame-2.png')
    frame3 = pygame.image.load(r'D:\iTanks\datamages\frame-3.png')
    frame4 = pygame.image.load(r'D:\iTanks\datamages\frame-4.png')
    frame5 = pygame.image.load(r'D:\iTanks\datamages\frame-5.png')
    frame6 = pygame.image.load(r'D:\iTanks\datamages\frame-6.png')
    frame7 = pygame.image.load(r'D:\iTanks\datamages\frame-7.png')
    frame8 = pygame.image.load(r'D:\iTanks\datamages\frame-8.png')
    frame9 = pygame.image.load(r'D:\iTanks\datamages\frame-9.png')
    frame10 = pygame.image.load(r'D:\iTanks\datamages\frame-10.png')
    frame11 = pygame.image.load(r'D:\iTanks\datamages\frame-11.png')
    frame12 = pygame.image.load(r'D:\iTanks\datamages\frame-12.png')
    frame13 = pygame.image.load(r'D:\iTanks\datamages\frame-13.png')
    frame14 = pygame.image.load(r'D:\iTanks\datamages\frame-14.png')
    frame15 = pygame.image.load(r'D:\iTanks\datamages\frame-15.png')
    frame16 = pygame.image.load(r'D:\iTanks\datamages\frame-16.png')
    frame17 = pygame.image.load(r'D:\iTanks\datamages\frame-17.png')
    frame18 = pygame.image.load(r'D:\iTanks\datamages\frame-18.png')
    frame19 = pygame.image.load(r'D:\iTanks\datamages\frame-19.png')
    frame20 = pygame.image.load(r'D:\iTanks\datamages\frame-20.png')
    frame21 = pygame.image.load(r'D:\iTanks\datamages\frame-21.png')
    frame22 = pygame.image.load(r'D:\iTanks\datamages\frame-22.png')
    frame23 = pygame.image.load(r'D:\iTanks\datamages\frame-23.png')
    frame24 = pygame.image.load(r'D:\iTanks\datamages\frame-24.png')
    frame25 = pygame.image.load(r'D:\iTanks\datamages\frame-25.png')
    frame26 = pygame.image.load(r'D:\iTanks\datamages\frame-26.png')
    frame27 = pygame.image.load(r'D:\iTanks\datamages\frame-27.png')
    frame28 = pygame.image.load(r'D:\iTanks\datamages\frame-28.png')
    frame29 = pygame.image.load(r'D:\iTanks\datamages\frame-29.png')
    loading1 = pygame.image.load(r'D:\iTanks\datamages\loading1.png')
    loading2 = pygame.image.load(r'D:\iTanks\datamages\loading2.png')
    loading3 = pygame.image.load(r'D:\iTanks\datamages\loading3.png')
    loading4 = pygame.image.load(r'D:\iTanks\datamages\loading4.png')

    # инициализация картинок\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    # данные проверки для игроков\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    x = 25  # положение (игрока 1) по x
    y = 38  # положение (игрока 1) по y
    x3 = int()
    y3 = int()
    y4 = int()
    x4 = int()
    weight = 126  # размеры (игрока 1) ширина
    height = 40  # размеры (игрока 1) высота
    speed = 0  # cкорость (игрока 1) (пиксели/за один шаг)
    speed2 = 0.20  # cкорость под углом (игрока 1) (пиксели/за один шаг)
    lastank = str()  # полседнее положение (игрока 1)
    clock = pygame.time.Clock()  # переменная ограничения Fps
    lastMove = "right"
    bullet = ()
    shotest = str()
    # данные проверки для игроков\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    x2 = 845  # положение (игрока 1) по x
    y2 = 718  # положение (игрока 1) по y
    weight2 = 126  # размеры (игрока 1) ширина
    height2 = 40  # размеры (игрока 1) высота
    speedy = 0  # cкорость (игрока 1) (пиксели/за один шаг)
    speed2y = 0.20  # cкорость под углом (игрока 1) (пиксели/за один шаг)
    lastank2 = str()  # полседнее положение (игрока 1)
    clock2 = pygame.time.Clock()  # переменная ограничения Fps
    lastMove2 = "right"
    bullet2 = ()
    bullet2y = ()
    bullety = ()
    shotest2 = str()
    hp2 = int()
    hp1 = int(350)
    raund = int(0)
    raund1 = int()
    raund2 = int()
    otrezok = int(0)
    damageshels1 = int(0)
    damageshels2 = int(0)
    nodamageshels1 = int(0)
    nodamageshels2 = int(0)
    shelsf1 = int(0)
    shelsf2 = int(0)
    score1 = int(0)
    score2 = int(0)

    # boolean Переменные\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    left = False  # проверка влево
    right = False  # проверка вправо
    down = False  # проверка вниз
    bull = False
    pl = False
    load = False
    up = False  # проверка вверх
    ru = False  # проверка вправо-вверх
    rd = False  # проверка вправо-вниз
    ld = False  # проверка влево-вниз
    lu = False  # проверка влево-вверх
    lastturn = False  # последний поворот игрока
    firststart = True  # проверка первого запуска
    speedtest = False  # проверка наличия разгона
    speedtesty = False  # проверка наличия разгона под углом
    stopleft = False  # проверка на дрифт
    stopright = False  # проверка на дрифт
    stopdown = False  # проверка на дрифт
    stopup = False  # проверка на дрифт
    n = False
    n2 = False
    a = False  # проверка нажато ли а
    d = False  # проверка нажато ли d
    s = False  # проверка нажато ли s
    w = False  # проверка нажато ли w
    l = False
    l2 = False
    e = False
    p = int()
    m = int()

    # boolean Переменные\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    left2 = False  # проверка влево
    right2 = False  # проверка вправо
    down2 = False  # проверка вниз
    bull2 = False
    pl2 = False
    up2 = False  # проверка вверх
    ru2 = False  # проверка вправо-вверх
    rd2 = False  # проверка вправо-вниз
    ld2 = False  # проверка влево-вниз
    lu2 = False  # проверка влево-вверх
    lastturn2 = False  # последний поворот игрока
    firststart2 = True  # проверка первого запуска
    speedtest2 = False  # проверка наличия разгона
    speedtest2y = False  # проверка наличия разгона под углом
    stopleft2 = False  # проверка на дрифт
    stopright2 = False  # проверка на дрифт
    stopdown2 = False  # проверка на дрифт
    stopup2 = False  # проверка на дрифт
    n2 = False
    n22 = False
    animate2 = 0
    animate = 0
    a2 = False  # проверка нажато ли а
    d2 = False  # проверка нажато ли d
    s2 = False  # проверка нажато ли s
    w2 = False  # проверка нажато ли w
    l2 = False
    l22 = False
    e2 = False
    sh1 = bool()
    sh2 = bool()
    p2 = int()
    m2 = int()

    class snaryad():
        def __init__(self, x, y, facing):
            self.x = x
            self.y = y
            self.facing = facing
            self.vel = 8 * facing

        def draw(self, window):
            global hp2
            for bullet in bullets:
                if x2 + 60 < self.x or x2 > self.x or y2 + 40 < self.y or y2 > self.y:
                    n = True
                    l = True
                    sh1 = True
                else:
                    hp2 -= 50
                    sh1 = False
                    l = False
                    n = False
                    bullets.clear()
            if sh1:
                window.blit(shot, (self.x+30, self.y))

    class snaryad2():
        def __init__(self, x, y, facing2):
            self.x = x
            self.y = y
            self.facing2 = facing2
            self.vel = 8 * facing2

        def draw2(self, window):
            global hp2
            for bullet2 in bullets2:
                if x2 + 120 < self.x or x2 + 40 > self.x or y2 + 40 < self.y or y2 > self.y:
                    n = True
                    l = True
                    sh1 = True

                else:
                    hp2 -= 50
                    sh1 = False
                    l = False
                    n = False
                    bullets2.clear()

            if sh1:
                window.blit(shot, (self.x - 43, self.y+80))

    class snaryady():
        def __init__(self, x2, y2, facingy):
            self.x2 = x2
            self.y2 = y2
            self.facingy = facingy
            self.vel2 = 8 * facingy

        def drawy(self, window):
            global hp1

            for bullety in bulletsy:
                if x + 60 < self.x2 or x > self.x2 or y + 40 < self.y2 or y > self.y2:
                    n2 = True
                    l2 = True
                    sh2 = True
                else:
                    hp1 -= 50
                    sh2 = False
                    l2 = False
                    n2 = False
                    bulletsy.clear()

            if sh2:
                window.blit(shot2, (self.x2+30, self.y2))

    class snaryad2y():
        def __init__(self, x2, y2, facingy):
            self.x2 = x2
            self.y2 = y2
            self.facing2y = facing2y
            self.vel2 = 8 * facing2y

        def draw2y(self, window):
            global hp1
            for bullety in bullets2y:
                if x + 120 < self.x2 or x + 40 > self.x2 or y + 40 < self.y2 or y > self.y2:
                    n2 = True
                    l2 = True
                    sh2 = True
                else:
                    hp1 -= 50
                    sh2 = False
                    l2 = False
                    n2 = False
                    bullets2y.clear()

            if sh2:
                window.blit(shot2, (self.x2-43, self.y2))

    def anim2():
        # обозначение глобальных переменных\\\\\\\\\\\\\\\\\\\\\\
        global animate2
        global speed2
        global speed2y
        global lastank2
        global firststart2
        global downturn2
        global upturn2
        global rightturn2
        global leftturn2
        global g2
        global shotest2
        global left2
        global e2
        window.blit(background, (0, 0))
        if animate2 + 1 >= 18:
            animate2 = 0
        if firststart2:
            window.blit(walkLeft2[animate2 // 9], (x2, y2))

        if lastMove2 == "left" and l2:
            for bullety in bulletsy:
                bullety.drawy(window)
            window.blit(shotleft2, (x2-35, y2))
        elif lastMove2 == "right" and l2:
            for bullety in bulletsy:
                bullety.drawy(window)
            window.blit(shotright2, (x2-15, y2))
        elif lastMove2 == "down" and l2:
            for bullet2y in bullets2y:
                bullet2y.draw2y(window)
            window.blit(shotdown2, (x2, y2-15))
        elif lastMove2 == "up" and l2:
            for bullet2y in bullets2y:
                bullet2y.draw2y(window)
            window.blit(shotup2, (x2, y2-15))

        else:
            if left2:  # проверка влево
                firststart2 = False
                window.blit(walkLeft2[animate2 // 9], (x2, y2))
                lastank2 = 'left'
                animate2 += 1
            elif right2:  # проверка вправо
                firststart2 = False
                window.blit(walkRight2[animate2 // 9], (x2, y2))
                lastank2 = 'right'
                animate2 += 1
            elif up2:  # проверка вверх
                firststart2 = False
                window.blit(walkUp2[animate2 // 9], (x2, y2))
                lastank2 = 'up'
                animate2 += 1
            elif down2:  # проверка вниз
                firststart2 = False
                window.blit(walkDown2[animate2 // 9], (x2, y2))
                lastank2 = 'down'
                animate2 += 1
            elif rd2:  # проверка вправо-вниз
                firststart2 = False
                window.blit(DR2, (x2, y2))
                lastank2 = 'DR'

            elif ru2:  # проверка вправо-вверх
                firststart2 = False
                window.blit(UR2, (x2, y2))
                lastank2 = 'UR'
                animate2 += 1
            elif ld2:  # проверка влево-вниз
                firststart2 = False
                window.blit(DL2, (x2, y2))
                lastank2 = 'DL'
                animate2 += 1
            elif lu2:  # проверка влево-вверх
                firststart2 = False
                window.blit(UL2, (x2, y2))
                lastank2 = 'UL'
                animate2 += 1
            else:  # проверка последнего изображения\\\\\\\\\
                if lastank2 == 'left':
                    window.blit(lefttank2, (x2, y2))
                elif lastank2 == 'right':
                    window.blit(righttank2, (x2, y2))
                elif lastank2 == 'up':
                    window.blit(uptank2, (x2, y2))
                elif lastank2 == 'down':
                    window.blit(downtank2, (x2, y2))
                elif lastank2 == 'DR':
                    window.blit(DR2, (x2, y2))
                elif lastank2 == 'DL':
                    window.blit(DL2, (x2, y2))
                elif lastank2 == 'UR':
                    window.blit(UR2, (x2, y2))
                elif lastank2 == 'UL':
                    window.blit(UL2, (x2, y2))

    # функция для создания анимации\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    def anim():

        # обозначение глобальных переменных\\\\\\\\\\\\\\\\\\\\\\
        global animate
        global speed
        global speed2
        global lastank
        global firststart
        global downturn
        global upturn
        global rightturn
        global leftturn
        global g
        global shotest
        global left
        global e
        # обозначение глобальных переменных\\\\\\\\\\\\\\\\\\\\\\

        # настройка спрайтов\\\\\\\\\\\\
        if animate + 1 >= 18:
            animate = 0
        # настройка спрайтов\\\\\\\\\\\\\

        # проверка первого запуска\\\\\\\\
        if firststart:
            window.blit(righttank, (x, y))
        # проверка первого запуска\\\\\\\\

        # анимация танка\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        if lastMove == "left" and l:
            for bullet in bullets:
                bullet.draw(window)
            window.blit(shotleft, (x-35, y))
        elif lastMove == "right" and l:
            for bullet in bullets:
                bullet.draw(window)
            window.blit(shotright, (x-15, y))
        elif lastMove == "down" and l:
            for bullet2 in bullets2:
                bullet2.draw2(window)
            window.blit(shotdown, (x, y-15))
        elif lastMove == "up" and l:
            for bullet2 in bullets2:
                bullet2.draw2(window)
            window.blit(shotup, (x, y-15))
        else:
            if left:  # проверка влево
                firststart = False
                window.blit(walkLeft[animate // 9], (x, y))
                lastank = 'left'
                animate += 1
            elif right:  # проверка вправо
                firststart = False
                window.blit(walkRight[animate // 9], (x, y))
                lastank = 'right'
                animate += 1
            elif up:  # проверка вверх
                firststart = False
                window.blit(walkUp[animate // 9], (x, y))
                lastank = 'up'
                animate += 1
            elif down:  # проверка вниз
                firststart = False
                window.blit(walkDown[animate // 9], (x, y))
                lastank = 'down'
                animate += 1
            elif rd:  # проверка вправо-вниз
                firststart = False
                window.blit(walkDR[animate // 9], (x, y))
                lastank = 'DR'
                animate += 1
            elif ru:  # проверка вправо-вверх
                firststart = False
                window.blit(walkUR[animate // 9], (x, y))
                lastank = 'UR'
                animate += 1
            elif ld:  # проверка влево-вниз
                firststart = False
                window.blit(walkDL[animate // 9], (x, y))
                lastank = 'DL'
                animate += 1
            elif lu:  # проверка влево-вверх
                firststart = False
                window.blit(walkUL[animate // 9], (x, y))
                lastank = 'UL'
                animate += 1
            else:  # проверка последнего изображения\\\\\\\\\
                if lastank == 'left':
                    window.blit(lefttank, (x, y))
                elif lastank == 'right':
                    window.blit(righttank, (x, y))
                elif lastank == 'up':
                    window.blit(uptank, (x, y))
                elif lastank == 'down':
                    window.blit(downtank, (x, y))
                elif lastank == 'DR':
                    window.blit(DR, (x, y))
                elif lastank == 'DL':
                    window.blit(DL, (x, y))
                elif lastank == 'UR':
                    window.blit(UR, (x, y))
                elif lastank == 'UL':
                    window.blit(UL, (x, y))
            # проверка последнего изображения\\\\\\\\\
            #
        pygame.display.update()  # обновление дисплея
    bullets = []
    bullets2 = []
    bulletsy = []
    bullets2y = []

    while menu:
        keys4 = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                menu = False
        clock.tick(60)
        window.blit(menu2, (0, 0))

        pressed = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        print(pos)
        if pos[0] > 382 and pos[0] < 630 and pos[1] > 343 and pos[1] < 409:
            window.blit(pt2, (382, 343))
        else:
            window.blit(p1, (382, 343))
        if pressed[0] and pos[0] > 382 and pos[0] < 630 and pos[1] > 343 and pos[1] < 409:
            raund1 = 0
            raund2 = 0
            menu = False
            tanks = True
            hp1 = 350
            hp2 = 350

        pygame.display.update()

    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = False
                pygame.quit()
        clock.tick(60)
        window.blit(gm, (0, 0))
        text = mario.render(str(shelsf1), True, green)
        window.blit(text, [225, 350])
        text = mario.render(str(shelsf2), True, yellow)
        window.blit(text, [735, 350])

        text = mario.render(str(damageshels2), True, yellow)
        window.blit(text, [870, 425])

        text = mario.render(str(damageshels1), True, green)
        window.blit(text, [360, 425])

        text = mario.render(str(damageshels1), True, green)
        window.blit(text, [408, 510])

        text = mario.render(str(damageshels1), True, yellow)
        window.blit(text, [915, 510])

        text = mario.render(str(damageshels2), True, yellow)
        window.blit(text, [870, 590])

        text = mario.render(str(damageshels1), True, green)
        window.blit(text, [360, 590])

        text = mario.render(str(damageshels2), True, yellow)
        window.blit(text, [640, 670])

        text = mario.render(str(damageshels1), True, green)
        window.blit(text, [130, 665])

        pressed2 = pygame.mouse.get_pressed()
        pos2 = pygame.mouse.get_pos()
        print(pos2)
        if pos2[0] > 750 and pos2[0] < 998 and pos2[1] > 725 and pos2[1] < 791:
            window.blit(home2, (750, 725))
        else:
            window.blit(home1, (750, 725))
        if pressed2[0] and pos2[0] > 750 and pos2[0] < 998 and pos2[1] > 725 and pos2[1] < 791:
            menu = True
            tanks = False
            gameover = False
        pygame.display.update()

    while load:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                load = False
                pygame.quit()
        clock.tick(5)
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*3
        pygame.display.update()
        time.sleep(0.1)
        window.blit(loading1, (0, 0))
        pygame.display.update()
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*3
        pygame.display.update()
        time.sleep(0.1)
        window.blit(loading2, (0, 0))
        pygame.display.update()
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*3
        pygame.display.update()
        time.sleep(0.1)
        window.blit(loading3, (0, 0))
        pygame.display.update()
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*3
        pygame.display.update()

        time.sleep(0.1)
        window.blit(frame1, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame2, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*2

        time.sleep(0.1)
        window.blit(frame3, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*4

        time.sleep(0.1)
        window.blit(frame4, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*2

        time.sleep(0.1)
        window.blit(frame5, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*2

        time.sleep(0.1)
        window.blit(frame6, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame7, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*2

        time.sleep(0.1)
        window.blit(frame8, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame9, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame10, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*3

        time.sleep(0.1)
        window.blit(frame11, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame12, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame13, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame14, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame15, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame16, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*2

        time.sleep(0.1)
        window.blit(frame17, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame18, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*4

        time.sleep(0.1)
        window.blit(frame19, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame20, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3

        time.sleep(0.1)
        window.blit(frame21, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*3

        time.sleep(0.1)
        window.blit(frame22, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*3

        time.sleep(0.1)
        window.blit(frame23, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*4

        time.sleep(0.1)
        window.blit(frame24, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*4

        time.sleep(0.1)
        window.blit(frame25, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*4

        time.sleep(0.1)
        window.blit(frame26, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*4

        time.sleep(0.1)
        window.blit(frame27, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*4

        time.sleep(0.1)
        window.blit(frame28, (780, 430))
        pygame.display.update()
        window.blit(loading4, (0, 0))
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*4

        time.sleep(0.1)
        window.blit(frame29, (780, 430))
        pygame.display.update()
        time.sleep(0.1)
        pygame.draw.rect(window, red2, (165, 356, otrezok, 44))
        otrezok += 3*4
        pygame.display.update()
        if otrezok >= 699:
            load = False
            tanks = True

    while tanks:
        b = (1)

        text = mario.render(str(raund1), True, green)
        window.blit(text, [450, -10])
        text = mario.render(str(raund2), True, yellow)
        window.blit(text, [550, -10])
        text = mario.render('HP '+str(hp1), True, green)
        window.blit(text, [0, -10])
        text = mario.render('HP '+str(hp2), True, yellow)
        window.blit(text, [860, -10])

        if raund1 > raund2:
            text = mario.render('>', True, green)
            window.blit(text, [495, -10])
        elif raund1 < raund2:
            text = mario.render('<', True, yellow)
            window.blit(text, [495, -10])
        else:
            text = mario.render('==', True, red)
            window.blit(text, [495, -10])

        keys7 = pygame.key.get_pressed()
        if keys7[pygame.K_z]:
            pygame.quit()
        e += 1
        # установка скорости цикла итого наша игра работает при ~60fps ближе к 65fps
        clock.tick(144)

        for bullet in bullets:
            if bullet.x < 1000 and bullet.x > 0:
                bullet.x += bullet.vel
                x4 = bullet.x
                n = True
                l = True
            else:
                n = False
                l = False
                bullets.pop(bullets.index(bullet))
        for bullet2 in bullets2:
            if bullet2.y < 800 and bullet2.y > -50:
                bullet2.y += bullet2.vel
                y4 = bullet2.x
                n = True
                l = True
            else:
                l = False
                n = False
                bullets2.pop(bullets2.index(bullet2))

        for bullety in bulletsy:

            if bullety.x2 < 1000 and bullety.x2 > 0:
                bullety.x2 += bullety.vel2
                x3 = bullety.x2
                n2 = True
                l2 = True
            else:
                l2 = False
                n2 = False
                bulletsy.clear()

        for bullet2y in bullets2y:
            if bullet2y.y2 < 770 and bullet2y.y2 > 50:
                y3 = bullet2y.y2
                bullet2y.y2 += bullet2y.vel2
                n2 = True
                l2 = True
            else:
                l2 = False
                n2 = False
                bullets2y.clear()

                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        if raund1 == 5 or raund2 == 5:
            if raund1 > raund2:
                text = mario2.render('GREEN WIN!'+str(raund+1), True, green)
                window.blit(text, [0, 300])
            elif raund1 < raund2:
                text = mario2.render('YELLOW WIN!'+str(raund+1), True, yellow)
                window.blit(text, [0, 300])
            elif raund1 == raund2:
                text = mario2.render('DRAW WIN!'+str(raund+1), True, red)
                window.blit(text, [15, 300])
            pygame.display.update()
            time.sleep(5)

            tanks = False
            menu = False
            gameover = True

        print('player 1', raund1)
        print('palyer 2', raund2)

        if hp1 == 0:
            hp1 = 350
            hp2 = 350
            raund2 += 1
            raund += 1
            x = 25
            y = 38
            x2 = 845
            y2 = 718

            text = mario2.render('ROUND '+str(raund+1), True, red)
            window.blit(text, [170, 300])
            pygame.display.update()
            time.sleep(5)
        if hp2 == 0:
            raund += 1
            hp1 = 350
            hp2 = 350
            raund1 += 1
            x = 25
            y = 38
            x2 = 845
            y2 = 718

            text = mario2.render('ROUND '+str(raund+1), True, red)
            window.blit(text, [170, 300])
            pygame.display.update()
            time.sleep(5)

        # обработка клавиш игрока 1\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        keys = pygame.key.get_pressed()
        keys2 = pygame.key.get_pressed()

        # обработка клавиш игрока 1\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        if keys[pygame.K_q]:

            if lastMove == "right":
                facing = 1
            else:
                facing = -1
            if len(bullets) < 1:
                bullets.append(snaryad(round(x + weight // 2),
                               round(y + height // 2), facing))

        if keys[pygame.K_q]:

            if lastMove == "up":
                facing2 = -1
            else:
                facing2 = 1
            if len(bullets2) < 1:
                bullets2.append(snaryad2(round(x + weight // 2),
                                round(y + height // 2), facing2))

        if keys2[pygame.K_KP0] or keys2[pygame.K_RCTRL]:

            if lastMove2 == "right":
                facingy = 1
            else:
                facingy = -1
            if len(bulletsy) < 1:
                bulletsy.append(snaryady(round(x2 + weight2 // 2),
                                round(y2 + height2 // 2), facingy))

        if keys2[pygame.K_KP0] or keys2[pygame.K_RCTRL]:

            if lastMove2 == "up":
                facing2y = -1
            else:
                facing2y = 1
            if len(bullets2y) < 1:
                bullets2y.append(
                    snaryad2y(round(x2 + weight2 // 2), round(y2 + height2 // 2), facing2y))

        # проверка на нажатие крестика\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        for event in pygame.event.get():  # сосдает массив с значениями кнопок
            if event.type == pygame.QUIT:  # проверка на крестик
                pygame.quit()
                tanks = False  # действие ifа
        # проверка на нажатие крестика\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        # обработка скорости и ускорения игрока 1\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        if speed <= 0.7 and speedtest:
            speed += 0.005
        if not speedtest and speed > 0:
            speed -= 0.05
        if speed2 <= 0.30:
            speed2 += 0.0005
        # обработка скорости и ускорения игрока 1\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        if speedy <= 0.7 and speedtesty:
            speedy += 0.005
        if not speedtesty and speedy > 0:
            speedy -= 0.05
        if speed2y <= 0.30:
            speed2y += 0.0005

        # обработка скольжения игрока 1 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        if not speedtest2 and speed2 >= 0.15:
            speed2 -= 0.1
        if speed > 0 and stopleft and x >= 0:
            x -= speed * 3
        elif speed > 0 and stopright and x <= 880:
            x += speed * 3
        elif speed > 0 and stopup and y >= 0:
            y -= speed * 3
        elif speed > 0 and stopdown and y < 680:
            y += speed * 3
        else:
            stopdown = False
            stopup = False
            stopright = False
            stopleft = False
        # обработка скольжения игрока 1 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        if not speedtest2y and speed2y >= 0.15:
            speed2y -= 0.1
        if speedy > 0 and stopleft2 and x2 >= 0:
            x2 -= speedy * 3
        elif speedy > 0 and stopright2 and x2 <= 880:
            x2 += speedy * 3
        elif speedy > 0 and stopup2 and y2 >= 0:
            y2 -= speedy * 3
        elif speedy > 0 and stopdown2 and y2 < 680:
            y2 += speedy * 3
        else:
            stopdown2 = False
            stopup2 = False
            stopright2 = False
            stopleft2 = False

        # управление игроком 1 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        if keys[pygame.K_a] and x >= 0 + 32 and (x2 + 50 < x or y2 - 42 > y or y2 + 42 < y or x2 - 50 > x) and (405 > y or 285 < x or x < 250) and (y < 0 or y > 265 or x > 490 or x < 453) and (y < 26 or y > 142 or x > 195 or x < 162):  # обработка клавиши влево
            x -= speed

            lastMove = "left"
            a = True
            stopdown = False
            stopup = False
            stopright = False
            stopleft = True
            left = True
            right = False
            up = False
            down = False
            ru = False
            rd = False
            ld = False
            lu = False
        elif keys[pygame.K_d] and x <= 920 and (x2 - 50 > x or y2 + 42 < y or y2 - 42 > y or x2 + 50 < x) and (405 > y or 230 < x or 180 > x) and (y > 680 or y < 650 or x < 740 or x > 971) and (y < 0 or y > 265 or x > 450 or x < 413) and (y < 26 or y > 142 or x > 69 or x < 36):  # обработка клавиши вправо
            x += speed

            d = True
            lastMove = "right"
            lastturn = 'right'
            stopdown = False
            stopup = False
            stopright = True
            stopleft = False
            left = False
            right = True
            up = False
            down = False
            ru = False
            rd = False
            ld = False
            lu = False
        elif keys[pygame.K_s] and y <= 680 and (y2 - 47 > y or y2 + 100 < y or x2 - 45 > x or x2 + 45 < x) and (y < 500 or y > 550 or x > 270) and (y < 355 or y > 800 or x > 300 or x < 230) and (y > 571 or y < 541 or x < 790 or x > 971):  # обработка клавиши вниз
            y += speed
            s = True
            pl = True
            lastMove = "down"
            lastturn = 'down'
            downturn = True
            stopdown = True
            stopup = False
            stopright = False
            stopleft = False
            left = False
            right = False
            up = False
            down = True
            ru = False
            rd = False
            ld = False
            lu = False
        elif keys[pygame.K_w] and y >= 32 and (y2 - 80 > y or y2 + 50 < y or x2 - 45 > x or x2 + 45 < x) and (y < 30 or y > 255 or x > 522 or x < 453) and (y > 680 or y < 650 or x < 790 or x > 971) and (y < 26 or y > 142 or x > 195 or x < 122):  # обработка клавиши вверх
            y -= speed
            w = True
            pl = True
            lastMove = "up"
            lastturn = 'up'
            upturn = True
            stopdown = False
            stopup = True
            stopright = False
            stopleft = False
            left = False
            right = False
            up = True
            down = False
            ru = False
            rd = False
            ld = False
            lu = False

        else:
            pl = False
            m = 0
            bull = False
            a = False
            d = False
            w = False
            s = False
            left = False
            right = False
            up = False
            down = False
            ru = False
            rd = False
            ld = False
            lu = False
            animate = 0

        if keys[pygame.K_s] and keys2[pygame.K_d] and x <= 1000 and y <= 720 and (y2 - 47 > y or y2 + 100 < y or x2 - 45 > x or x2 + 45 < x) and (x2 - 50 > x or y2 + 42 < y or y2 - 42 > y or x2 + 50 < x) and (x - 90 > x2 or y + 42 < y2 or y - 42 > y2 or x + 50 < x2) and (y > 571 or y < 541 or x < 770 or x > 971) and (y < 0 or y > 265 or x > 450 or x < 433) and (y < 500 or y > 550 or x > 270) and (y < 26 or y > 142 or x > 195 or x < 162):
            x += speed2
            y += speed2 * 9.5
            ru = False
            rd = True
            ld = False
            lu = False
            left = False
            right = False
            up = False
            down = False
        elif keys[pygame.K_s] and keys2[pygame.K_a] and x >= 0 and y <= 720 and (y2 - 47 > y or y2 + 100 < y or x2 - 45 > x or x2 + 45 < x) and (x2 + 50 < x or y2 - 42 > y or y2 + 42 < y or x2 - 50 > x) and (405 > y or 735 < y or 285 < x or x < 250) and (y > 571 or y < 541 or x < 770 or x > 971) and (y < 500 or y > 550 or x > 270) and (y < 26 or y > 142 or x > 195 or x < 162):
            x -= speed2
            y += speed2 * 9
            ru = False
            rd = False
            ld = True
            lu = False
            left = False
            right = False
            up = False
            down = False
        elif keys[pygame.K_w] and keys2[pygame.K_d] and x <= 1000 and y >= 32 and (y2 - 80 > y or y2 + 50 < y or x2 - 45 > x or x2 + 45 < x) and (x2 - 50 > x or y2 + 42 < y or y2 - 42 > y or x2 + 50 < x) and (y < 0 or y > 255 or x > 490 or x < 453) and (y > 680 or y < 650 or x < 790 or x > 971) and (y > 680 or y < 650 or x < 790 or x > 971) and (y < 0 or y > 265 or x > 450 or x < 433) and (y < 26 or y > 142 or x > 195 or x < 162):
            x += speed2
            y -= speed2 * 9
            ru = True
            rd = False
            ld = False
            lu = False
            left = False
            right = False
            up = False
            down = False
        elif keys[pygame.K_w] and keys2[pygame.K_a] and y >= 32 and x >= 30 and (x2 + 50 < x or y2 - 42 > y or y2 + 42 < y or x2 - 50 > x) and (y2 - 80 > y or y2 + 50 < y or x2 - 45 > x or x2 + 45 < x) and (y2 < 0 or y2 > 255 or x2 > 490 or x2 < 453) and (y > 680 or y < 650 or x < 790 or x > 971) and (y < 26 or y > 142 or x > 195 or x < 162):
            x -= speed2
            y -= speed2 * 9.5
            ru = False
            rd = False
            ld = False
            lu = True
            left = False
            right = False
            up = False
            down = False
        if left or right or down or up or ru or rd or ld or lu:
            speedtest = True
        else:
            speedtest = False
        if left or right or down or up or ru or rd or ld or lu:
            speedtest2 = True
        else:
            speedtest2 = False
        # управление игроком 1 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        keys3 = pygame.key.get_pressed()
        if keys3[pygame.K_q] and n2:
            bull2 = True
        # обработка клавиши влево
        if keys3[pygame.K_LEFT] and x2 >= 0 + 32 and (x + 50 < x2 or y - 42 > y2 or y + 42 < y2 or x - 50 > x2) and (405 > y2 or 285 < x2 or x2 < 250) and (y2 < 0 or y2 > 265 or x2 > 490 or x2 < 453) and (y2 < 26 or y2 > 142 or x2 > 195 or x2 < 162):
            x2 -= speedy

            lastMove2 = "left"
            a2 = True
            stopdown2 = False
            stopup2 = False
            stopright2 = False
            stopleft2 = True
            left2 = True
            right2 = False
            up2 = False
            down2 = False
            ru2 = False
            rd2 = False
            ld2 = False
            lu2 = False
        elif keys3[pygame.K_RIGHT] and x2 <= 920 and (x - 90 > x2 or y + 42 < y2 or y - 42 > y2 or x + 50 < x2) and (405 > y2 or 230 < x2 or 180 > x2) and (y2 > 680 or y2 < 650 or x2 < 740 or x2 > 971) and (y2 < 0 or y2 > 265 or x2 > 450 or x2 < 413) and (y2 < 26 or y2 > 142 or x2 > 69 or x2 < 36):  # обработка клавиши вправо
            d2 = True
            lastMove2 = "right"
            lastturn2 = 'right'
            stopdown2 = False
            stopup2 = False
            stopright2 = True
            stopleft2 = False
            left2 = False
            right2 = True
            up2 = False
            down2 = False
            ru2 = False
            rd2 = False
            ld2 = False
            lu2 = False
        elif keys3[pygame.K_DOWN] and y2 <= 680 and (y - 47 > y2 or y + 100 < y2 or x - 45 > x2 or x + 45 < x2) and (y2 < 500 or y2 > 550 or x2 > 270) and (y2 < 355 or y2 > 800 or x2 > 300 or x2 < 230) and (y2 > 571 or y2 < 541 or x2 < 790 or x2 > 971):  # обработка клавиши вниз

            y2 += speedy
            s2 = True
            pl2 = True
            lastMove2 = "down"
            lastturn2 = 'down'
            downturn2 = True
            stopdown2 = True
            stopup2 = False
            stopright2 = False
            stopleft2 = False
            left2 = False
            right2 = False
            up2 = False
            down2 = True
            ru2 = False
            rd2 = False
            ld2 = False
            lu2 = False
        elif keys3[pygame.K_UP] and y2 >= 32 and (y - 47 > y2 or y + 50 < y2 or x - 45 > x2 or x + 45 < x2) and (y2 < 30 or y2 > 255 or x2 > 522 or x2 < 453) and (y2 > 680 or y2 < 650 or x2 < 790 or x2 > 971) and (y2 < 26 or y2 > 142 or x2 > 195 or x2 < 122):
            y2 -= speedy
            w2 = True
            pl2 = True
            lastMove2 = "up"
            lastturn2 = 'up'
            upturn2 = True
            stopdown2 = False
            stopup2 = True
            stopright2 = False
            stopleft2 = False
            left2 = False
            right2 = False
            up2 = True
            down2 = False
            ru2 = False
            rd2 = False
            ld2 = False
            lu2 = False
        else:
            pl2 = False
            m2 = 0
            bull2 = False
            a2 = False
            d2 = False
            w2 = False
            s2 = False
            left2 = False
            right2 = False
            up2 = False
            down2 = False
            ru2 = False
            rd2 = False
            ld2 = False
            lu2 = False
            animate2 = 0
        if keys3[pygame.K_DOWN] and keys3[pygame.K_RIGHT] and x2 <= 1000 and y2 <= 720 and (y - 47 > y2 or y + 100 < y2 or x - 45 > x2 or x + 45 < x2) and (x - 90 > x2 or y + 42 < y2 or y - 42 > y2 or x + 50 < x2) and (y2 > 571 or y2 < 541 or x2 < 770 or x2 > 971) and (y2 < 0 or y2 > 265 or x2 > 450 or x2 < 433) and (y2 < 500 or y2 > 550 or x2 > 270) and (y2 < 26 or y2 > 142 or x2 > 195 or x2 < 162):
            x2 += speed2y
            y2 += speed2y * 9.25
            ru2 = False
            rd2 = True
            ld2 = False
            lu2 = False
            left2 = False
            right2 = False
            up2 = False
            down2 = False
        elif keys3[pygame.K_DOWN] and keys3[pygame.K_LEFT] and x2 >= 0 and y2 <= 720 and (x + 50 < x2 or y - 42 > y2 or y + 42 < y2 or x - 50 > x2) and (y - 47 > y2 or y + 100 < y2 or x - 45 > x2 or x + 45 < x2) and (405 > y2 or 735 < y2 or 285 < x2 or x2 < 250) and (y2 > 571 or y2 < 541 or x2 < 770 or x2 > 971) and (y2 < 500 or y2 > 550 or x2 > 270) and (y2 < 26 or y2 > 142 or x2 > 195 or x2 < 162):
            x2 -= speed2y
            y2 += speed2y * 9
            ru2 = False
            rd2 = False
            ld2 = True
            lu2 = False
            left2 = False
            right2 = False
            up2 = False
            down2 = False
        elif keys3[pygame.K_UP] and keys3[pygame.K_RIGHT] and x2 <= 1000 and y2 >= 32 and (y - 47 > y2 or y + 50 < y2 or x - 45 > x2 or x + 45 < x2) and (x - 90 > x2 or y + 42 < y2 or y - 42 > y2 or x + 50 < x2) and (y2 < 0 or y2 > 255 or x2 > 490 or x2 < 453) and (y2 > 680 or y2 < 650 or x2 < 790 or x2 > 971) and (y2 > 680 or y2 < 650 or x2 < 790 or x2 > 971) and (y2 < 0 or y2 > 265 or x2 > 450 or x2 < 433) and (y2 < 26 or y2 > 142 or x2 > 195 or x2 < 162):
            x2 += speed2y
            y2 -= speed2y * 9
            ru2 = True
            rd2 = False
            ld2 = False
            lu2 = False
            right2 = False
            up2 = False
            down2 = False
        elif keys3[pygame.K_UP] and keys3[pygame.K_LEFT] and y2 >= 32 and x2 >= 30 and (y - 47 > y2 or y + 50 < y2 or x - 45 > x2 or x + 45 < x2) and (x + 50 < x2 or y - 42 > y2 or y + 42 < y2 or x - 50 > x2) and (y2 < 0 or y2 > 255 or x2 > 490 or x2 < 453) and (y2 > 680 or y2 < 650 or x2 < 790 or x2 > 971) and (y2 < 26 or y2 > 142 or x2 > 195 or x2 < 162):
            x2 -= speed2y
            y2 -= speed2y * 9.25
            ru2 = False
            rd2 = False
            ld2 = False
            lu2 = True
            left2 = False
            right2 = False
            up2 = False
            down2 = False
        if left2 or right2 or down2 or up2 or ru2 or rd2 or ld2 or lu2:
            speedtesty = True
        else:
            speedtesty = False
        if left2 or right2 or down2 or up2 or ru2 or rd2 or ld2 or lu2:
            speedtest2y = True
        else:
            speedtest2y = False

        anim()  # вызов функции анимациии
        anim2()
