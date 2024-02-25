import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from detoureur import detect_and_extract_face, looper
from dotenv import load_dotenv 

## CHARGEMENT DU DOTENV
load_dotenv()
# path to mean image : 
path = os.getenv('meanImagePATH')

# taux de difference acceptable, en %
authorizedDelta = 15

# path to test images
# good images
pathGood = '/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/test/ACCEPTEES/'
# bad images
pathBad = '/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/test/REFUSEES/'

## ON COMMENCE PAR LES BONNES IMAGES
# on charge l'image moyenne
averageImage = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# on charge la liste des images
myListGood = os.listdir(pathGood)

## on cree un dataframe pour stocker les resultats
df_results_good = pd.DataFrame(columns=['image', 'error'])

'''
on va rendre ca sous forme de fonction
variables : Liste
            path
            
def compare_images(liste, path):
    bienClassees = 0
    malClassees = 0
    # on parcourt les images
    for img in liste:
        # on charge l'image
        current_image_path = os.path.join(path, img)
        current_image = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)

        # redimensionnement de l'image courante pour qu'elle ait la même taille que l'image moyenne
        current_image = cv2.resize(current_image, (averageImage.shape[1], averageImage.shape[0]))

        # conversion de l'image courante en type de données de l'image moyenne
        current_image = current_image.astype(averageImage.dtype)

        # Detection et extraction du visage
        detect_and_extract_face(current_image_path, current_image_path)

        # on charge l'image du visage extrait
        current_image_face = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)

        # redimensionnement de l'image du visage à 1000x1000 pixels
        current_image_face = cv2.resize(current_image_face, (1000, 1000))

        # on calcule la difference entre l'image moyenne et l'image du visage extrait
        diff = cv2.absdiff(averageImage, current_image_face)

        # Définir le masque ovale centré au centre de l'image
        mask = np.zeros_like(diff)
        center = (mask.shape[1] // 2, mask.shape[0] // 2)
        axes = (400, 300)  # Demi-longueur des axes (rayon pour x et y)
        cv2.ellipse(mask, center, axes, 0, 0, 360, 255, thickness=-1)

        # Appliquer le masque ovale à la différence
        diff_roi = cv2.bitwise_and(diff, diff, mask=mask)

        # Calculer la moyenne de la différence dans la région d'intérêt
        error_roi = np.mean(diff_roi)
        
            # Vérifier si l'erreur est inférieure au seuil autorisé
        if error_roi <= authorizedDelta:
            # print(f"{img} est ACCEPTABLE - Erreur : {error_roi}%")
            bienClassees += 1
        else:
            # print(f"{img} est NON ACCEPTABLE - Erreur : {error_roi}%")
            malClassees += 1

        # on stocke le resultat dans le dataframe
        df_results_good = df_results_good._append({'image': img, 'error': error_roi}, ignore_index=True)
        # on affiche le resultat
        # print(img, error_roi)
        
        ## on veut que si l image est correcte elle soit copiée dans le dossier ./images/definitives, avec verification ava,t de sy elle s y trouve ou non
        if error_roi <= authorizedDelta:
            if not os.path.exists('./images/definitives/' + img):
                cv2.imwrite('./images/definitives/' + img, current_image_face)

        

    # Matrice de confusion
    confusion_matrix = np.array([[bienClassees, malClassees], [0, 0]])
    print(confusion_matrix)
    

'''




