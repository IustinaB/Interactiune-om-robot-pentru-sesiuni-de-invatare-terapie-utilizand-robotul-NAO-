import tkinter as tk
from fereastra_autentificare import pagina_autentificare

def pagina_principala():
    root = tk.Tk()
    root.title("NAO")
    root.geometry('1200x700')
    root.configure(bg="white")
    root.bind('<Escape>', lambda event: root.destroy())

    # Setare imagine de fundal
    image_path = "fundalprincipal.png"
    background_image = tk.PhotoImage(file=image_path)

    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)

    frame_main = tk.Frame(root, bg="white", width=400, height=400)
    frame_main.pack(side=tk.RIGHT, pady=20, padx=200)

    # Label-uri fereastra principala
    label_1 = tk.Label(frame_main, text="Bine ați venit!", font=("Verdana", 30), background="white")
    label_1.place(x=65, y=10)

    label_2 = tk.Label(frame_main, text="Să începem!", font=("Verdana", 27), background="white")
    label_2.place(x=80, y=140)

    # Buton next
    button_next = tk.Button(frame_main, text="Spre pagina de\nautentificare", background="white", font=("Verdana", 12), width=13, height=3,
                            borderwidth=4, command=lambda: pagina_autentificare(root, frame_main, background_label))
    button_next.place(x=120, y=270)

    root.mainloop()

if __name__ == "__main__":
    pagina_principala()
