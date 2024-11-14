import tkinter as tk
import os
from pagini_play.first_meet_play import fereastra_first_meet
from pagini_play.soundrec_play import fereastra_sound
from pagini_play.numbers_play import fereastra_numbers
from pagini_play.figures_play import fereastra_figures
from pagini_play.speech_play import fereastra_speech
from pagini_play.colors_play import fereastra_colors
from pagini_play.animals_play import fereastra_animals
from pagini_play.fruits_play import fereastra_fruits


def deconectare(frame_main, background_label):
    frame_nivel.pack_forget()
    frame_nivel1.pack_forget()
    frame_nivel2.pack_forget()
    frame_nivel3.pack_forget()
    frame_button_back.pack_forget()
    frame_deconectare.pack_forget()

    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    frame_main.pack(side=tk.RIGHT, pady=20, padx=200)


def back(frame_copil, frame_butoane):
    frame_nivel.pack_forget()
    frame_nivel1.pack_forget()
    frame_nivel2.pack_forget()
    frame_nivel3.pack_forget()
    frame_button_back.pack_forget()
    frame_deconectare.pack_forget()

    frame_copil.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    frame_butoane.pack(side='bottom', anchor='se')


def stergere_frame():
    frame_nivel.pack_forget()
    frame_nivel1.pack_forget()
    frame_nivel2.pack_forget()
    frame_nivel3.pack_forget()
    frame_button_back.pack_forget()
    frame_deconectare.pack_forget()


# nivel 1
def first_meet_install(root):
    stergere_frame()
    os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\firstmeet_installpkg.py')
    fereastra_first_meet(root, frame_nivel, frame_button_back, frame_deconectare)


def numbers_recognition_install(root, cnp_copil, tabel_date):
    stergere_frame()
    os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\numberrecognition_installpkg.py')
    fereastra_numbers(root, frame_nivel, frame_button_back, frame_deconectare, cnp_copil, tabel_date)


def geometricfigures_recognition_install(root, cnp_copil, tabel_date):
    stergere_frame()
    os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\geometricfiguresrec_installpkg.py')
    fereastra_figures(root, frame_nivel, frame_button_back, frame_deconectare, cnp_copil, tabel_date)


#nivel 1.2.3
def speech_recognition_install(root, cnp_copil, tabel_date):
    stergere_frame()
    os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\speechrecognition_installpkg.py')
    fereastra_speech(root, frame_nivel, frame_button_back, frame_deconectare, cnp_copil, tabel_date)


def sound_recognition_install(root, cnp_copil, tabel_date):
    stergere_frame()
    os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\soundrecognition_installpkg.py')
    fereastra_sound(root, frame_nivel, frame_button_back, frame_deconectare, cnp_copil, tabel_date)


def fruits_recognition_install(root, cnp_copil, tabel_date):
    stergere_frame()
    os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\fruitsrec_installpkg.py')
    fereastra_fruits(root, frame_nivel, frame_button_back, frame_deconectare, cnp_copil, tabel_date)


def colors_recognition_install(root, nivel,  cnp_copil,tabel_date):
    stergere_frame()
    if nivel==1:
        os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\colorsrec1_installpkg.py')
    elif nivel==2:
        os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\colorsrec2_installpkg.py')
    else:
        os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\colorrecognition_installpkg.py')
    fereastra_colors(root, frame_nivel, frame_button_back, frame_deconectare, nivel, cnp_copil, tabel_date)


def animals_recognition_install(root, nivel, cnp_copil,tabel_date):
    stergere_frame()
    if nivel==1:
        os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\animalsrec1_installpkg.py')
    elif nivel==2:
        os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\animalsrec2_installpkg.py')
    else:
        os.system('C:\\Python27\\python.exe C:\\.Partitie_cu_informatii\\An4\\Licenta\\instalare_pachete\\animalsrecognition_installpkg.py')
    fereastra_animals(root, frame_nivel, frame_button_back, frame_deconectare,nivel, cnp_copil,tabel_date)


