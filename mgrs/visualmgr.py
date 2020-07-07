"""
VisualManager 2.0
updated 07/07/20

"""

line = "----------------------------------------------------------"


def divider(times):
    for i in range(times):
        print(line)


def splash():
    print()
    divider(2)
    print(spaces("Setupist DEV"))
    print(spaces("(C) 2020 Nedim Kujraković"))
    print(spaces("nedkuj.com | nk@nedkuj.com"))
    divider(2)
    print(f"Application is starting...")
    print()


def goodbye():
    divider(2)


def spaces(middleString):
    resp = ""
    spPerSide = len(line) - len(middleString)
    for i in range(spPerSide):
        if i == int((len(line) - len(middleString)) / 2):
            resp = resp + middleString
        resp = resp + " "
    return resp
