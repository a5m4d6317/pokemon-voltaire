import tkinter as tk
from PIL import Image, ImageTk

# --- Fenêtre ---
fenetre = tk.Tk()
fenetre.title("Lucas Simulator")
canvas = tk.Canvas(fenetre, width=300, height=300, bg="white")
canvas.pack()

# --- Sprite ---
sprite_sheet = Image.open("lucas.png")

# Taille d’un sprite (tu peux vérifier en zoomant sur l’image)
sprite_width = 32
sprite_height = 32

# Frame du perso vu de face, en position debout
# (ligne 0 = vers le haut, ligne 1 = droite, ligne 2 = bas, ligne 3 = gauche)
frame = sprite_sheet.crop((0, 2 * sprite_height, sprite_width, 3 * sprite_height))
sprite = ImageTk.PhotoImage(frame)

# Ajouter le sprite au canvas
sprite_id = canvas.create_image(150, 150, image=sprite)

# --- Mouvements ---
def deplacer(dx, dy):
    canvas.move(sprite_id, dx, dy)

def bouger(event):
    touches = {
        "z": (0, -10),
        "s": (0, 10),
        "q": (-10, 0),
        "d": (10, 0),
    }
    touche = event.char.lower()
    if touche in touches:
        dx, dy = touches[touche]
        deplacer(dx, dy)

fenetre.bind("<Key>", bouger)
fenetre.mainloop()
