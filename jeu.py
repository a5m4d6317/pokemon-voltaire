import tkinter as tk

# Crée la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Compteur de clics")
fenetre.geometry("300x200")

# Variable pour compter les clics
nombre_de_clics = 0

# Fonction qui s'exécute quand on clique sur le bouton
def cliquer():
    global nombre_de_clics
    nombre_de_clics += 1
    label.config(text=f"Nombre de clics : {nombre_de_clics}")

# Label pour afficher le nombre de clics
label = tk.Label(fenetre, text="Nombre de clics : 0", font=("Arial", 16))
label.pack(pady=20)

# Le bouton qui déclenche le compteur
bouton = tk.Button(fenetre, text="Clique ici 👆", command=cliquer, font=("Arial", 14))
bouton.pack(pady=10)

# Lance l'interface
fenetre.mainloop()
