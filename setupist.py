import os

# Local imports
from mgrs import visualmgr
from mgrs import dbmgr
from src import core

# TODO ask to run as admin, if not already
# TODO consider the option of silent uninstallation as well

os.chdir(os.path.dirname(os.path.realpath(__file__)))

software = dbmgr.get_online_db()

visualmgr.splash()

print("Choose instalation type. Enter p for personalized, if you have added the packages in the download.txt file, "
      "or g if you want to display the main menu.")
typechooser = str(input("Personalized or global? (p/g) "))
print()
if typechooser.lower() == "p":
    # todo check if download.tyt exists, if not, ask the user to enter the correct filename (or to name it download.txt)
    core.personalized_install(dbmgr.get_local_prefs(os.getcwd()), os.getcwd() + "\\Downloads\\")
elif typechooser.lower() == "g":
    print("Right now, this is all empty space. In future versions, Main Menu is to be implemented here.")
else:
    # TODO handle unknown input
    print("Input not recognized...")

print()
input("All done! Press any key to exit...")
