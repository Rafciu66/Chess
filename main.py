from tkinter import *
#----------------------------#
root = Tk()
root.geometry("800x800")
root.title("Szachy")
global Obrazki

def ramki_przyciski():
    global Ramki
    global Przyciski
    global tura
    Ramki = {}
    Przyciski = {}
    tura="b"
Obrazki = {}

Obrazki["wieza_czarna_obr"]  =  PhotoImage(file='wieza_czarna.png')
Obrazki["wieza_biala_obr"]   =  PhotoImage(file='wieza_biala.png')
Obrazki["pion_czarny_obr"]   =  PhotoImage(file='pion_czarny.png')
Obrazki["pion_bialy_obr"]    =  PhotoImage(file='pion_bialy.png')
Obrazki["kon_bialy_obr"]     =  PhotoImage(file='kon_bialy.png')
Obrazki["kon_czarny_obr"]    =  PhotoImage(file='kon_czarny.png')
Obrazki["goniec_bialy_obr"]  =  PhotoImage(file='goniec_bialy.png')
Obrazki["goniec_czarny_obr"] =  PhotoImage(file='goniec_czarny.png')
Obrazki["krol_czarny_obr"]   =  PhotoImage(file='krol_czarny.png')
Obrazki["krol_bialy_obr"]    =  PhotoImage(file='krol_bialy.png')
Obrazki["hetman_czarny_obr"] =  PhotoImage(file='hetman_czarny.png')
Obrazki["hetman_bialy_obr"]  =  PhotoImage(file='hetman_bialy.png')
def show_warning(figura):
    kolor=figura[0]
    if kolor=="c":
        info="Czarne Wygrały!!!"
    if kolor=="b":
        info="Biale wygrały!!!"
    warning_window = Toplevel(root)
    warning_window.geometry("300x200")
    warning_window.title("Zwyciestwo!")
    x=info
    warning_label = Label(warning_window, text=x, fg="red")
    warning_label.pack(pady=20)
    def on_reset():
        warning_window.destroy()
        ramki_przyciski()
        emptyMap(root,Przyciski,Ramki)
        pozycjaStartowa(Przyciski,Obrazki)
    reset_button = Button(warning_window, text="Zacznij od nowa", command=on_reset)
    reset_button.pack(pady=20)
    
    # Disable the window close button
    warning_window.protocol("WM_DELETE_WINDOW", lambda: None)
    
    # Lock the main root window until the pop-up is closed
    warning_window.transient(root) #zawsze na wieszchu, minimalizuje sie z root 
    warning_window.grab_set()
    root.wait_window(warning_window)
def whatIsToBeat(tile, color):
    return_list = []
    if tile>9:
        if color == "c":
            if (tile<20):
                left_cordinates="0"+str(tile-11)
                righ_cordinates="0"+str(tile-9)
            else:
                left_cordinates=tile-11
                righ_cordinates=tile-9
            if tile%10>0:
                if (Przyciski[f"przycisk{left_cordinates}"].cget('text'))!="":
                    if (Przyciski[f"przycisk{left_cordinates}"].cget('text'))[0]=="b":
                        return_list.append(int(left_cordinates))
                        print(left_cordinates)
            if tile%10<7:
                if (Przyciski[f"przycisk{righ_cordinates}"].cget('text'))!="":
                    x=Przyciski[f"przycisk{righ_cordinates}"].cget('text')
                    if x[0]=="b":
                        return_list.append(int(righ_cordinates))
                        print(righ_cordinates)
        if color == "b":
            left_cordinates=tile+11
            righ_cordinates=tile+9
            if tile%10<7:

                if (Przyciski[f"przycisk{left_cordinates}"].cget('text'))!="":             
                        if (Przyciski[f"przycisk{left_cordinates}"].cget('text'))[0]=="c":
                            return_list.append(int(left_cordinates))
                            print(left_cordinates)
            if tile%10>0:

                if (Przyciski[f"przycisk{righ_cordinates}"].cget('text'))!="":
                        x=Przyciski[f"przycisk{righ_cordinates}"].cget('text')
                        if x[0]=="c":
                            return_list.append(int(righ_cordinates))
                            print(righ_cordinates)
    return return_list
