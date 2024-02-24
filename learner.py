import os
import cv2
import numpy as np

path = './images/definitives/'

mesImages = []

myList = os.listdir(path)

print(myList)

# ANALYSIS OF THE PICTURES IN DATABASE

# CREATION de l'image moyenne depuis les images de la base de données

# Conversion en nuances de gris

# Taille spécifiée pour l'image moyenne
target_size = (1000, 1000)

# Créons une image comme tableau de pixels tous à 0 de taille 1000x1000
averageImage = np.zeros(target_size, np.float32)

# Compteur pour suivre le nombre total d'images
count = 0

# Boucle sur toutes les images
for img in myList:
    # Chemin d'accès à l'image
    current_image_path = os.path.join(path, img)

    # Lecture de l'image en nuances de gris
    current_image = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)

    # Ajout de l'image actuelle à l'image moyenne
    averageImage = cv2.add(averageImage, current_image.astype(np.float32))

    # Incrémentation du compteur
    count += 1

# Pour chaque pixel de l'image moyenne, on divise sa nuance de gris par le nombre total d'images
print(count)
averageImage = (averageImage / count).astype(np.uint8)
print(averageImage)

# Affichage ou enregistrement de l'image moyenne
cv2.imshow('Average Image', averageImage)
cv2.imwrite('averageImage.png', averageImage)
## enregistrement de l image dans le dossier ./images/definitives comme averageImage.jpg
cv2.imwrite('./images/definitives/averageImage.jpg', averageImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
