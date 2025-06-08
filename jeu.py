import tkinter as tk

# Créer la fenêtre
fenetre = tk.Tk()
fenetre.title("Déplacement avec ZQSD")

# Créer le canvas (la zone de dessin)
canvas = tk.Canvas(fenetre, width=400, height=400, bg="white")
canvas.pack()

# Créer un point (joueur) sous forme de cercle
joueur = canvas.create_oval(190, 190, 210, 210, fill="blue")

# Fonction pour déplacer le point
def deplacer(event):
    touche = event.keysym
    if touche == "z":
        canvas.move(joueur, 0, -10)
    elif touche == "s":
        canvas.move(joueur, 0, 10)
    elif touche == "q":
        canvas.move(joueur, -10, 0)
    elif touche == "d":
        canvas.move(joueur, 10, 0)

# Lier les touches au déplacement
fenetre.bind("<KeyPress>", deplacer)

# Lancer la boucle du jeu
fenetre.mainloop()
