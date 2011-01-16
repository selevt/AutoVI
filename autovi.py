from utils import *
from cmds import basic, navigation, delete, change, binds 

config.MODS = ["<super>"]
config.FOLDER = "AutoVI"
config.ESCAPE = "<escape>"
config.ACTIVATE = "v"
config.NUM = 9


binds.add_cmds()
delete.add_cmds()
change.add_cmds()
navigation.add_cmds()
basic.add_cmds()

# Add commands into AutoKey
print "enumerating scripts..."
num_scripts()
print "sorting scripts"
sort_cmds()
print "producing scripts..."
produce_scripts()
print "installing scripts..."
install_scripts()
