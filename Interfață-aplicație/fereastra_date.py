import tkinter as tk
from tkinter import ttk
from fereastra_copil_activitati import pagina_detalii_copil
from conectare_bd import conectare
from fereastra_adaugare_copil import adaugare_copil
from tkinter import messagebox


def stergere(cnp_copil, id_terapeut):
    result = messagebox.askyesno("Confirmă Ștergerea", "Sunteți sigur că doriți să ștergeți pacientul?")
    if result == True:
        connection = conectare()
        cursor = connection.cursor()
        try:
            query = "DELETE from activitate WHERE id_pacient_fk = %s"
            cursor.execute(query, (cnp_copil,))
            connection.commit()

            query1 = "DELETE from pacient WHERE id_pacient_cnp = %s"
            cursor.execute(query1, (cnp_copil,))
            connection.commit()
            messagebox.showinfo("Deleted", "Pacientul a fost șters.")

            query2 = "SELECT id_pacient_cnp, prenume, nume, gen, varsta FROM pacient WHERE id_terapeut_fk = %s"
            cursor.execute(query2, (id_terapeut,))
            date_copii = cursor.fetchall()

            for row in tabel_date.get_children():
                tabel_date.delete(row)

            for index, row in enumerate(date_copii, start=1):
                tabel_date.insert("", "end", values=(index,) + row)
        except Exception as e:
            print(f"Eroare la interogare: {e}")
        finally:
            cursor.close()
    else:
        pass


def deconectare(frame_main, background_label):
    frame.pack_forget()
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    frame_main.pack(side=tk.RIGHT, pady=20, padx=200)


def vizualizare_detalii(event,root, frame_main, background_label, id_terapeut):
    element = tabel_date.focus()  #elementul selectat
    cnp_copil=tabel_date.item(element,"values")[1]
    nume_copil = tabel_date.item(element, "values")[2]
    prenume_copil=tabel_date.item(element,"values")[3]
    button_detalii.config(command=lambda: pagina_detalii_copil(cnp_copil,nume_copil,prenume_copil,root, frame, frame_main, background_label))
    button_detalii.pack(pady=10)
    buton_stergere.config(command=lambda: stergere(cnp_copil, id_terapeut))
    buton_stergere.pack(pady=10)

def pagina_date(root, id_terapeut, frame_main, background_label):
    root.title("Vizualizare date")

    global frame
    frame = tk.Frame(root, bg="white")
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    button_deconectare=tk.Button(frame, text="Deconectare", background="white", font=("Verdana", 10), width=12, height=1,
                                      borderwidth=4, command=lambda: deconectare(frame_main, background_label))
    button_deconectare.pack(side=tk.LEFT, anchor=tk.NW, padx=10, pady=10)

    global button_adaugare_copil
    button_adaugare_copil = tk.Button(frame, text="Adăugare pacient", background="white", font=("Verdana", 10), width=18,
                                      height=1,
                                      borderwidth=4, command=lambda: adaugare_copil(id_terapeut, tabel_date))
    button_adaugare_copil.pack(side=tk.RIGHT, anchor=tk.NE, padx=10, pady=10)

    global label_vizualizare
    label_vizualizare=tk.Label(frame, text="Vizualizare date pacienți înregistrați", font=("Verdana", 12), background="white",
                       width=30, height=1, justify="center")
    label_vizualizare.pack(side=tk.TOP, fill=tk.X, padx=20,pady=60)


    connection=conectare()
    if connection is None:
        return "Eroare la conectare!"
    try:
        cursor = connection.cursor()

        query = "SELECT id_pacient_cnp, prenume, nume, gen, varsta FROM pacient WHERE id_terapeut_fk = %s"
        cursor.execute(query,(id_terapeut,))

        date_copii = cursor.fetchall()

        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Eroare la executarea interogării: {e}")
        return

    global tabel_date
    # creare tabel
    tabel_date = ttk.Treeview(frame, columns=("col1", "col2", "col3", "col4", "col5", "col6"), show="headings")
    tabel_date.heading("col1", text="Nr.")
    tabel_date.heading("col2", text="CNP")
    tabel_date.heading("col3", text="Nume")
    tabel_date.heading("col4", text="Prenume")
    tabel_date.heading("col5", text="Gen")
    tabel_date.heading("col6", text="Vârsta")

    tabel_date.column("col1", width=50, anchor='center')
    tabel_date.column("col2", width=150, anchor='center')
    tabel_date.column("col3", width=150, anchor='center')
    tabel_date.column("col4", width=150, anchor='center')
    tabel_date.column("col5", width=150, anchor='center')
    tabel_date.column("col6", width=150, anchor='center')

    for index, row in enumerate(date_copii, start=1):
        tabel_date.insert("", "end", values=(index,) + row)

    global button_detalii
    button_detalii = tk.Button(frame, text="Detalii activități", background="white", font=("Verdana", 9), width=30, height=1,
                            borderwidth=4 )
    global buton_stergere
    buton_stergere=tk.Button(frame, text="Ștergere pacient", background="white", font=("Verdana", 9), width=30, height=1,
                            borderwidth=4 )
    tabel_date.bind("<ButtonRelease-1>", lambda event: vizualizare_detalii(event, root, frame_main, background_label, id_terapeut))

    tabel_date.pack(padx=20)


    root.mainloop()

if __name__ == "__main__":
    pagina_date()
