
from pathlib import Path

from pygame import init
class ts():
    def __init__(self,cam):
        arquivo = open(cam,'r')
        a = True
        while a:
            file_line = arquivo.read(16)
            if not file_line:
                print("End Of File")
                a = False
            else:
                print(file_line)