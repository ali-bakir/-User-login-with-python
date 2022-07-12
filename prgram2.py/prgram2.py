from binascii import a2b_base64
import tkinter as tk

arayüz = tk.Tk()
arayüz.title("Şifre")
arayüz.geometry("300x200")
a1 = "alibakr"
a2 = "12345"

kullanıcı = tk.Label(text="KULLANICI ADI:")
kullanıcı.place(x=10,y=10)

y = tk.StringVar()
kullanıcı_girisi = tk.Entry(textvariable=y)
kullanıcı_girisi.place(x=110,y=10)

kullanıcı = tk.Label(text="ŞİFRE GİRİŞİ:")
kullanıcı.place(x=26,y=35)

x = tk.StringVar()
kullanıcı_girisi = tk.Entry(textvariable=x)
kullanıcı_girisi.place(x=110,y=35)

dogru_yanlis = tk.Label(font="Verdana 30 bold")
dogru_yanlis.place(x=100,y=95)

def giris_komut():
    kullan = y.get()
    sif = x.get()
    print(kullan,"\n",sif)
    if kullan == a1 and sif == a2:
        print("doğru")
        dogru_yanlis.config(text="DOĞRU",fg="green")
    else:
        print("yanlış")
        dogru_yanlis.config(text="YANLIŞ",fg="red")

giris = tk.Button(text="GİRİŞ",command=giris_komut)
giris.place(x=213,y=55)

arayüz.mainloop()