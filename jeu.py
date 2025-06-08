import tkinter as tk
from PIL import Image, ImageTk

# Fenêtre principale
root = tk.Tk()
root.title("Jeu Pokémon Lucas")

# Canvas pour dessiner
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Charger le sprite
sprite_sheet = Image.open("lucas.png")  # Assure-toi que ce nom est bon
sprite_sheet = sprite_sheet.resize((144, 192))  # redimensionne proprement si besoin
sprite_image = ImageTk.PhotoImage(sprite_sheet.crop((0, 0, 32, 32)))  # Premier sprite

# Position de départ
x, y = 250, 250
sprite = canvas.create_image(x, y, image=sprite_image)

# Déplacement avec ZQSD
def move(event):
    global x, y
    key = event.keysym
    if key == 'z':
        y -= 10
    elif key == 's':
        y += 10
    elif key == 'q':
        x -= 10
    elif key == 'd':
        x += 10
    canvas.coords(sprite, x, y)

# Bind des touches
root.bind("<Key>", move)

# Boucle principale
root.mainloop()
