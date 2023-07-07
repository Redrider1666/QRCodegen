###################################
######## Coded by Redrider ########
###################################

import tkinter as tk
from PIL import ImageTk, Image, ImageFilter
import qrcode


print("RRRRRR   EEEEEE  DDDDD    RRRRRR   IIIII  DDDDD    EEEEEE  RRRRRR   ")
print("RR   RR  EE      DD   DD  RR   RR   III   DD   DD  EE      RR   RR  ")
print("RRRRRR   EEEE    DD   DD  RRRRRR    III   DD    DD EEEE    RRRRRR ")  
print("RR RR    EE      DD   DD  RR RR     III   DD   DD  EE      RR RR")    
print("RR   RR  EEEEEE  DDDDDD   RR   RR  IIIII  DDDDDD   EEEEEE  RR   RR")  


def gerar_qrcode():
    texto = texto_entry.get()
    imagem_qrcode = qrcode.make(texto)
    imagem_qrcode.save('qrcodes/qrcode.png')

    imagem = Image.open('qrcodes/qrcode.png')
    largura, altura = imagem.size

    nova_largura = largura // 2
    nova_altura = altura // 2

    imagem = imagem.resize((nova_largura, nova_altura), resample=Image.LANCZOS)

    x = (largura_janela - nova_largura) // 2
    y = (altura_janela - nova_altura) // 2 + 50  

    imagem_qrcode = ImageTk.PhotoImage(imagem)
    qr_code_label.configure(image=imagem_qrcode)
    qr_code_label.image = imagem_qrcode 
    qr_code_label.place(x=x, y=y)

    status_label.configure(text='QR code successfully generated!', fg='#228B22') 

def on_enter(event):
    gerar_button.configure(bg='#196619')

def on_leave(event):
    gerar_button.configure(bg='#228B22')

janela = tk.Tk()
janela.title('QR Code Generator')

largura_janela = 800
altura_janela = 600
janela.geometry(f"{largura_janela}x{altura_janela}")

janela.configure(bg='#f0f0f0')
janela.iconbitmap('images/icon.ico')

fonte = ('Arial', 14)

quadro = tk.Frame(janela, bg='#f0f0f0')
quadro.pack(pady=100)

texto_label = tk.Label(quadro, text='Link:', font=fonte, bg='#f0f0f0')
texto_label.grid(row=0, column=0, padx=10, pady=10)

texto_entry = tk.Entry(quadro, width=30, font=fonte)
texto_entry.grid(row=0, column=1, padx=10, pady=10)

gerar_button = tk.Button(quadro, text='Generate', command=gerar_qrcode, font=fonte, bg='#228B22', fg='white')
gerar_button.grid(row=1, columnspan=2, padx=10, pady=10)

gerar_button.bind("<Enter>", on_enter)
gerar_button.bind("<Leave>", on_leave)

status_label = tk.Label(quadro, text='', font=fonte, bg='#f0f0f0')
status_label.grid(row=2, columnspan=2, padx=10, pady=10)

qr_code_label = tk.Label(janela)
qr_code_label.pack()

janela.mainloop()
