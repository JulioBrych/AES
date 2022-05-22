
from tkinter import *
from tkinter.filedialog import *
import os
from pathlib import Path
from AES import *
from tkinter import messagebox
import re
caminho_do_arquivo_entrada = Path()
caminho_do_arquivo_saida = ""
tipoEntrada = ""

def criptografar():
    #65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80
    global caminho_do_arquivo_entrada
    global caminho_do_arquivo_saida
    global janela
    global tipoEntrada
    chaveTeste = []
    chaveValida = False
    pathSaida = str(caminho_do_arquivo_saida) + "/" + nome.get() + tipoEntrada
    contemLetras = bool(re.search('[a-zA-Z]', chave.get()))
    if(contemLetras != False or chave.get() == ""):
       messagebox.showerror("Erro!","Chave nao pode conter letras ou ser vazia")
    else:
        chaveTeste = chave.get().split(',')
        chaveTeste = list(map(int, chaveTeste))

        if(len(chaveTeste) == 16):
            chaveValida = True
            for i in chaveTeste:
                if(i>255):
                    chaveValida = False
                    break;
            if chaveValida == False:
                messagebox.showerror("Erro!","Valor do byte superior a 255")
                
        else:
            messagebox.showerror("Erro!","Numero de bytes da chave invalidos")

        if(chaveValida == True):
            cripto  = Aes(caminho_do_arquivo_entrada,pathSaida,chaveTeste)
            if cripto.startLeitura() == True:
                 messagebox.showinfo("Sucesso!","Criptografado com êxito")
            else:
                messagebox.showerror("Erro!","Selecione um arquivo")
    
def selecionarArquivoEntrada():
    global caminho_do_arquivo_entrada
    global janela
    global tipoEntrada
    caminho_do_arquivo_entrada = Path(askopenfilename(
        title='Selecionar Arquivo',
        initialdir='/',
        filetypes = (("Arquivos de texto", "*.txt"),("Arquivos Binário", "*.bin"))))
    aux = os.path.splitext(str(caminho_do_arquivo_entrada))
    tipoEntrada = aux[len(aux)-1]
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
janela.minsize(515,250)

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
