from random import randint
from tkinter import *

class sayisalLoto:
    def __init__(self, menu):
        self.menu = menu
        menu.title("Sayısal Loto Oyununa Hoş Geldiniz!")
        menu.geometry("550x350")
        menu.configure(bg="yellow")
        self.baslik = Label(menu, text="Şanslı Numaraların!",bg = "yellow", fg = "black", font = "none 24 bold")
        self.baslik.config(font=("Times New Roman", 32))

        self.baslik.pack()

        self.numaralar = Entry(menu, text="Numaralarınız oluşturuyor...")
        self.numaralar.config(width=70)
        self.numaralar.pack()

        self.yeniden = Button(menu, text="Numaraları Oluştur!", command=self.numaraOlustur)
        self.yeniden.pack()

        self.yardim = Button(root,
                             text="Sayısal Loto Yardım",
                             command=self.YardimSayfasiAc)
        self.yardim.pack(pady=10)

        self.kapat = Button(menu, text="Kapat", command=menu.quit)
        self.kapat.pack()


    # Sayısal Loto kodlaması alıntıdır.
    def numaraOlustur(self):
        i = 0
        self.numaralar.delete(0, 'end')
        secilenler = [0, 0, 0, 0, 0, 0]
        while i < len(secilenler):
            secilen = randint(1, 49)
            if secilen not in secilenler:
                secilenler[i] = secilen
                i += 1
        sansliNumaralar = str((sorted(secilenler)))
        self.numaralar.insert(0, sansliNumaralar)

    def YardimSayfasiAc(self):

        Yardimsayfasi = Toplevel(root)
        Yardimsayfasi.title("YARDIM!")
        Yardimsayfasi.geometry("400x400")
        Yardimsayfasi.configure(bg= "turquoise")
        Label(Yardimsayfasi,
              text="Rakamları listelemek için Numaraları Oluştur butonuna basınız.\n Karşınıza birbirinden farklı ve rastgele numaralar gelecektir.", bg = "turquoise", fg = "black").grid(column = 0, row = 2, rowspan = 4, padx = 10, pady = 10)







root = Tk()
sayisalLotom = sayisalLoto(root)
sayisalLotom.numaraOlustur()
root.mainloop()