bienClassees = 0
malClassees = 0
# on parcourt les images
for img in myListGood:
    # on charge l'image
    current_image_path = os.path.join(pathGood, img)
    current_image = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)

    # redimensionnement de l'image courante pour qu'elle ait la même taille que l'image moyenne
    current_image = cv2.resize(current_image, (averageImage.shape[1], averageImage.shape[0]))

    # conversion de l'image courante en type de données de l'image moyenne
    current_image = current_image.astype(averageImage.dtype)

    # Detection et extraction du visage
    detect_and_extract_face(current_image_path, current_image_path)

    # on charge l'image du visage extrait
    current_image_face = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)

    # redimensionnement de l'image du visage à 1000x1000 pixels
    current_image_face = cv2.resize(current_image_face, (1000, 1000))

    # on calcule la difference entre l'image moyenne et l'image du visage extrait
    diff = cv2.absdiff(averageImage, current_image_face)

    # Définir le masque ovale centré au centre de l'image
    mask = np.zeros_like(diff)
    center = (mask.shape[1] // 2, mask.shape[0] // 2)
    axes = (400, 300)  # Demi-longueur des axes (rayon pour x et y)
    cv2.ellipse(mask, center, axes, 0, 0, 360, 255, thickness=-1)

    # Appliquer le masque ovale à la différence
    diff_roi = cv2.bitwise_and(diff, diff, mask=mask)

    # Calculer la moyenne de la différence dans la région d'intérêt
    error_roi = np.mean(diff_roi)
    
        # Vérifier si l'erreur est inférieure au seuil autorisé
    if error_roi <= authorizedDelta:
        # print(f"{img} est ACCEPTABLE - Erreur : {error_roi}%")
        bienClassees += 1
    else:
        # print(f"{img} est NON ACCEPTABLE - Erreur : {error_roi}%")
        malClassees += 1

    # on stocke le resultat dans le dataframe
    df_results_good = df_results_good._append({'image': img, 'error': error_roi}, ignore_index=True)
    # on affiche le resultat
    # print(img, error_roi)
    
    ## on veut que si l image est correcte elle soit copiée dans le dossier ./images/definitives, avec verification ava,t de sy elle s y trouve ou non
    if error_roi <= authorizedDelta:
        if not os.path.exists('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/definitives/' + img):
            cv2.imwrite('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/definitives/' + img, current_image_face)

    

# Matrice de confusion
confusion_matrix = np.array([[bienClassees, malClassees], [0, 0]])
print(confusion_matrix)


## ON FAIT LA MEME AVEC LES MAUVAISES IMAGES

myListBad = os.listdir(pathBad)

# on cree un dataframe pour stocker les resultats
df_results_bad = pd.DataFrame(columns=['image', 'error'])

# Réinitialiser les compteurs
bienClassees = 0
malClassees = 0

# on parcourt les images
for img in myListBad:
    # on charge l'image
    current_image_path = os.path.join(pathBad, img)
    current_image = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)

    # redimensionnement de l'image courante pour qu'elle ait la même taille que l'image moyenne
    current_image = cv2.resize(current_image, (averageImage.shape[1], averageImage.shape[0]))

    # conversion de l'image courante en type de données de l'image moyenne
    current_image = current_image.astype(averageImage.dtype)

    # Detection et extraction du visage
    detect_and_extract_face(current_image_path, current_image_path)

    # on charge l'image du visage extrait
    current_image_face = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)

    # redimensionnement de l'image du visage à 1000x1000 pixels
    current_image_face = cv2.resize(current_image_face, (1000, 1000))

    # on calcule la difference entre l'image moyenne et l'image du visage extrait
    diff = cv2.absdiff(averageImage, current_image_face)

    mask = np.zeros_like(diff)
    center = (mask.shape[1] // 2, mask.shape[0] // 2)
    axes = (400, 300)  # Demi-longueur des axes (rayon pour x et y)
    cv2.ellipse(mask, center, axes, 0, 0, 360, 255, thickness=-1)

    # Appliquer le masque ovale à la différence
    diff_roi = cv2.bitwise_and(diff, diff, mask=mask)

    # Calculer la moyenne de la différence dans la région d'intérêt
    error_roi = np.mean(diff_roi)

    # Vérifier si l'erreur est inférieure au seuil autorisé
    if error_roi < authorizedDelta:
        # print(f"{img} est ACCEPTABLE - Erreur : {error_roi}%")
        malClassees += 1
    else:
        # print(f"{img} est NON ACCEPTABLE - Erreur : {error_roi}%")
        bienClassees += 1

    # on stocke le resultat dans le dataframe
    df_results_bad = df_results_bad._append({'image': img, 'error': error_roi}, ignore_index=True)
    # on affiche le resultat
    # print(img, error_roi)

# Matrice de confusion
confusion_matrix_bad = np.array([[0, 0], [bienClassees, malClassees]])
print("Matrice de confusion avec toutes les mauvaises:")
print(confusion_matrix_bad)


# MATRICE DE CONFUSION GLOBALE
confusion_matrix_globale = confusion_matrix + confusion_matrix_bad
print("Matrice de confusion globale:")
print(confusion_matrix_globale)