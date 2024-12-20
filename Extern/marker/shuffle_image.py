from PIL import Image
import random

def create_random_mosaic(image_path, output_path):
    # Charger l'image
    image = Image.open(image_path)

    # Vérifier que l'image est bien de 1024x1024
    if image.size != (1024, 1024):
        raise ValueError("L'image doit être de 1024x1024 pixels.")

    # Définir la taille des sous-carrés
    square_size = 256

    # Diviser l'image en une grille de 4x4
    squares = []
    for y in range(0, 1024, square_size):
        for x in range(0, 1024, square_size):
            square = image.crop((x, y, x + square_size, y + square_size))
            squares.append(square)

    # Mélanger les carrés de manière aléatoire
    random.shuffle(squares)

    # Créer une nouvelle image pour la mosaïque
    mosaic = Image.new('RGB', (1024, 1024))

    # Réassembler les carrés mélangés dans la nouvelle image avec rotation aléatoire
    index = 0
    for y in range(0, 1024, square_size):
        for x in range(0, 1024, square_size):
            rotated_square = squares[index].rotate(random.choice([0, 90, 180, 270]))
            mosaic.paste(rotated_square, (x, y))
            index += 1

    # Sauvegarder l'image résultante
    mosaic.save(output_path)
    print(f"Mosaïque aléatoire créée et sauvegardée sous {output_path}")

# Exemple d'utilisation
create_random_mosaic("redpanda.jpeg", "output_mosaic.png")
