from datetime import datetime
import os
import tkinter as tk

def play_activitate_first():
    os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\play_activities\\firstmeet.py')

def back(frame_nivel, frame_button_back, frame_deconectare):
    frame_pachet.pack_forget()
    frame_button_back_nivel.pack_forget()
    frame_deconectare.pack(side='top', anchor='nw')
    frame_nivel.pack(fill=tk.BOTH, padx=20)
    frame_button_back.pack(side='bottom', anchor='se')


def fereastra_first_meet(root, frame_nivel, frame_button_back, frame_deconectare):
    global frame_pachet
    frame_pachet = tk.Frame(root, bg="white")
    frame_pachet.pack(fill=tk.BOTH, padx=20, pady=180)

    label_first_meet = tk.Label(frame_pachet, text="Pachetul s-a instalat!\nSă începem activitatea!", font=("Verdana", 18), background="white",
                       width=30, height=2, justify="center")
    label_first_meet.pack(pady=10)

    button_play_first = tk.Button(frame_pachet, text="Play activitate\nFirst Meet", background="white", font=("Verdana", 12),
                                  width=15, height=3, command=play_activitate_first)
    button_play_first.pack(pady=10)

    global frame_button_back_nivel
    frame_button_back_nivel = tk.Frame(root, bg="white")
    frame_button_back_nivel.pack(side='bottom', anchor='se')

    button_back_date = tk.Button(frame_button_back_nivel, text="Înapoi", background="white", font=("Verdana", 10), width=15,
                                 height=1, borderwidth=4, command=lambda: back(frame_nivel, frame_button_back, frame_deconectare))
    button_back_date.pack(padx=20, pady=20)
