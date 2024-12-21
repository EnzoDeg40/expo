from PIL import Image
import random
import os

def crop_and_resize_to_square(image, size):
    # Rendre l'image carrée en la recadrant
    width, height = image.size
    if width != height:
        min_dim = min(width, height)
        left = (width - min_dim) // 2
        top = (height - min_dim) // 2
        right = left + min_dim
        bottom = top + min_dim
        image = image.crop((left, top, right, bottom))
    # Redimensionner à la taille spécifiée
    image = image.resize((size, size))
    return image

def create_random_mosaic(image_path, output_path):
    # Charger l'image
    image = Image.open(image_path)

    # Recadrer et redimensionner l'image pour qu'elle soit 1024x1024
    image = crop_and_resize_to_square(image, 1024)

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

def get_all_images_from_folder(folder_path):
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(supported_formats)]
    return images

# Exemple d'utilisation
textures_folder = "../textures"
images = get_all_images_from_folder(textures_folder)
print(f"Images trouvées : {images}")

for image_path in images:
    output_path = os.path.join(textures_folder, f"mosaic_{os.path.basename(image_path)}")
    create_random_mosaic(image_path, output_path)