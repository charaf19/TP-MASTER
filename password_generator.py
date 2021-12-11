from random import randint, choice
from tkinter import *
import string


def generate_pasword():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# creation de la fenetre
window = Tk()
window.title("generateur de mdp")
window.geometry("720x480")
window.iconbitmap("superhero.ico")
window.config(background="#4065A4")
# creation de la frame principale
frame = Frame(window, bg="#4065A4")
# creation d'image
width = 300
height = 500
image = PhotoImage(file="password.png")
canvas = Canvas(frame, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creer une sous boite
right_frame = Frame(frame, bg="#4065A4")

# creer un titre
label_title = Label(right_frame, text="mot de passe", font=("helvetica, 20"), bg="#4065A4", fg='white')
label_title.pack()
# creer un champ d'enteré input
password_entry = Entry(right_frame, font=("helvetica, 20"), bg="white", fg='black')
password_entry.pack()
# on place la sous boite à droite de la frame principal
right_frame.grid(row=0, column=1, sticky=W)
# Creer un boutton
generate_password_button = Button(right_frame, text="Générer", font=("helvetica, 20"), bg="#4065A4", fg='white',command=generate_pasword)
generate_password_button.pack(fill=X)
# afficher la frame
frame.pack(expand=YES)
#creation d'une barre de menu
menu_bar= Menu(window)
#creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="nouveau",command=generate_pasword)
file_menu.add_command(label="Quitter",command=window.quit)
menu_bar.add_cascade(label="fichier",menu=file_menu)

#configurer notre fenetre pour ajouter cette menu bar

window.config(menu=menu_bar)
# AFFICHER LA FENETRE
window.mainloop()
