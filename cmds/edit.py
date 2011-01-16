from utils import *

def add_cmds():
    pc = Cmd(')')
    pc.add_loc(sc('qyq'))
    pc.add_loc(sc('<ctrl>+<a>'))
    pc.add_loc(sc('<ctrl>+<x>'))
    pc.add_loc('system.exec_command("sleep 0.1")')
    pc.add_loc('clip = clipboard.get_clipboard()')
    pc.add_loc('clipboard.fill_clipboard(clip)')
    pc.add_loc('system.exec_command("sleep 0.1")')
    pc.add_loc(sc('<ctrl>+<v>'))
