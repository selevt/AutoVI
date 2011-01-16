import os, os.path
from autokey import nogui

class Config(object):
    SCRIPT_FILE = ""
    FOLDER = ""
    FOLDER_ID = ""
    MODS = []
    ESCAPE = ""
    ACTIVATE = ""
    NUM = 9

config = Config()
config.SCRIPT_FILE = "scripts.aks"
config.FOLDER_ID = "autovim"

#def set_config(mods):
#    MODS = mods


####### GEN methods ############

def gen_cmd(keys, loc):
    temp = """
try:
    store.__class__.active
except:
    setattr(store.__class__, 'active', False)
    %s

if store.__class__.active and not store.__class__.insert:
    keyboard.send_keys("<backspace>"*%s)
    %s
else:
    pass
"""
    code = ('\n'+(' '*4)).join(loc)

    return temp % (im(False), len(keys), code)

def sc(keys):
    return 'keyboard.send_keys("%s")' % keys

def im(b):
    return "setattr(store.__class__, 'insert', %s)" % str(b)

def nf(msg):
    return """system.exec_command('notify-send "AutoVI" "%s"')""" % msg

def imn(b):
    t = "on" if b else "off"
    msg = "insert mode %s" % t
    return nf(msg)

####### Autovi methods #####

class FakeApp(object):
    def init_global_hotkeys(self, foo):
        pass

##### new  #####

all_cmds = list()

class Cmd(object):
    def __init__(self, name, special=False, enum=True, modifier=True):
        self.loc = []
        self.name = name
        self.special = special
        self.enum = enum

        # default is abbr mode with name as trigger
        self.abbreviation(name)
        self.key = None
        self.modifier = modifier

        all_cmds.append(self)

    def __repr__(self):
        return self.name

    def add_loc(self, *code):
        for cod in code:
            self.loc.append(cod)

    def script(self):
        if self.special:
            return "\n%s" % '\n'.join(self.loc)
        else:
            return gen_cmd(self.name, self.loc)

    def abbreviation(self, abbr):
        self.mode = nogui.TriggerMode.ABBREVIATION
        self.abbr = abbr

    def hotkey(self, key):
        self.mode = nogui.TriggerMode.HOTKEY
        self.key = key


def num_scripts():
    for cmd in all_cmds[:]:
        if cmd.enum and 0 < len(cmd.name) <= 2:
            for i in range(config.NUM,1,-1):
                if len(cmd.name) == 1:
                    num_name = '%s%s' % (str(i), cmd.name)
                else:
                    num_name = '%s%s%s' % (cmd.name[0], str(i), cmd.name[1])
                num_cmd = Cmd(num_name)
                num_cmd.loc = cmd.loc * i
        

def sort_cmds():
    all_cmds.sort(key=lambda cmd: len(cmd.name))
    all_cmds.reverse()

def produce_scripts():
    if os.path.isfile(config.SCRIPT_FILE):
        os.remove(config.SCRIPT_FILE)
    with open(config.SCRIPT_FILE, 'wb') as f:
        for cmd in all_cmds:
            f.write("<%s>\n%s\n" % (cmd.name, cmd.script()))


def install_scripts():
    nogui.load_script_file(config.SCRIPT_FILE)
    vim = nogui.Folder(config.FOLDER)
    for cmd in all_cmds:
        scr = nogui.create_script(cmd.name)
        if cmd.mode == nogui.TriggerMode.ABBREVIATION:
            nogui.set_abbreviation(scr, cmd.abbr)
            scr.immediate = True
            scr.triggerInside = True
            scr.backspace = False
        elif cmd.mode == nogui.TriggerMode.HOTKEY:
            if cmd.modifier:
                nogui.set_hotkey(scr, config.MODS, cmd.key)
            else:
                nogui.set_hotkey(scr, [], cmd.key)

        vim.add_item(scr)

    

    cm = nogui.get_config_manager(FakeApp())
    cm.folders[config.FOLDER_ID] = vim
    cm.config_altered()
