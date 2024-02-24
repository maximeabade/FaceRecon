
import cv2
import os
import time
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from detoureur import detect_and_extract_face  # Assurez-vous d'importer votre fonction de comparaison
from imutils.video import VideoStream
from dotenv import load_dotenv
from matplotlib import pyplot as plt




def capture_et_reconnaissance(authorizedDelta=20):
    """
    Fonction qui gère la capture d'images et la reconnaissance faciale.

    Args:
        authorizedDelta (float): Taux de différence acceptable (en %).

    Returns:
        None.
    """

    # On charge l'image moyenne
    load_dotenv()
    path = os.getenv('meanImagePATH')
    averageImage = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # On initialise la webcam
    vs = VideoStream(src=0).start()

    # On initialise le temps
    start = datetime.now()

    # On initialise le nombre de photos prises
    nbPhotos = 0

    # On initialise la variable de sortie
    output = False

    # On initialise les dataframes pour stocker les résultats
    df_results = pd.DataFrame(columns=['image', 'error'])

    def crop_center(image, target_height, target_width):
        h, w = image.shape
        start_h = (h - target_height) // 2
        start_w = (w - target_width) // 2
        return image[start_h:start_h + target_height, start_w:start_w + target_width]

    # On crée une fenêtre pour l'affichage en temps réel
    cv2.namedWindow("Webcam Feed", cv2.WINDOW_NORMAL)

    while datetime.now() - start < timedelta(seconds=10) and output == False:
        # On prend une photo
        frame = vs.read()

        # On convertit la photo en niveau de gris
        current_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Redimensionnement de l'image courante pour qu'elle ait la même taille que l'image moyenne
        current_image = cv2.resize(current_image, (averageImage.shape[1], averageImage.shape[0]))

        # Conversion de l'image courante en type de données de l'image moyenne
        current_image = current_image.astype(averageImage.dtype)

        # On sauvegarde l'image dans le dossier ./images/temp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        image_path = f'./images/temp/image_{timestamp}.png'
        cv2.imwrite(image_path, current_image)

        # On incrémente le nombre de photos prises
        nbPhotos += 1

        # Votre logique de comparaison ici
        detect_and_extract_face(image_path, image_path)  # Assurez-vous d'utiliser la bonne fonction
        current_image_face = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        current_image_face = cv2.resize(current_image_face, (1000, 1000))

        # Rogner au centre
        current_image_face = crop_center(current_image_face, 1000, 1000)

        diff = cv2.absdiff(averageImage, current_image_face)

        # Créer un masque ovale centré au centre de l'image
        mask = np.zeros_like(diff)
        center = (mask.shape[1] // 2, mask.shape[0] // 2)
        axes = (400, 300)  # Demi-longueur des axes (rayon pour x et y)
        cv2.ellipse(mask, center, axes, 0, 0, 360, 255, thickness=-1)

        # Appliquer le masque ovale à la différence
        diff_roi = cv2.bitwise_and(diff, diff, mask=mask)

        # Calculer la moyenne de la différence dans la région d'intérêt
        error_roi = np.mean(diff_roi)

        # Si c'est un match, on ajuste la variable de sortie
        if error_roi < authorizedDelta:
            print(f"Match trouvé avec une erreur de {error_roi:.2f} %")
            output = True

        # On stocke les résultats dans les dataframes
        df_results = df_results._append({'image': image_path, 'error': error_roi}, ignore_index=True)

        
        # On affiche la webcam en temps réel
        cv2.imshow("Webcam Feed", frame)
        cv2.waitKey(500)  #

    # On arrête la capture vidéo
    vs.stop()

    # On détruit la fenêtre à la fin du programme
    cv2.destroyAllWindows()

    # On affiche les résultats
    print(f"Nombre de photos prises : {nbPhotos}")

    # Optionnel : Enregistrement des résultats
    # df_results.to_csv('resultats.csv', index=False)

    # On analyse la matrice de confusion
    confusion_matrix_globale = df_results['error'].apply(lambda x: 0 if x <= authorizedDelta else 1).value_counts().to_numpy()
    confusion_matrix_globale = np.array([[confusion_matrix_globale[0], 0], [confusion_matrix_globale[1], 0]])

    print("Matrice de confusion globale:")
    print(confusion_matrix_globale)