#----------------------------#
def isAnythingAhead(tile, color):
    if tile>9:
        if color == "c":
            if (tile-10>10):
                if Przyciski[f"przycisk{tile-10}"].cget('text')=="":
                    return 1
            else:
                if Przyciski[f"przycisk{"0"+str(tile-10)}"].cget('text')=="":
                    return 1
            return 0
        if color == "b":
            if Przyciski[f"przycisk{tile+10}"].cget('text')=="":
                return 1
            return 0
#----------------------------#  
def ruch(figura, tile):   #zwraca mozliwe ruchy figury x na polu y
#    print("figura to: ", figura, "tile to:", tile)
    tile = int(tile)
    figura = str(figura)
    klasa = figura[1]
    strona = figura[0]
    mozliwy_ruch = []
    wspx=tile%10 # 43: wspx = 3, wspy = 4 
    wspy=tile//10 #
    if (klasa=="s"):
        if (strona=="c"):
            for y in whatIsToBeat(tile, strona):
                print(y)
                for v in mozliwy_ruch:
                    print(v)
                mozliwy_ruch.append(y)
                for v in mozliwy_ruch:
                    print(v)
            if (isAnythingAhead(tile, strona)):
                mozliwy_ruch.append(tile-10)#, tile-20
                mozliwy_ruch.sort()
                if (isAnythingAhead(tile-10, strona)):
                    mozliwy_ruch.append(tile-20)#, tile-20
                    mozliwy_ruch.sort()
            return mozliwy_ruch
        else:
            for y in whatIsToBeat(tile, strona):
                mozliwy_ruch.append(y)
            if (isAnythingAhead(tile, strona)):
                mozliwy_ruch.append(tile+10)#, tile+20
                mozliwy_ruch.sort()
                if (isAnythingAhead(tile+10, strona)):
                    mozliwy_ruch.append(tile+20)#, tile+20
                    mozliwy_ruch.sort()
            return mozliwy_ruch
    if (klasa=="p"):
        if (strona=="c"):
            for y in whatIsToBeat(tile, strona):
                print(y)
                for v in mozliwy_ruch:
                    print(v)
                mozliwy_ruch.append(y)
                for v in mozliwy_ruch:
                    print(v)
            if (isAnythingAhead(tile, strona)):
                mozliwy_ruch.append(tile-10)#, tile-20
                mozliwy_ruch.sort()
            return mozliwy_ruch
        else:
            for y in whatIsToBeat(tile, strona):
                mozliwy_ruch.append(y)
            if (isAnythingAhead(tile, strona)):
                mozliwy_ruch.append(tile+10)#, tile+20
                
                mozliwy_ruch.sort()
            return mozliwy_ruch
    if (klasa=="w"):
        for x in range(8):
            x=x+1
            if ((wspx+x)<=7):
                if Przyciski[f"przycisk{wspy}{wspx+x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy}{wspx+x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile+x)
                        break
                else:
                    mozliwy_ruch.append(tile+x)
        for x in range(8):
            x=x+1
            if ((wspx-x)>=0):
                if Przyciski[f"przycisk{wspy}{wspx-x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy}{wspx-x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile-x)
                        break
                else:
                    mozliwy_ruch.append(tile-x)
        for x in range(8):
            x=x+1
            if ((wspy+x)<=7):
                if Przyciski[f"przycisk{wspy+x}{wspx}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy+x}{wspx}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile+x*10)
                        break
                else:
                    mozliwy_ruch.append(tile+x*10)
        for x in range(8):
            x=x+1
            if ((wspy-x)>=0):
                r=Przyciski[f"przycisk{wspy-x}{wspx}"].cget('text')
                if r!="":
                    if Przyciski[f"przycisk{wspy-x}{wspx}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile-x*10)
                        break
                else:
                    mozliwy_ruch.append(tile-x*10)

        mozliwy_ruch.sort()
        return mozliwy_ruch
    if (klasa=="k"):
        if (wspx+2<=7):
            if((wspy)+1<=7):
                if (Przyciski[f"przycisk{wspy+1}{wspx+2}"].cget('text')+"x")[0]!=strona:
                    mozliwy_ruch.append(tile+12)
            if((wspy)-1>=0):
                if (Przyciski[f"przycisk{wspy-1}{wspx+2}"].cget('text')+"x")[0]!=strona:
                    mozliwy_ruch.append(tile-8)
        if (wspx-2)>=0:
            if((wspy)+1<=7):
                if (Przyciski[f"przycisk{wspy+1}{wspx-2}"].cget('text')+"x")[0]!=strona:
                    mozliwy_ruch.append(tile+8)
            if((wspy)-1>=0):
                if (Przyciski[f"przycisk{wspy-1}{wspx-2}"].cget('text')+"x")[0]!=strona:
                    mozliwy_ruch.append(tile-12)
        if((wspy)+2<=7):
            if(wspx+1<=7):
                if (Przyciski[f"przycisk{wspy+2}{wspx+1}"].cget('text')+"x")[0]!=strona:
                    mozliwy_ruch.append(tile+21)
            if(wspx-1>=0):
                if (Przyciski[f"przycisk{wspy+2}{wspx-1}"].cget('text')+"x")[0]!=strona:
                    mozliwy_ruch.append(tile+19)
        if((wspy)-2>=0):
            if(wspx+1<=7):
                if (Przyciski[f"przycisk{wspy-2}{wspx+1}"].cget('text')+"x")[0]!=strona:
                    mozliwy_ruch.append(tile-19)
            if(wspx-1>=0):
                if (Przyciski[f"przycisk{wspy-2}{wspx-1}"].cget('text')+"x")[0]!=strona:
                    mozliwy_ruch.append(tile-21)
        mozliwy_ruch.sort()
        return mozliwy_ruch
    if (klasa=="g"):
        for x in range(8):
            x=x+1
            if ((wspy+x<=7) and (wspx+x<=7)):
                if Przyciski[f"przycisk{wspy+x}{wspx+x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy+x}{wspx+x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile+11*x)
                        break
                else:
                    mozliwy_ruch.append(tile+11*x)
        for x in range(8):
            x=x+1
            if ((wspy+x<=7) and (wspx-x>=0)):
                if Przyciski[f"przycisk{wspy+x}{wspx-x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy+x}{wspx-x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile+9*x)
                        break
                else:
                    mozliwy_ruch.append(tile+9*x)                
        for x in range(8):
            x=x+1
            if ((wspy-x>=0) and (wspx-x>=0)):
                if Przyciski[f"przycisk{wspy-x}{wspx-x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy-x}{wspx-x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile-11*x)
                        break
                else:
                    mozliwy_ruch.append(tile-11*x) 
        for x in range(8):
            x=x+1
            if ((wspy-x>=0) and (wspx+x<=7)):
                if Przyciski[f"przycisk{wspy-x}{wspx+x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy-x}{wspx+x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile-9*x)
                        break
                else:
                    mozliwy_ruch.append(tile-9*x) 
        mozliwy_ruch.sort()
        return mozliwy_ruch
    if (klasa=="h"):
        for x in range(8):
            x=x+1
            if ((wspx+x)<=7):
                if Przyciski[f"przycisk{wspy}{wspx+x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy}{wspx+x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile+x)
                        break
                else:
                    mozliwy_ruch.append(tile+x)
        for x in range(8):
            x=x+1
            if ((wspx-x)>=0):
                if Przyciski[f"przycisk{wspy}{wspx-x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy}{wspx-x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile-x)
                        break
                else:
                    mozliwy_ruch.append(tile-x)
        for x in range(8):
            x=x+1
            if ((wspy+x)<=7):
                if Przyciski[f"przycisk{wspy+x}{wspx}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy+x}{wspx}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile+x*10)
                        break
                else:
                    mozliwy_ruch.append(tile+x*10)
        for x in range(8):
            x=x+1
            if ((wspy-x)>=0):
                r=Przyciski[f"przycisk{wspy-x}{wspx}"].cget('text')
                if r!="":
                    if Przyciski[f"przycisk{wspy-x}{wspx}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile-x*10)
                        break
                else:
                    mozliwy_ruch.append(tile-x*10)
        for x in range(8):
            x=x+1
            if ((wspy+x<=7) and (wspx+x<=7)):
                if Przyciski[f"przycisk{wspy+x}{wspx+x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy+x}{wspx+x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile+11*x)
                        break
                else:
                    mozliwy_ruch.append(tile+11*x)
        for x in range(8):
            x=x+1
            if ((wspy+x<=7) and (wspx-x>=0)):
                if Przyciski[f"przycisk{wspy+x}{wspx-x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy+x}{wspx-x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile+9*x)
                        break
                else:
                    mozliwy_ruch.append(tile+9*x)                
        for x in range(8):
            x=x+1
            if ((wspy-x>=0) and (wspx-x>=0)):
                if Przyciski[f"przycisk{wspy-x}{wspx-x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy-x}{wspx-x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile-11*x)
                        break
                else:
                    mozliwy_ruch.append(tile-11*x) 
        for x in range(8):
            x=x+1
            if ((wspy-x>=0) and (wspx+x<=7)):
                if Przyciski[f"przycisk{wspy-x}{wspx+x}"].cget('text')!="":
                    if Przyciski[f"przycisk{wspy-x}{wspx+x}"].cget('text')[0]==strona:
                        break
                    else:
                        mozliwy_ruch.append(tile-9*x)
                        break
                else:
                    mozliwy_ruch.append(tile-9*x) 
        mozliwy_ruch.sort()
        return mozliwy_ruch 
    if (klasa=="c"):
        x=1
        if ((wspy+x<=7) and (wspx+x<=7)):
            if Przyciski[f"przycisk{wspy+x}{wspx+x}"].cget('text')=="":
                mozliwy_ruch.append(tile+11*x)
            elif Przyciski[f"przycisk{wspy+x}{wspx+x}"].cget('text')[0]!=strona:
                mozliwy_ruch.append(tile+11*x)
        if ((wspy+x<=7) and (wspx-x>=0)):
            if Przyciski[f"przycisk{wspy+x}{wspx-x}"].cget('text')=="":
                mozliwy_ruch.append(tile+9*x)
            elif Przyciski[f"przycisk{wspy+x}{wspx-x}"].cget('text')[0]!=strona:
                mozliwy_ruch.append(tile+9*x)
        if ((wspy-x>=0) and (wspx-x>=0)):
            if Przyciski[f"przycisk{wspy-x}{wspx-x}"].cget('text')=="":
                mozliwy_ruch.append(tile-11*x)
            elif Przyciski[f"przycisk{wspy-x}{wspx-x}"].cget('text')[0]!=strona:
                mozliwy_ruch.append(tile-11*x)
        if ((wspy-x>=0) and (wspx+x<=7)):
            if Przyciski[f"przycisk{wspy-x}{wspx+x}"].cget('text')=="":
                mozliwy_ruch.append(tile-9*x)
            elif Przyciski[f"przycisk{wspy-x}{wspx+x}"].cget('text')[0]!=strona:
                mozliwy_ruch.append(tile-9*x)
        if ((wspx+x)<=7):
            if Przyciski[f"przycisk{wspy}{wspx+x}"].cget('text')=="":
                mozliwy_ruch.append(tile+x)
            elif Przyciski[f"przycisk{wspy}{wspx+x}"].cget('text')[0]!=strona:
                mozliwy_ruch.append(tile+x)
        if ((wspx-x)>=0):
            if Przyciski[f"przycisk{wspy}{wspx-x}"].cget('text')=="":
                mozliwy_ruch.append(tile-x)
            elif Przyciski[f"przycisk{wspy}{wspx-x}"].cget('text')[0]!=strona:
              mozliwy_ruch.append(tile-x)
        if ((wspy+x)<=7):
            if Przyciski[f"przycisk{wspy+x}{wspx}"].cget('text')=="":
                mozliwy_ruch.append(tile+x*10)
            elif Przyciski[f"przycisk{wspy+x}{wspx}"].cget('text')[0]!=strona:
                mozliwy_ruch.append(tile+x*10)
        if ((wspy-x)>=0):
            if Przyciski[f"przycisk{wspy-x}{wspx}"].cget('text')=="":
                mozliwy_ruch.append(tile-x*10)
            elif Przyciski[f"przycisk{wspy-x}{wspx}"].cget('text')[0]!=strona:
                mozliwy_ruch.append(tile-x*10)
        mozliwy_ruch.sort()
        return mozliwy_ruch 
#----------------------------#
def pozycjaStartowa(Przyciski, Obrazki):  #Ustawia po polach 0-1 i 6-7 figury w pozycji startowej
    color = "red"
    for y in range(8):
        for x in range (8):
            if (y==0):
                if ((x==0) or  (x==7)):
                    Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="bw",image=Obrazki["wieza_biala_obr"])
                if ((x==1) or (x==6)):
                    Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="bk",image=Obrazki["kon_bialy_obr"])
                if ((x==2) or (x==5)):
                    Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="bg",image=Obrazki["goniec_bialy_obr"])
                if (x==3):
                    Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="bc",image=Obrazki["krol_bialy_obr"])
                if (x==4):
                    Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="bh",image=Obrazki["hetman_bialy_obr"])
            elif (y==1):
                Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="bs",image=Obrazki["pion_bialy_obr"])
            elif (y==6):
                Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="cs",image=Obrazki["pion_czarny_obr"])
            elif (y==7):
                if ((x==0) or  (x==7)):
                    Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="cw",image=Obrazki["wieza_czarna_obr"])
                if ((x==1) or (x==6)):
                    Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="ck",image=Obrazki["kon_czarny_obr"])
                if ((x==2) or (x==5)):
                    Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="cg",image=Obrazki["goniec_czarny_obr"])
                if (x==3):
                    Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="cc",image=Obrazki["krol_czarny_obr"])
                if (x==4):
                    Przyciski[f"przycisk{y}{x}"].configure(width=1,height=1, text="ch",image=Obrazki["hetman_czarny_obr"])
#----------------------------#
def emptyMap(root,Przyciski,Ramki): # Tworzy plansze 8x8
    for i in range(8):  #  weight ustawia taki sam priorytet przy skalowaniu, unifrom sprawia ze kazdy obiekt w grupie ma rozmiar najwiekszego
        root.grid_rowconfigure(i, weight=1, uniform="grp")
        root.grid_columnconfigure(i, weight=1, uniform="grp")
    for y in range(8):  # tworzy ramke z przyciskiem
        for x in range (8):
            if ((x+y)%2==0):
                color = "white"
            else:
                color = "green"
            Ramki[f"ramka{y}{x}"] = Frame(root, highlightbackground="black", borderwidth=0, width=1, height=1, highlightthickness=2)
            Przyciski[f"przycisk{y}{x}"] = Button(Ramki[f"ramka{y}{x}"], text="", background=color, command=lambda x=x, y=y: buttonPressed(Przyciski,Przyciski[f"przycisk{y}{x}"],x,y,Ramki,tura))
            Przyciski[f"przycisk{y}{x}"].pack(expand=True, fill='both')
            Ramki[f"ramka{y}{x}"].grid(row=y, column=x, sticky="nsew")
#----------------------------#
def buttonPressed (Przyciski,called_button,xcords,ycords,Ramki,turn):
    if ycords==0:
        local="0"+str(xcords)
    else:
        local=ycords*10+xcords
    if Ramki[f"ramka{local}"].cget('highlightbackground')!="red":   #Gdy wybrano pole nie bedace mozliwym ruchem
        global pole
        if ycords==0:
            pole="0"+str(xcords)
        else:
            pole=ycords*10+xcords
        if Przyciski[f"przycisk{pole}"].cget('text')!="":
            h=turn
            if Przyciski[f"przycisk{pole}"].cget('text')[0]==h:
        #if 1==1:
            
                for x in range(8):
                    for y in range (8):
                        Ramki[f"ramka{x}{y}"].configure(highlightbackground="black")
                figure = called_button.cget('text')
                if figure != "":
                    print("mozliwe ruchy: ",ruch(figure,pole))
                    for mozliwy_ruch in ruch(figure,pole): #dla kazdego mozliwego ruchu
                        kolor_figury = Przyciski[f"przycisk{mozliwy_ruch//10}{mozliwy_ruch%10}"].cget("text")
                        print("kolor figury: ",kolor_figury)
                        print('mozliwy ruch=', mozliwy_ruch)
                        Ramki[f"ramka{mozliwy_ruch//10}{mozliwy_ruch%10}"].configure(highlightbackground="red")
                        # if kolor_figury=="":
                        #     Ramki[f"ramka{mozliwy_ruch//10}{mozliwy_ruch%10}"].configure(highlightbackground="red")
                        # elif kolor_figury[0]!=figure[0]:
                        #     Ramki[f"ramka{mozliwy_ruch//10}{mozliwy_ruch%10}"].configure(highlightbackground="red")
    else: #Gdy wybrano pole w ktore moze sie przemiescic figura
        global tura
        if turn=="b":
            tura="c"
        else:
            tura="b"
        print()
        text_of_selected_button = Przyciski[f"przycisk{pole}"].cget('text')
        czy_krol = Przyciski[f"przycisk{local}"].cget('text')
        if text_of_selected_button == "bs":
            text_of_selected_button="bp"
        if text_of_selected_button == "cs":
            text_of_selected_button="cp"
        image_of_selected_button = Przyciski[f"przycisk{pole}"].cget('image')
        called_button.configure(image=image_of_selected_button)
        Przyciski[f"przycisk{pole}"].configure(image="", text="")
        if czy_krol=="cc" or czy_krol=="bc":
            show_warning(text_of_selected_button)
        if (text_of_selected_button=="cp" and int(local)<10):
            Przyciski[f"przycisk{local}"].configure(image=Obrazki["hetman_czarny_obr"], text="ch")
        elif (text_of_selected_button=="bp" and int(local)>69):
            Przyciski[f"przycisk{local}"].configure(image=Obrazki["hetman_bialy_obr"], text="bh")
        else:
            Przyciski[f"przycisk{local}"].configure(image=image_of_selected_button, text=text_of_selected_button)
        for x in range(8):
            for y in range (8):
                Ramki[f"ramka{y}{x}"].configure(highlightbackground="black")
        bite_pola = set()
        for y in range(8):
            for x in range (8):
                complete_tile=str(y)+str(x)
                typ_figury=Przyciski[f"przycisk{complete_tile}"].cget('text')
                if typ_figury!="":
                    if typ_figury[0]!=tura:
                        for mozliwosc in ruch(typ_figury, complete_tile):
                            bite_pola.add(mozliwosc)
        print("Bite pola: ")
        for x in bite_pola:
            print(x)
            if (int(x)<10):
                x="0"+str(x)
            Ramki[f"ramka{x}"].configure(highlightbackground="blue")

                       

#----------------------------#
#----------------------------#
#----------------------------#

# list1 = {"kamien", "papier", "drewno"}
# list2 = {"k", "dro", "metal"}
# list3 = list1 - list2
# print(list3)

ramki_przyciski()
emptyMap(root,Przyciski,Ramki)
pozycjaStartowa(Przyciski,Obrazki)


root.mainloop()


