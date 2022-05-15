
from cProfile import label
from tkinter import *
from tkinter.filedialog import *

from bitarray import test
from matplotlib.pyplot import text
caminho_do_arquivo_entrada = ""
caminho_do_arquivo_saida = ""

def criptografar():
    ...

def selecionarArquivoEntrada():
    global caminho_do_arquivo_entrada
    global janela
    caminho_do_arquivo_entrada = askopenfilename(
        title='Selecionar Arquivo',
        initialdir='/',
        filetypes = (("Arquivos de texto", "*.txt"),("Arquivos Binário", "*.bin")))
    box1.config(text=caminho_do_arquivo_entrada)

def selecionarArquivoSaida():
    global caminho_do_arquivo_saida
    global janela
    caminho_do_arquivo_saida = ""
    caminho_do_arquivo_saida = askdirectory(
        title='Selecionar Pasta',
        initialdir='/')
    box2.config(text=caminho_do_arquivo_saida)
    
janela = Tk()
janela.title("Criptador AES (Modo ECB)")
janela.minsize(600,500)

label1 = Label(janela,text="Arquivo:")
label1.place(x=20,y=20)
label2 = Label(janela,text="Chave:")
label2.place(x=20,y=50)
label3 = Label(janela,text="Local do Arquivo Criptografado:") 
label3.place(x=20,y=80)
label4 = Label(janela,text="Nome do Arquivo Criptografado:") 
label4.place(x=20,y=140)
chave = StringVar()
nome = StringVar()
nomeEntrada= Entry(janela, width = 70, textvariable = nome)
nomeEntrada.place(x=20,y=170)
chaveEntrada= Entry(janela, width = 60, textvariable = chave)
chaveEntrada.place(x=80,y=50)
box1= Label(janela,text=caminho_do_arquivo_entrada, width = 60)
box1.place(x=80,y=20)
box2= Label(janela,text=caminho_do_arquivo_saida, width = 70)
box2.place(x=20,y=110)
botao1 = Button(janela,text="Buscar",command=selecionarArquivoEntrada)
botao1.place(x=450,y=15)
botao1 = Button(janela,text="Buscar",command=selecionarArquivoSaida)
botao1.place(x=450,y=105)
botao1 = Button(janela,text="Criptografar",command=criptografar)
botao1.place(x=50,y=200)
janela.mainloop()
