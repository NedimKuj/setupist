import os

# Local imports
from mgrs import visualmgr
from mgrs import dbmgr
from src import core

# TODO ask to run as admin, if not already

os.chdir(os.path.dirname(os.path.realpath(__file__)))

software = dbmgr.db

visualmgr.splash()

typechooser = str(input("Personalized or global? (p/g) "))
if typechooser.lower() == "p":
    core.personalized_install(dbmgr.get_local_prefs(os.getcwd()), os.getcwd() + "\\Downloads\\")
elif typechooser.lower() == "g":
    print("In future versions, Main Menu is to be implemented here")
else:
    # TODO handle unknown input
    print("Input not recognized...")

input("All done! Press any key to exit...")
