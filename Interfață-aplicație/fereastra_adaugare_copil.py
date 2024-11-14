import tkinter as tk
from conectare_bd import conectare
from datetime import datetime


def varsta_gen(cnp):
    cifra1 = int(cnp[0])
    an = int(cnp[1:3]) + 2000
    luna = int(cnp[3:5])
    zi = int(cnp[5:7])

    if cifra1 == 5:
        gen = 'M'
    elif cifra1 == 6:
        gen = 'F'

    zi_nastere = datetime(an, luna, zi)

    data_actuala=datetime.today()
    varsta=data_actuala.year - zi_nastere.year - ((data_actuala.month,data_actuala.day)<(zi_nastere.month, zi_nastere.day))
    return varsta, gen


def adaugare(root, id_terapeut, tabel_date, frame_copil):
    cnp = entry_cnp.get()
    nume = entry_nume.get()
    prenume = entry_prenume.get()

    if cnp=="" or nume=="" or prenume=="":
        raspuns="Trebuie completate toate câmpurile!"
    elif len(cnp)!=13 or not cnp.isdigit():
        raspuns="CNP ul trebuie să conțină 13 cifre!"
    elif not nume.isalpha() or not prenume.isalpha():
        raspuns="Numele și prenumele să nu conțină cifre!"
    else:
        varsta, gen =varsta_gen(cnp)
        connection = conectare()
        cursor = connection.cursor()
        try:
            sql = "INSERT INTO pacient (id_pacient_cnp, nume, prenume, gen, varsta, id_terapeut_fk) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (cnp, nume, prenume, gen, varsta, id_terapeut))
            connection.commit()
            raspuns = "Date inserate cu succes."
            print(raspuns)

            query = "SELECT id_pacient_cnp, prenume, nume, gen, varsta FROM pacient WHERE id_terapeut_fk = %s"
            cursor.execute(query, (id_terapeut,))
            date_copii = cursor.fetchall()

            for row in tabel_date.get_children():
                tabel_date.delete(row)

            for index, row in enumerate(date_copii, start=1):
                tabel_date.insert("", "end", values=(index,) + row)
            entry_cnp.delete(0, tk.END)
            entry_nume.delete(0, tk.END)
            entry_prenume.delete(0, tk.END)
        except Exception as e:
            print(f"Eroare la interogare: {e}")
        finally:
            cursor.close()
    label_raspuns = tk.Label(frame_copil, text=raspuns, font=("Verdana", 10), background="white",
                             width=40, height=2, justify="center")
    label_raspuns.place(x=20, y=280)


def adaugare_copil(id_terapeut, tabel_date):
    date_copil = tk.Tk()
    date_copil.title("Adăugare pacient")
    date_copil.geometry('400x400')
    date_copil.configure(bg="white")

    global frame_copil
    frame_copil = tk.Frame(date_copil, bg="white", width=400, height=500)
    frame_copil.pack(padx=20, pady=20)

    label_date = tk.Label(frame_copil, text="Introduceți datele", font=("Verdana", 12), background="white",
                          width=20, height=1, justify="center")
    label_date.place(x=80, y=30)

    label_cnp = tk.Label(frame_copil, text="CNP:", font=("Verdana", 10), background="white",
                           width=6, height=1, justify="center")
    label_cnp.place(x=20, y=100)

    label_nume = tk.Label(frame_copil, text="Nume:", font=("Verdana", 10), background="white",
                            width=6, height=1, justify="center")
    label_nume.place(x=20, y=140)

    label_prenume = tk.Label(frame_copil, text="Prenume:", font=("Verdana", 10), background="white",
                          width=8, height=1, justify="center")
    label_prenume.place(x=20, y=180)


    global entry_cnp, entry_nume, entry_prenume
    entry_cnp = tk.Entry(frame_copil, width=30, borderwidth=2, font=("Verdana", 10), relief="sunken")
    entry_cnp.place(x=90, y=100)

    entry_nume = tk.Entry(frame_copil, width=30, font=("Verdana", 10), borderwidth=2, relief="sunken")
    entry_nume.place(x=90, y=140)

    entry_prenume = tk.Entry(frame_copil, width=30, font=("Verdana", 10), borderwidth=2, relief="sunken")
    entry_prenume.place(x=90, y=180)

    button_creare = tk.Button(frame_copil, text="Înregistrare", background="white", font=("Verdana", 10), width=12, height=1,
                              borderwidth=4, command= lambda: adaugare(date_copil, id_terapeut, tabel_date, frame_copil))
    button_creare.place(x=120, y=240)

    date_copil.mainloop()