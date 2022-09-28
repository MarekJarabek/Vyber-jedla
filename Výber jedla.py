import tkinter #plátno
canvas = tkinter.Canvas(width=500,height=500)#dĺžka a šírka plátna
canvas.pack()

canvas.create_text(250, 70, text='Výber jedla', font='Arial 30') #nadpis na plátne
canvas.create_rectangle(10,100,110,200, fill='green') #zelený štvorec
canvas.create_rectangle(130,100,230,200, fill='red') #červený štvorec
canvas.create_rectangle(250,100,350,200, fill='blue') #modrý štvorec
canvas.create_rectangle(370,100,470,200, fill='orange') #oranžový štvorec

def stvorce(event): #definícia ktorá zaznamenáva pohyb kurzora
      kod() #premenná kód
      subor = open('vyber_jedla.txt', 'a') #otvorenie súboru vyber jedla txt
      if 100<event.y<200 and 10<event.x<110: #podmienka kde musím stlačiť aby sa mi napísalo g
            subor.write(' g\n') #zapíše to g do súboru
      elif 100<event.y<200 and 130<event.x<230: #podmienka kde musím stlačiť aby sa mi napísalo r
            subor.write(' r\n') #zapíše to r do súboru
      elif 100<event.y<200 and 250<event.x<350: #podmienka kde musím stlačiť aby sa mi napísalo b
            subor.write(' b\n') #zapíše to b do súboru
      elif 100<event.y<200 and 370>event.x<470: #podmienka kde musím stlačiť aby sa mi napísalo o
            subor.write(' o\n') #zapíše to o do súboru
      subor.close() #zatvorí súbor

def kod(): #definícia kód
      kodik = entry1.get() #entry zaznamenané pod názvom kodik
      subor = open('vyber_jedla.txt', 'a') #otvorí súbor vyber jedla txt
      subor.write(kodik) #zapíše to súradnicu z entry do textoveho suboru
      subor.close() #zatvori to subor
entry1 = tkinter.Entry() #vytvori to entry
entry1.pack()

canvas.bind('<Button-1>', stvorce) #pri stlaceni laveho tlacidla mysky sa spusti funkcia stvorce