def nivel_1(root):
    frame_nivel2.pack_forget()
    frame_nivel3.pack_forget()
    frame_nivel1.pack()


def nivel_2(root):
    frame_nivel1.pack_forget()
    frame_nivel3.pack_forget()
    frame_nivel2.pack()


def nivel_3(root):
    frame_nivel1.pack_forget()
    frame_nivel2.pack_forget()
    frame_nivel3.pack()


def tipuri_activitati(root, frame_copil, frame_butoane, frame_main, background_label, cnp_copil, tabel_date):
    frame_copil.pack_forget()
    frame_butoane.pack_forget()
    root.title("Activități")

    global frame_deconectare
    frame_deconectare = tk.Frame(root, bg="white")
    frame_deconectare.pack(side='top', anchor='nw')

    button_deconectare = tk.Button(frame_deconectare, text="Deconectare", background="white", font=("Verdana", 10), width=12, height=1,
                                   borderwidth=4, command=lambda: deconectare(frame_main,background_label))
    button_deconectare.pack(side=tk.LEFT, anchor=tk.NW, padx=20, pady=(20,0))

    global frame_nivel
    frame_nivel = tk.Frame(root, bg="white")
    frame_nivel.pack(fill=tk.BOTH, padx=20)

    label_nivel = tk.Label(frame_nivel, text="Nivel activitate", font=("Verdana", 13), background="white",
                           width=30, height=2, justify="center")
    label_nivel.pack(pady=10)

    frame_butoane_nivel = tk.Frame(frame_nivel, bg="white")
    frame_butoane_nivel.pack(pady=10)

    button_n1 = tk.Button(frame_butoane_nivel, text="Nivel 1", background="white", font=("Verdana", 12), width=10, height=1,
                          borderwidth=4, command=lambda: nivel_1(root))
    button_n1.pack(side=tk.LEFT, padx=25)

    button_n2 = tk.Button(frame_butoane_nivel, text="Nivel 2", background="white", font=("Verdana", 12), width=10, height=1,
                          borderwidth=4, command=lambda: nivel_2(root))
    button_n2.pack(side=tk.LEFT, padx=25)

    button_n3 = tk.Button(frame_butoane_nivel, text="Nivel 3", background="white", font=("Verdana", 12), width=10, height=1,
                          borderwidth=4, command=lambda: nivel_3(root))
    button_n3.pack(side=tk.LEFT, padx=25)


    # nivel 1
    global frame_nivel1
    frame_nivel1 = tk.Frame(root, bg="white", padx=20, pady=20)

    label_activitati_n1 = tk.Label(frame_nivel1, text="Alege una dintre activitățile de nivel 1!", font=("Verdana", 15), background="white",
                                    width=40, height=1, justify="center")

    button_first_meet = tk.Button(frame_nivel1, text="Prima întâlnire cu robotul", background="white", font=("Verdana", 12), width=40, height=2,
                                   borderwidth=4, command=lambda: first_meet_install(root))


    button_numbers_recognition = tk.Button(frame_nivel1, text="Învățare cifre", background="white", font=("Verdana", 12), width=40, height=2,
                                            borderwidth=4, command=lambda :numbers_recognition_install(root, cnp_copil, tabel_date))

    button_geometricfig_recognition = tk.Button(frame_nivel1, text="Învățare figuri geometrice", background="white", font=("Verdana", 12), width=40, height=2,
                                                 borderwidth=4, command=lambda :geometricfigures_recognition_install(root, cnp_copil, tabel_date))
    button_animals_recognition1 = tk.Button(frame_nivel1, text="Recunoaștere animale pe baza imaginilor", background="white",
                                           font=("Verdana", 12), width=40, height=2,
                                           borderwidth=4, command=lambda: animals_recognition_install(root,1, cnp_copil, tabel_date))
    button_colors_recognition1 = tk.Button(frame_nivel1, text="Recunoaștere culori", background="white",
                                           font=("Verdana", 12), width=40, height=2,
                                           borderwidth=4, command=lambda: colors_recognition_install(root, 1,  cnp_copil,tabel_date))
    label_activitati_n1.pack(pady=10)
    button_first_meet.pack(pady=10)
    button_numbers_recognition.pack(pady=10)
    button_geometricfig_recognition.pack(pady=10)
    button_animals_recognition1.pack(pady=10)
    button_colors_recognition1.pack(pady=10)

    # #nivel 2
    global frame_nivel2
    frame_nivel2 = tk.Frame(root, bg="white", padx=20, pady=20)

    label_activitati_n2 = tk.Label(frame_nivel2, text="Alege una dintre activitățile de nivel 2!", font=("Verdana", 15),
                                    background="white", width=40, height=1, justify="center")
    label_activitati_n2.pack(pady=10)

    button_animals_recognition2 = tk.Button(frame_nivel2, text="Recunoaștere animale pe baza imaginilor",
                                          background="white", font=("Verdana", 12), width=40, height=2,
                                          borderwidth=4, command=lambda: animals_recognition_install(root,2, cnp_copil,tabel_date))
    button_colors_recognition2 = tk.Button(frame_nivel2, text="Recunoaștere culori", background="white",
                                          font=("Verdana", 12), width=40, height=2,
                                          borderwidth=4, command=lambda: colors_recognition_install(root,2,  cnp_copil,tabel_date))
    button_fruits_recognition = tk.Button(frame_nivel2, text="Recunoaștere fructe pe baza imaginilor",
                                            background="white", font=("Verdana", 12), width=40, height=2,
                                            borderwidth=4,
                                            command=lambda: fruits_recognition_install(root, cnp_copil, tabel_date))
    button_animals_recognition2.pack(pady=10)
    button_colors_recognition2.pack(pady=10)
    button_fruits_recognition.pack(pady=10)

    # nivel 3
    global frame_nivel3
    frame_nivel3 = tk.Frame(root, bg="white", padx=20, pady=20)

    label_activitati_n3 = tk.Label(frame_nivel3, text="Alege una dintre activitățile de nivel 3!", font=("Verdana", 15), background="white",
                                    width=40, height=1, justify="center")
    button_speech_recognition = tk.Button(frame_nivel3, text="Recunoaștere animale pe baza descrierilor", background="white", font=("Verdana", 12), width=40, height=2,
                                           borderwidth=4, command=lambda :speech_recognition_install(root, cnp_copil, tabel_date))
    button_sound_recognition = tk.Button(frame_nivel3, text="Recunoaștere instrumente muzicale", background="white", font=("Verdana", 12), width=40, height=2,
                                          borderwidth=4, command= lambda: sound_recognition_install(root, cnp_copil, tabel_date))
    button_colors_recognition = tk.Button(frame_nivel3, text="Recunoaștere culori", background="white", font=("Verdana", 12), width=40, height=2,
                                           borderwidth=4, command=lambda :colors_recognition_install(root,3,cnp_copil, tabel_date))
    button_animals_recognition = tk.Button(frame_nivel3, text="Recunoaștere animale pe baza imaginilor", background="white",
                                          font=("Verdana", 12), width=40, height=2,
                                          borderwidth=4, command=lambda: animals_recognition_install(root, 3, cnp_copil, tabel_date))

    label_activitati_n3.pack(pady=10)
    button_speech_recognition.pack(pady=10)
    button_sound_recognition.pack(pady=10)
    button_colors_recognition.pack(pady=10)
    button_animals_recognition.pack(pady=10)

    global frame_button_back
    frame_button_back = tk.Frame(root, bg="white")
    frame_button_back.pack(side='bottom', anchor='se')

    button_back_date = tk.Button(frame_button_back, text="Înapoi", background="white", font=("Verdana", 10), width=15,
                                 height=1, borderwidth=4,
                                 command=lambda: back(frame_copil, frame_butoane))
    button_back_date.pack(padx=20, pady=20)




