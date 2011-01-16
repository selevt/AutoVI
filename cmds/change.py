from utils import *

def add_cmds():
    for cm in [c for c in all_cmds if c.name.startswith('d') or c.name == 'D']:
        change_name = cm.name.replace('d', 'c')
        change_name = change_name.replace('D', 'C')
        change_cmd = Cmd(change_name)
        change_cmd.loc = cm.loc[:]
        change_cmd.add_loc(im(True))
        change_cmd.add_loc(imn(True))
        if change_name == 'cc' or change_name =='C':
            change_cmd.add_loc(sc("<enter><up>"))
