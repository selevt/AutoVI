from utils import *

def add_cmds():
    u = Cmd('u')
    u.add_loc(sc('<ctrl>+z'))

    slash = Cmd('/', enum=False)
    slash.add_loc(sc('<ctrl>+f'))
    slash.add_loc(im(True))
    
    save = Cmd(':w', enum=False)
    save.add_loc(sc('<ctrl>+s'))
    
    quit = Cmd(':q')
    quit.add_loc(sc('<ctrl>+q'))
    
    #savequit = Cmd(':wq')
    #savequit.add_loc(sc('<ctrl>+s'))
    #savequit.add_loc(sc('<alt>+<f4>'))
