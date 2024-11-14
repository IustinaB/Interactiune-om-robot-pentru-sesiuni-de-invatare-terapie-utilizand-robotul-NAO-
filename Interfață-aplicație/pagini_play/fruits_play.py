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


def play_activitate_fruits():
    label_fruits.pack_forget()
    button_play_fruits.pack_forget()
    frame_button_back_nivel.pack_forget()
    label_final.pack(pady=10)
    button_final.pack(pady=10)
    global nume_activitate, data_start
    nume_activitate = "Recunoaștere fructe din imagini - n2"
    data_start = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\play_activities\\fruitsbh.py')


def back(frame_nivel, frame_button_back, frame_deconectare):
    frame_pachet.pack_forget()
    frame_button_back_nivel.pack_forget()
    frame_deconectare.pack(side='top', anchor='nw')
    frame_nivel.pack(fill=tk.BOTH, padx=20)
    frame_button_back.pack(side='bottom', anchor='se')


def fereastra_fruits(root, frame_nivel, frame_button_back, frame_deconectare, cnp_copil, tabel_date):
    global frame_pachet, label_fruits, button_play_fruits
    frame_pachet = tk.Frame(root, bg="white")
    frame_pachet.pack(fill=tk.BOTH, padx=20, pady=180)

    label_fruits = tk.Label(frame_pachet, text="Pachetul pentru activitatea de recunoaștere\na fructelor din imagini s-a instalat!\nSă începem activitatea!",
                             font=("Verdana", 18), background="white",
                             width=40, height=3, justify="center")
    label_fruits.pack(pady=10)

    button_play_fruits = tk.Button(frame_pachet, text="Play activitate\nFruits Recognition", background="white",
                                    font=("Verdana", 12),
                                    width=20, height=3, command= lambda: play_activitate_fruits(cnp_copil, tabel_date))
    button_play_fruits.pack(pady=10)

    global button_final, label_final
    button_final = tk.Button(frame_pachet, text="Final activitate", background="white",
                             font=("Verdana", 12),
                             width=20, height=1,
                             command=lambda: finalizare_activitate(cnp_copil, tabel_date, frame_nivel,
                                                                   frame_button_back, frame_deconectare))
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