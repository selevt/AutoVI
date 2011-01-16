from utils import *

def add_cmds():
    # mode commands

    active = Cmd('active', special=True, enum=False)

    active.add_loc("try:")
    active.add_loc("    if store.__class__.active:")
    active.add_loc("        setattr(store.__class__, 'active', False)")
    active.add_loc("        %s" % nf("AutoVI deactivated"))
    active.add_loc("    else:")
    active.add_loc("        setattr(store.__class__, 'active', True)")
    active.add_loc("        %s" % nf("AutoVI activated"))
    active.add_loc("except:")
    active.add_loc("    setattr(store.__class__, 'active', False)")
    active.add_loc("    %s" % im(False))
    active.add_loc("    %s" % nf("AutoVI initialized - deactivated"))
    active.hotkey(config.ACTIVATE)


    escape = Cmd('escape', special=True, enum=False)

    escape.add_loc("try:")
    escape.add_loc("    if store.__class__.active and store.__class__.insert:")
    escape.add_loc("        %s" % im(False))
    escape.add_loc("        %s" % imn(False))
    escape.add_loc("    else:")
    escape.add_loc("        %s" % sc("<escape>"))
    escape.add_loc("except:")
    escape.add_loc("    setattr(store.__class__, 'active', False)")
    escape.add_loc("    %s" % im(False))
    escape.hotkey(config.ESCAPE)
    escape.modifier = False


    i = Cmd('i', enum=False)
    i.add_loc(im(True))
    i.add_loc(imn(True))

    a = Cmd('a', enum=False)
    a.add_loc(sc("<right>"))
    a.add_loc(im(True))
    a.add_loc(imn(True))

    o = Cmd('o', enum=False)
    o.add_loc(sc("<end><enter>"))
    o.add_loc(im(True))
    o.add_loc(imn(True))

    O = Cmd('O', enum=False)
    O.add_loc(sc("<up><end><enter>"))
    O.add_loc(im(True))
    O.add_loc(imn(True))

    J = Cmd('J')
    J.add_loc(sc("<end> <delete>"))
