import tkinter as tk
from tkinter import messagebox, Entry, Label, Button
from PIL import Image, ImageTk
import random

#############################################################################
################## ---> FUNÇOES <-- #########################################

def is_primo(n):
    indice = miller_rabin_test(n=int(entrada.get()))
    return indice

def classificacao(indice):
    if indice == True:
        return 'ESTE NUMERO É PRIMO!'
    else:
        return 'ESTE NUMERO NÃO E PRIMO!'

def miller_rabin_test(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def acao():
    print('processando...')
    print('numero verificado [{}]'.format(entrada.get()))
    indice = is_primo(n=entrada.get())
    classific = classificacao(indice=indice)
    messagebox.showinfo('STATUS: CLASSIFICAÇÃO', classific)

#############################################################################
#############################################################################

janela = tk.Tk()
janela.title('CHECA PRIMO')
janela.geometry('300x50')

Imagem = Image.open('imagens/calc.png')
Imagem_redimensionada = Imagem.resize((55, 45))
image_tk = ImageTk.PhotoImage(Imagem_redimensionada)

logo = Label(master=janela, image=image_tk)
logo.grid(row=0, column=0, rowspan=2)

etiqueta_entrada1 = Label(master=janela, text='Digite um número: ')
etiqueta_entrada1.grid(row=0, column=1)

entrada = Entry(master=janela)
entrada.grid(row=0, column=2)

botao = Button(master=janela, text='Checar', command=acao)
botao.grid(row=1, column=2, rowspan=1)

janela.mainloop()
