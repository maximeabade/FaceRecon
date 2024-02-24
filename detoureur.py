import cv2
import os
import imghdr


def detect_and_extract_face(image_path, output_path):
  """
  Détecte un visage sur une photo et l'extrait en une image PNG de 1000x1000 pixels.

  Args:
      image_path (str): Le chemin d'accès à la photo.
      output_path (str): Le chemin d'accès où l'image du visage sera sauvegardée.

  Returns:
      None.
  """

  # Chargement du modèle de détection de visage
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

  # Chargement de l'image
  image = cv2.imread(image_path)

  # Conversion de l'image en niveaux de gris
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Détection des visages
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

  # Si aucun visage n'est détecté, on quitte la fonction
  if len(faces) == 0:
    # print("Aucun visage détecté.")
    return

  # On extrait le premier visage détecté
  (x, y, w, h) = faces[0]

  # On agrandit la zone du visage pour s'assurer d'avoir une marge suffisante
  margin = 0.2
  x1 = int(x - margin * w)
  y1 = int(y - margin * h)
  x2 = int(x + (1 + margin) * w)
  y2 = int(y + (1 + margin) * h)

  # On vérifie que la zone du visage est dans l'image
  if x1 < 0 or y1 < 0 or x2 > image.shape[1] or y2 > image.shape[0]:
    print("Le visage est trop près du bord de l'image.")
    return

  # On extrait la zone du visage
  face_image = image[y1:y2, x1:x2]

  # Redimensionnement de l'image du visage à 1000x1000 pixels
  face_image = cv2.resize(face_image, (1000, 1000))

  # Enregistrement de l'image du visage
  cv2.imwrite(output_path, face_image)

  # print("Visage extrait avec succès.")



def looper(input_path, output_path):
    # Vérifie que le dossier de sortie existe, sinon le crée
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Liste des images dans le dossier
    images = [f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f)) and imghdr.what(os.path.join(input_path, f))]

    # Boucle sur toutes les images
    for image in images:
        # Chemin d'accès à l'image
        image_path = os.path.join(input_path, image)

        # Chemin d'accès où l'image du visage sera sauvegardée
        output_file = os.path.join(output_path, image)

        # Détection et extraction du visage
        detect_and_extract_face(image_path, output_file)

# Appel de looper
looper('./images/originals/', './images/definitives/')
