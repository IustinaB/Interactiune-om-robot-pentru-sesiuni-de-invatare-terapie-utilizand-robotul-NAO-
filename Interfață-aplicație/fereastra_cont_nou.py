import re
import tkinter as tk
from conectare_bd import conectare


def email_valid(email):
    valid=r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    return re.match(valid, email)


def inserare_date(entry_email,entry_parola):
    email = entry_email.get()
    parola = entry_parola.get()
    if email=="" or parola=="":
        raspuns="Trebuie să completați\ntoate câmpurile!"
    elif not email_valid(email):
        raspuns="Formatul pentru email este invalid!"
    elif len(parola)<7:
        raspuns="Parola trebuie\nsă aibă minim 7 caractere!"
    else:
        connection=conectare()
        cursor = connection.cursor()
        try:
            sql = "INSERT INTO terapeut (email, parola) VALUES (%s, %s)"
            cursor.execute(sql, (email, parola))
            connection.commit()
            raspuns="Date inserate cu succes.\nMergi pe pagina de anterioară\nși încearcă să te autentifici!"

            entry_email.delete(0, tk.END)
            entry_parola.delete(0, tk.END)
        except Exception as e:
                print(f"Eroare la interogare: {e}")
        finally:
            cursor.close()

    label_raspuns.config(text=raspuns)
    label_raspuns.place(x=50, y=290)


def creare_cont():
    cont = tk.Tk()
    cont.title("Creare cont")
    cont.geometry('400x400')
    cont.configure(bg="white")

    label_date = tk.Label(cont, text="Introduceți datele", font=("Verdana", 12), background="white",
                       width=30, height=2, justify="center")
    label_date.place(x=50, y=40)

    label_email = tk.Label(cont, text="Email:", font=("Verdana", 10), background="white",
                           width=10, height=2, justify="center")
    label_email.place(x=30, y=110)

    label_parola = tk.Label(cont, text="Parolă:", font=("Verdana", 10), background="white",
                            width=10, height=2, justify="center")
    label_parola.place(x=30, y=150)

    global entry_email, entry_parola
    entry_email = tk.Entry(cont, width=30, borderwidth=2, font=("Verdana", 10), relief="sunken")
    entry_email.place(x=100, y=120)

    entry_parola = tk.Entry(cont, width=30, font=("Verdana", 10), show="*", borderwidth=2, relief="sunken")
    entry_parola.place(x=100, y=160)

    button_creare = tk.Button(cont, text="Înregistrare", background="white", font=("Verdana", 10), width=12, height=1,
                             borderwidth=4, command= lambda: inserare_date(entry_email, entry_parola, cont))
    button_creare.place(x=150, y=220)

    global label_raspuns
    label_raspuns = tk.Label(cont, text="", font=("Verdana", 12), background="white",
                             width=30, height=3, justify="center")

    cont.mainloop()