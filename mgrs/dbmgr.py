import csv

db = {"chrome": "http://dl.google.com/chrome/install/375.126/chrome_installer.exe",
      "dropbox": "https://www.dropbox.com/download?plat=win",
      "firefox-32bit": "https://download.mozilla.org/?product=firefox-latest-ssl&os=win&lang=en-US",
      "firefox-64bit": "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US",
      "gdrive": "https://dl.google.com/drive/installbackupandsync.exe",
      "jetbrains-toolbox": "https://download-cf.jetbrains.com/toolbox/jetbrains-toolbox-1.17.7139.exe",
      "steam": "https://steamcdn-a.akamaihd.net/client/installer/SteamSetup.exe",
      "teamviewer15": "https://dl.teamviewer.com/download/version_15x/TeamViewer_Setup.exe",
      "thunderbird-32bit": "https://download.mozilla.org/?product=thunderbird-latest&os=win&lang=en-US",
      "thunderbird-64bit": "https://download.mozilla.org/?product=thunderbird-latest&os=win64&lang=en-US",
      "vlc-32bit": "http://get.videolan.org/vlc/last/win32/vlc-3.0.11-win32.exe",
      "vlc-64bit": "http://get.videolan.org/vlc/last/win64/vlc-3.0.11-win64.exe",
      "7zip-32bit": "https://www.7-zip.org/a/7z1900.exe",
      "7zip-64bit": "https://www.7-zip.org/a/7z1900-x64.exe"}

local_prefs = []


def get_local_prefs(path):
    with open(path + "\\download.txt", newline='') as csvfile:
        local_prefs.clear()
        reader = csv.reader(csvfile, delimiter='\n', quotechar='"')
        for line in reader:
            try:
                local_prefs.append(line[0])
            except Exception:
                # Ignore blank spaces
                pass
        # print(local_prefs)
        csvfile.close()
    return local_prefs
