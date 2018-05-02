#!/usr/bin/python

intab = "abcdefghijklmnopqrstuvwxyz"
outab = "amvekuidchtnsbrlqpoygwjzfx"
trantab = str.maketrans(intab, outab)

with open('wubi_qwerty.txt', 'r') as r:
    str = r.read()
    with open('wubi_dvorak.txt', 'w') as w:
        w.write(str.translate(trantab))