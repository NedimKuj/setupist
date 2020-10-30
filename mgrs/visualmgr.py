"""
VisualManager 2.0.1
updated 07/07/20

"""

line = "----------------------------------------------------------"


def divider(times):
    for i in range(times):
        print(line)


def splash():
    print()
    divider(2)
    print(spaces("Setupist v0.0.2"))
    print(spaces("Release date: 30/10/2020"))
    print(spaces("(C) 2020 Nedim Kujraković"))
    print(spaces("nedkuj.com | contact@nedkuj.com"))
    divider(2)
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
