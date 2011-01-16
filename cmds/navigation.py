from utils import *

def add_cmds():
    # basic navigation (has to be after commands using these (dw before w))

    h = Cmd('h')
    h.add_loc(sc("<left>"))

    #for yay in range(200, 1, -1):
    #    numj = Cmd('%sj' % str(yay))
    #    for wee in range(yay):
    #        numj.add_loc(sc("<down>"))

    j = Cmd('j')
    j.add_loc(sc("<down>"))

    k = Cmd('k')
    k.add_loc(sc('<up>'))

    l = Cmd('l')
    l.add_loc(sc('<right>'))

    w = Cmd('w')
    w.add_loc(sc('<ctrl>+<right>'))

    b = Cmd('b')
    b.add_loc(sc('<ctrl>+<left>'))

    x = Cmd('x')
    x.add_loc(sc('<delete>'))

    zero = Cmd('0', enum=False)
    zero.add_loc(sc('<home>'))

    dollar = Cmd('$', enum=False)
    dollar.add_loc(sc('<end>'))

    gg = Cmd('gg', enum=False)
    gg.add_loc(sc('<ctrl>+<home>'))

    G = Cmd('G', enum=False)
    G.add_loc(sc('<ctrl>+<end>'))
