from tkinter import*

def kullanıcı_bilgisi():

    yas = int(input('Yaşınızı Giriniz:'))
    cınsıyet = input('Cinsiyetinizi Giriniz: ')
    kilo = int(input('Kilonuzu KG cinsinden giriniz: '))
    boy = int(input('Boyunuzu cm cinsinden giriniz: '))


    if cınsıyet == 'erkek':
        c1 = 66
        hm = 6.2 * boy
        wm = 12.7 * kilo
        am = 6.76 * yas
    elif cınsıyet == 'kadın':
        c1 = 655.1
        hm = 4.35 * boy
        wm = 4.7 * kilo
        am = 4.7 * yas
    else:
        print("yanlış cinsiyet girdiniz")


    sonuc = c1 + hm + wm - am

    return(int(sonuc))

def aktıvıte_hesabı(sonuc):
    aktivite_seviyesi = input('Aktivite seviyenizi giriniz (sedanter,azhareketli, orta derece hareketli, çok hareketli, ya da aşırı hareketli): ')

    if aktivite_seviyesi == 'sedanter':
        aktivite_seviyesi = 1.2 * sonuc
    elif aktivite_seviyesi == 'azhareketli':
        aktivite_seviyesi = 1.375 * sonuc
    elif aktivite_seviyesi == 'orta derece hareketli':
        aktivite_seviyesi = 1.55 * sonuc
    elif aktivite_seviyesi == 'çok hareketli':
        aktivite_seviyesi = 1.725 * sonuc
    elif aktivite_seviyesi == 'aşırı hareketli':
        aktivite_seviyesi = 1.9 * sonuc

    return(int(aktivite_seviyesi))

def hedef_belirleme(aktivite_seviyesi):
    hedef = input('Hedefiniz nedir ?, zayıflamak, kiloyu korumak, kilo almak: ')

    if hedef == 'zayıflamak':
        kalori = aktivite_seviyesi - 500
    elif hedef == 'kiloyu korumak':
        kalori = aktivite_seviyesi
    elif hedef == 'kilo almak':
        kilo_almak = int(input('Haftada 1 veya 2 kilo mu almak istiyorsun? 1 Veya 2 giriniz'))
        if kilo_almak == 1:
            kalori = aktivite_seviyesi + 500
        elif kilo_almak == 2:
            kalori = aktivite_seviyesi + 1000


    print(' ', hedef,'için, Günlük Alman gereken kalori miktarı :', int(kalori), '!')


    ############




root = Tk()
root.title("KALORİ İHTİYACI HESAPLAMA")
root.bind("<Return>", lambda x: calculate_button())
app_title = Label(
    root, text="KALORİ İHTİYACI HESAPLAMA", pady=10, font=("Helvetica 12 bold")
)
app_title.grid(row=0, column=0, columnspan=2)
cınsıyet = IntVar()


input_frame = LabelFrame(root, text="bilgiler", padx=20, pady=10)
input_frame.grid(row=1, column=0, padx=10)


yas = Label(input_frame, text="Yaş")
yas.grid(row=0, column=0, columnspan=2)
yas_input = Entry(input_frame, width=10)
yas_input.grid(row=1, column=0, columnspan=2)

kilo = Label(input_frame, text="Kilo")
kilo.grid(row=2, column=0, pady=[10, 0], columnspan=2)
kilo_input = Entry(input_frame, width=10)
kilo_input.grid(row=3, column=0, columnspan=2)

boy = Label(input_frame, text="Boy")
boy.grid(row=4, column=0, pady=[10, 0], columnspan=2)
boy_input = Entry(input_frame, width=10)
boy_input.grid(row=5, column=0, columnspan=2)




r1 = Radiobutton(input_frame, text="Erkek", variable=cınsıyet, value=0)
r1.grid(row=10, column=0, pady=[10, 0])

r2 = Radiobutton(input_frame, text="Kadın", variable=cınsıyet, value=1)
r2.grid(row=10, column=1, pady=[10, 0])


output_frame = LabelFrame(root, text="GÜN İÇİN HAREKETLİLİK SEVİYENİZ")
output_frame.grid(row=1, column=1, ipady=21, padx=10)

bmr_label = Radiobutton(output_frame, text="Sedanter",value=2)
bmr_label.grid(row=1, column=0, padx=50, pady=[50, 250])
bmr_output = Label(output_frame, font=("Helvetica 15 bold"))
bmr_output.grid(row=2, column=0)

bmr_label = Radiobutton(output_frame, text="Az hareketli",value=3)
bmr_label.grid(row=1, column=0, padx=50, pady=[50,200])
bmr_output = Label(output_frame, font=("Helvetica 15 bold"))
bmr_output.grid(row=2, column=0)
bmr_label = Radiobutton(output_frame, text="Orta Derece hareketli",value=4)
bmr_label.grid(row=1, column=0, padx=50, pady=[50,150])
bmr_output = Label(output_frame, font=("Helvetica 15 bold"))
bmr_output.grid(row=2, column=0)
bmr_label = Radiobutton(output_frame, text="Çok hareketli",value=5)
bmr_label.grid(row=1, column=0, padx=50, pady=[50,100])
bmr_output = Label(output_frame, font=("Helvetica 15 bold"))
bmr_output.grid(row=2, column=0)
bmr_label = Radiobutton(output_frame, text="Aşırı Hareketli",value=6)
bmr_label.grid(row=1, column=0, padx=50, pady=[50,50])
bmr_output = Label(output_frame, font=("Helvetica 15 bold"))
bmr_output.grid(row=2, column=0)

output_frame = LabelFrame(root, text="Hedefiniz Nedir?")
output_frame.grid(row=1, column=2, ipady=21, padx=10)



hedef_label1 = Radiobutton(output_frame, text="Zayıflamak",variable=5,value=10)
hedef_label1.grid(row=1, column=0, padx=50, pady=[50, 250])
hedef_output = Label(output_frame, font=("Helvetica 15 bold"))
hedef_output.grid(row=2, column=0)

hedef_label2 = Radiobutton(output_frame, text="Kilo Almak",variable=5,value=11)
hedef_label2.grid(row=1, column=0, padx=50, pady=[50,200])
hedef_output = Label(output_frame, font=("Helvetica 15 bold"))
hedef_output.grid(row=2, column=0)
hedef_label = Radiobutton(output_frame, text="Hızlı Kilo almak",variable=5,value=12)
hedef_label.grid(row=1, column=0, padx=50, pady=[50,150])
hedef_output = Label(output_frame, font=("Helvetica 15 bold"))
hedef_output.grid(row=2, column=0)
hedef_label = Radiobutton(output_frame, text="Kiloyu Korumak",variable=5,value=13)
hedef_label.grid(row=1, column=0, padx=50, pady=[50,100])






calculate_button = Button(root, width=15, text="Hesapla",command=print())
calculate_button.grid(row=2, column=0, pady=[20, 0], padx=20)





clear_button = Button(root, width=15, text="Temizle",)
clear_button.grid(row=2, column=1, pady=[20, 0])


exit_button = Button(root, width=20, text="ÇIKIŞ", command=root.quit)
exit_button.grid(row=3, column=0, pady=[20, 10], columnspan=2)

root.mainloop()












