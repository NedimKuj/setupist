import subprocess
import urllib.request
from alive_progress import alive_bar

# Local
from mgrs import dbmgr


def personalized_install(what, where):
    personalization = {}
    global_db = dbmgr.get_online_db()
    for entry in what:
        if entry in global_db.keys():
            personalization.update({entry: global_db[entry]})
    download_and_install(personalization, where)


def download(what, directory):
    print("Downloading sofware...")
    with alive_bar(total=len(what)) as bar:
        for i in what.keys():
            print(f"Downloading {i}... ", end=' ')
            # TODO must make sure Downloads exists! (make this check)
            # TODO also check if file already exists
            urllib.request.urlretrieve(what[i], directory + i + ".exe")
            bar()


def install(what, directory):
    with alive_bar(total=len(what)) as bar:
        for i in what.keys():
            print(f"Installing {i}...")
            if i == "opera":
                subprocess.run(directory + i + ".exe /silent /allusers=1 /launchopera=0 /setdefaultbrowser=0")
            else:
                subprocess.run(directory + i + ".exe /s")
            bar()


def download_and_install(what, where):
    download(what, where)
    print("Installing software...")
    install(what, where)
