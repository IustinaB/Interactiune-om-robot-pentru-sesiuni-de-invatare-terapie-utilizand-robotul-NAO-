import tkinter as tk
from tkinter import ttk
import os
from fereastra_tipuri_activitati import tipuri_activitati
from conectare_bd import conectare


def deconectare(frame_main, background_label):
    frame_copil.pack_forget()
    frame_butoane.pack_forget()
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    frame_main.pack(side=tk.RIGHT, pady=20, padx=200)


def back(frame, frame_copil, frame_butoane):
    frame_copil.pack_forget()
    frame_butoane.pack_forget()
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


def conectare_nao(root, frame_copil, frame_butoane, frame_main, background_label, cnp_copil):
    os.system('C:\\Python27\\python.exe scriptconectare.py')
    tipuri_activitati(root, frame_copil, frame_butoane, frame_main, background_label, cnp_copil,tabel_date)


def pagina_detalii_copil(cnp_copil,nume_copil,prenume_copil,root,frame, frame_main, background_label):
    frame.pack_forget()

    root.title("Detalii activități")

    nume_complet=nume_copil + " " +prenume_copil

    global frame_copil
    frame_copil = tk.Frame(root, bg="white")
    frame_copil.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    button_deconectare = tk.Button(frame_copil, text="Deconectare", background="white", font=("Verdana", 10), width=12, height=1,
                                   borderwidth=4, command=lambda: deconectare(frame_main, background_label))
    button_deconectare.pack(side=tk.LEFT, anchor=tk.NW, padx=10, pady=10)

    button_conectare = tk.Button(frame_copil, text="Conectare NAO", background="white", font=("Verdana", 10), width=15,
                                 height=1, borderwidth=4, command=lambda: conectare_nao(root, frame_copil,
                                                                                              frame_butoane, frame_main,
                                                                                              background_label, cnp_copil))
    button_conectare.pack(side=tk.RIGHT, anchor=tk.NE, padx=10, pady=10)

    label_a = tk.Label(frame_copil, text=nume_complet, font=("Verdana", 13), background="white",
                       width=20, height=1, justify="center")
    label_a.pack(side=tk.TOP, fill=tk.X, padx=20,pady=60)

    connection = conectare()
    if connection is None:
        return "Eroare la conectare!"
    try:
        cursor = connection.cursor()

        query = "SELECT nume_activitate, data_inceput, data_sfarsit FROM activitate WHERE id_pacient_fk = %s"
        cursor.execute(query, (cnp_copil,))

        date_activitati_copil = cursor.fetchall()

        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Eroare la executarea interogării: {e}")
        return

    # creare tabel
    global tabel_date
    tabel_date = ttk.Treeview(frame_copil, columns=("col1", "col2", "col3", "col4"), show="headings")
    tabel_date.heading("col1", text="Nr.")
    tabel_date.heading("col2", text="Nume activitate")
    tabel_date.heading("col3", text="Data și ora începerii activității")
    tabel_date.heading("col4", text="Data și ora finalizării activității")

    tabel_date.column("col1", width=50, anchor='center')
    tabel_date.column("col2", width=300, anchor='center')
    tabel_date.column("col3", width=200, anchor='center')
    tabel_date.column("col4", width=200, anchor='center')

    for index, row in enumerate(date_activitati_copil, start=1):
        tabel_date.insert("", "end", values=(index,) + row)


    tabel_date.pack(padx=20)

    global frame_butoane
    frame_butoane = tk.Frame(root, bg="white")
    frame_butoane.pack(side='bottom', anchor='se')


    button_back_date = tk.Button(frame_butoane, text="Înapoi", background="white", font=("Verdana", 10), width=15, height=1, borderwidth=4,
                                 command=lambda: back(frame,frame_copil, frame_butoane))
    button_back_date.pack(padx=20, pady=20)

    root.mainloop()


