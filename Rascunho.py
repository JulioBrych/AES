'''
from operator import xor
from tkinter import *

class Application:
    def __init__(self, master=None):
        pass

root = Tk()
Application(root)
root.mainloop()
'''
listaIndice  = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

res = hex(ord('j'))
print(res)

a = 5
b = 3
print(a^b)

some_bytes = b"\xab"
hexadecimal_string = some_bytes.hex()
print(hexadecimal_string)