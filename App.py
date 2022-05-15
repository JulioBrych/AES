
from cProfile import label
from tkinter import *
from tkinter.filedialog import askopenfilename
caminho_do_arquivo = ""

def clickMe():
    texto2.configure(text=entrada.get())

def selecionarArquivo():
    global caminho_do_arquivo
    caminho_do_arquivo = askopenfilename(filetypes = (("Arquivos de texto", "*.txt")))

janela = Tk() #tk e o codigo que cria a janela vazia
janela.title("Criptador AES (Modo ECB)")

janela.minsize(500,500)
entrada = StringVar()
texto1 = Label(janela,text="Selecione o Arquivo")
texto1.grid(column=0,row=0,padx=10,pady=30)
texto2 = Label(janela)
texto2.grid(column=4,row=0)
nameEntered = Entry(janela, width = 15, textvariable = entrada)
nameEntered.grid(column = 2, row = 0,padx=30)
botao = Button(janela,text="OK",command=clickMe)
botao.grid(column=3,row=0)
a = Button(janela,text="oba")
a.place(x=200,y=100)
janela.mainloop() #codigo para manter a janela em execução
