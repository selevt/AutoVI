from utils import *

def add_cmds():
    dd = Cmd('dd')
    dd.add_loc(sc('<end><shift>+<home><delete>'))
    dd.add_loc(sc("<delete>"))

    D = Cmd('D', enum=False)
    D.add_loc(sc('<end><shift>+<home><delete>'))
    D.add_loc(sc("<delete>"))

    db = Cmd('db')
    db.add_loc(sc('<ctrl>+<shift>+<left>'))
    db.add_loc(sc("<delete>"))

    dw = Cmd('dw')
    dw.add_loc(sc('<ctrl>+<shift>+<right>'))
    dw.add_loc(sc("<delete>"))

    dh = Cmd('dh')
    dh.add_loc(sc('<backspace>'))

    dl = Cmd('dl')
    dl.add_loc(sc('<delete>'))

    d0 = Cmd('d0', enum=False)
    d0.add_loc(sc('<shift>+<home><delete>'))

    d_dollar = Cmd('d$', enum=False)
    d_dollar.add_loc(sc('<shift>+<end><delete>'))

    dgg = Cmd('dgg', enum=False)
    dgg.add_loc(sc('<shift>+<ctrl>+<home>'))
    dgg.add_loc(sc('<delete>'))

    dG = Cmd('dG', enum=False)
    dG.add_loc(sc('<shift>+<ctrl>+<end>'))
    dG.add_loc(sc('<delete>'))
