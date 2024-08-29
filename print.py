from escpos.printer import Serial
from time import sleep
import random

p = Serial(devfile='/dev/ttyS3')

def line(s):
    p.set(double_height=True, double_width=True)
    print(s)
    p.text(f'{s}\n')
    sleep(0.1)

def small_line():
    p.set_with_default()
    line('')

orderno=1
t=1

def order(n):
    global t
    global orderno
    t+=random.randrange(1,10)
    h=8+t//60
    m=int(t%60)
    for i in range(10): line('')
    #line(f'10/20/2024  {h}:{m:02d} AM')
    #line( 'Server: Willow   OR#: 01')
    #line( '       -- FIRE --       ')
    line(f'10/20/2024  {h}:{m:02d} AM')
    line( 'Server: Willow   OR#: 01')
    small_line()
    line( '       -- FIRE --       ')
    small_line()
    for i in range(n):
#        line('1 EGG CHEESE OMELETE')
#        line('  The Tasty Way')
        p.set(align='center')
        line('WRITTEN AND DIRECTED BY')
        line('DOUG LOWELL')
        small_line()
        for j in range(4):
            line('')
    orderno+=1
    p.cut()


#while True:
#order(random.randrange(1,8))
order(1)
#    sleep(random.randrange(0, 3))

