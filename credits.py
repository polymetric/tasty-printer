from escpos.printer import Serial
from time import sleep
import random
import sys

p = Serial(devfile='/dev/ttyS3')

def line(s):
    print(s)
#    p.textln(s)
    sleep(.5)

def lines(n):
    for i in range(n): line('          ')

def small_line():
    p.set_with_default()
    line('')

print('REMINDER: print some omelete tickets before printing the credits!')
#    p.set(double_height=True, double_width=True)
#    p.set(width=4, height=4)
#    p.set(align='center')

#sleep(1)
if sys.argv[1] == 'doug':
    lines(8)
    line('WRITTEN AND DIRECTED BY')
    line('DOUG LOWELL')
    lines(4)
    p.cut()

def card(title, name):
    p.set(

def nametitle_outward(title, name, width=48, char='.'):
    s=""
    s += title
    for i in range(width-len(name)-len(title)):
        s += char
    s += name.upper()
    line(s)

if sys.argv[1] == '21':
   # p.set(align='left')
    p.set_with_default(double_height=False, double_width=False)
#    p.set(custom_size
#   line('12345678901234567890123456789012345678901234567890')
#    line(' PRODUCTION SOUND MIXER  Terrel Brown')
#    line('           FOLEY ARTIST  Olga Valdejulli')
#    line('            FOLEY MIXER  Eli Rutan')
#    line('  Production Assistants  Yasmine Young')
#    line('                         Liz Perez')
    nametitle_outward('Written and Directed by', 'Doug Lowell')
    nametitle_outward('Executive Producers', 'Quinn Taylor')
    nametitle_outward('', 'Eli Rutan', char=' ')
    line('')
    nametitle_outward('The Cook', 'Leandre Holder')
    nametitle_outward('The Morning Manager', 'Henry L. Hill')
    nametitle_outward('The Waitress', 'Kati Foss')
    nametitle_outward('Bass Player', 'Thomas Milova')
    nametitle_outward('Trumpet Player', 'Austin Kelly')
    nametitle_outward('Accordian Player', 'Flora Flora Flora')
    nametitle_outward('Big Moe', 'Dwayne Reynolds')
    line('')
    nametitle_outward('First Assistant Director', 'Andrea Nique')
    nametitle_outward('Associate Producer', 'Oscar Urdaneta')
    nametitle_outward('Edited by', 'Billy Welch')
    nametitle_outward('Director of Photography', 'Quinn Taylor')
    nametitle_outward('Gaffer', 'Eli Rutan')
    nametitle_outward('Score by', 'Thomas Milovac')
    nametitle_outward('', 'Austin Kelly', char=' ')
    nametitle_outward('', 'Flora Flora Flora', char=' ')
    nametitle_outward('Score recorded by', 'Jason Woods')
    line('')
    nametitle_outward('Production Sound Mixer', 'Terrell Brown')
    nametitle_outward('Foley Artist', 'Olga Valdejulli')
    nametitle_outward('Foley Mixer', 'Eli Rutan')
    nametitle_outward('Production Assistants', 'Yasmine Young')
    nametitle_outward('', 'Liz Perez', char=' ')
    nametitle_outward('Actor Wrangler', 'Rita Lowell')
    nametitle_outward('Wardrobe Manager', 'Stephen Russo')
    line('')
    nametitle_outward('Big Moe\'s Logo By', 'Chill Artistry')



#for i in range(1,20):
#    line(i)


