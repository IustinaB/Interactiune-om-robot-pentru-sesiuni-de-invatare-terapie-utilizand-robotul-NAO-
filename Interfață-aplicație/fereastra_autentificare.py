import tkinter as tk
from fereastra_date import pagina_date
from conectare_bd import conectare
from fereastra_cont_nou import creare_cont


def pagina_autentificare(root, frame_main, background_label):
    for widget in frame_main.winfo_children():
        widget.destroy()

    root.title("Autentificare")

    # Label pagina conectare
    label_3 = tk.Label(frame_main, text="Introduceți datele", font=("Verdana", 20), background="white",
                       width=20, height=2, justify="center")
    label_3.place(x=30, y=20)

    label_email = tk.Label(frame_main, text="Email:", font=("Verdana", 15), background="white",
                       width=5, height=1, justify="center")
    label_email.place(x=10, y=150)

    label_parola = tk.Label(frame_main, text="Parolă:", font=("Verdana", 15), background="white",
                       width=5, height=1, justify="center")
    label_parola.place(x=10, y=190)

    global entry_email, entry_parola
    entry_email = tk.Entry(frame_main, width=25,borderwidth=2, font=("Verdana", 12), relief="sunken")
    entry_email.place(x=100, y=155)
    entry_email.insert(0,"ana.blaj@gmail.com")
    entry_parola = tk.Entry(frame_main, width=25, font=("Verdana", 12), show="*", borderwidth=2, relief="sunken")
    entry_parola.place(x=100, y=195)
    entry_parola.insert(0, "anablaj.20")
    button_login = tk.Button(frame_main, text="Autentificare", background="white", font=("Verdana", 10), width=10, height=1,
                            borderwidth=4, command=lambda: login(root, background_label, frame_main))
    button_login.place(x=260, y=250)

    label_creare_cont = tk.Label(frame_main, text="Nu ai un cont? Creează-ți unul:", font=("Verdana", 9), background="white",
                            width=25, height=2, justify="center")
    label_creare_cont.place(x=10, y=300)

    button_creare_cont = tk.Button(frame_main, text="Înregistrare", background="white", font=("Verdana", 10), width=10, height=1,
                             borderwidth=4, command=creare_cont)
    button_creare_cont.place(x=260, y=300)

    global label_a
    label_a = tk.Label(frame_main, text="", font=("Verdana", 13), background="white",
                       width=30, height=2, justify="center")


def login(root, background_label,frame_main):
    email = entry_email.get()
    parola = entry_parola.get()
    connection=conectare()
    if email=="" or parola=="":
        raspuns="Nu ati completat toate campurile!"
        label_a.config(text=raspuns)
        label_a.place(x=40, y=350)
    elif connection is None:
        return "Eroare la conectare!"
    else:
        try:
            cursor=connection.cursor()

            # verificam daca email-ul si parola exista in tabela terapeut
            interogare="SELECT id_terapeut FROM terapeut WHERE email=%s AND parola=%s"
            cursor.execute(interogare,(email,parola))

            rezultat=cursor.fetchone()
            if rezultat is not None:
                id_terapeut=rezultat[0]

                frame_main.pack_forget()
                background_label.place_forget()
                entry_email.delete(0,tk.END)
                entry_parola.delete(0,tk.END)
                pagina_date(root, id_terapeut,frame_main, background_label)

            else:
                raspuns="Email sau parolă incorecte!"
                label_a.config(text=raspuns)
                label_a.place(x=40, y=350)

            cursor.close()
            connection.close()

        except Exception as e:
            print(f"Eroare la executarea interogării: {e}")
            return



