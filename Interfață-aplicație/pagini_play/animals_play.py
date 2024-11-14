import os
import tkinter as tk
from datetime import datetime
from pagini_play.inserare_date_activitate import insert_date

def finalizare_activitate(cnp_copil, tabel_date, frame_nivel, frame_button_back, frame_deconectare):
    data_stop = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    insert_date(nume_activitate, data_start, data_stop, cnp_copil, tabel_date)

    frame_pachet.pack_forget()
    frame_button_back_nivel.pack_forget()
    frame_deconectare.pack(side='top', anchor='nw')
    frame_nivel.pack(fill=tk.BOTH, padx=20)
    frame_button_back.pack(side='bottom', anchor='se')
def play_activitate_animals(nivel):
    label_animals.pack_forget()
    button_play_animals.pack_forget()
    frame_button_back_nivel.pack_forget()
    label_final.pack(pady=10)
    button_final.pack(pady=10)
    global nume_activitate, data_start
    if nivel==1:
        nume_activitate = "Recunoaștere animale pe baza imaginilor - n1"
        data_start = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\play_activities\\animalsbh1.py')
    elif nivel==2:
        nume_activitate = "Recunoaștere animale pe baza imaginilor - n2"
        data_start = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\play_activities\\animalsbh2.py')
    else:
        nume_activitate = "Recunoaștere animale pe baza imaginilor - n3"
        data_start = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\play_activities\\animalsbh.py')


def back(frame_nivel, frame_button_back, frame_deconectare):
    frame_pachet.pack_forget()
    frame_button_back_nivel.pack_forget()
    frame_deconectare.pack(side='top', anchor='nw')
    frame_nivel.pack(fill=tk.BOTH, padx=20)
    frame_button_back.pack(side='bottom', anchor='se')

def fereastra_animals(root, frame_nivel, frame_button_back, frame_deconectare, nivel, cnp_copil,tabel_date):
    global frame_pachet, label_animals
    frame_pachet = tk.Frame(root, bg="white")
    frame_pachet.pack(fill=tk.BOTH, padx=20, pady=180)

    label_animals = tk.Label(frame_pachet, text="Pachetul pentru activitatea de recunoaștere\na animalelor pe baza imaginilor\ns-a instalat! Să începem activitatea!",
                             font=("Verdana", 18), background="white",
                             width=40, height=3, justify="center")
    label_animals.pack(pady=10)
    global button_play_animals
    button_play_animals = tk.Button(frame_pachet, text="Play activitate\nAnimals recognition", background="white",
                                    font=("Verdana", 12),
                                    width=20, height=3, command= lambda: play_activitate_animals(nivel))
    button_play_animals.pack(pady=10)

    global button_final, label_final
    button_final=tk.Button(frame_pachet, text="Final activitate", background="white",
                                    font=("Verdana", 12),
                                    width=20, height=1, command= lambda: finalizare_activitate(cnp_copil,tabel_date, frame_nivel, frame_button_back, frame_deconectare))
    label_final = tk.Label(frame_pachet,
                             text="La finalul activității, pentru a înregistra\n datele despre activitate în baza de date\naccesați acest buton!",
                             font=("Verdana", 18), background="white",
                             width=40, height=3, justify="center")
    global frame_button_back_nivel
    frame_button_back_nivel = tk.Frame(root, bg="white")
    frame_button_back_nivel.pack(side='bottom', anchor='se')

    button_back_date = tk.Button(frame_button_back_nivel, text="Înapoi", background="white", font=("Verdana", 10),
                                 width=15,
                                 height=1, borderwidth=4,
                                 command=lambda: back(frame_nivel, frame_button_back, frame_deconectare))
    button_back_date.pack(padx=20, pady=20)