from escpos.printer import Serial
from time import sleep
import random

p = Serial(devfile='/dev/ttyS3')

def line(s):
    print(s)
    p.text(f'{s}\n')
    sleep(0.1)

def small_line():
    p.set_with_default()
    line('')
    p.set(double_height=True, double_width=True)

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
        line('1 EGG CHEESE OMELETE')
        line('  The Tasty Way')
        small_line()
    orderno+=1

#p.set(font='b')
p.set(double_height=True, double_width=True)

order(3)



p.cut()
