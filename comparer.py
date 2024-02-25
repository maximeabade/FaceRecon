import os
import cv2
import numpy as np
import pandas as pd
import concurrent.futures
from detoureur import detect_and_extract_face
from dotenv import load_dotenv 

load_dotenv()
path = os.getenv('meanImagePATH')
authorizedDelta = 20

averageImage = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
pathGood = '/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/test/ACCEPTEES/'
pathBad = '/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/test/REFUSEES/'

def crop_center(image, target_height, target_width):
    h, w = image.shape
    start_h = (h - target_height) // 2
    start_w = (w - target_width) // 2
    return image[start_h:start_h + target_height, start_w:start_w + target_width]


def compare_image(img):
    current_image_path = os.path.join(pathGood, img)
    current_image = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)
    current_image = cv2.resize(current_image, (averageImage.shape[1], averageImage.shape[0]))
    current_image = current_image.astype(averageImage.dtype)

    detect_and_extract_face(current_image_path, current_image_path)
    current_image_face = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)
    current_image_face = cv2.resize(current_image_face, (1000, 1000))
    
    # Ajustez ici pour assurer que les deux images ont la même forme
    current_image_face = crop_center(current_image_face, 1000, 1000)

    diff = np.abs(averageImage - current_image_face)

    center = (diff.shape[1] // 2, diff.shape[0] // 2)
    axes = (400, 300)
    mask = np.zeros_like(diff)
    cv2.ellipse(mask, center, axes, 0, 0, 360, 255, thickness=-1)
    diff_roi = cv2.bitwise_and(diff, diff, mask=mask)
    error_roi = np.mean(diff_roi)

    if error_roi <= authorizedDelta:
        bienClassees += 1
    else:
        malClassees += 1

    df_results_good = df_results_good.append({'image': img, 'error': error_roi}, ignore_index=True)

    if error_roi <= authorizedDelta and not os.path.exists('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/definitives/' + img):
        cv2.imwrite('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/definitives/' + img, current_image_face)

myListGood = os.listdir(pathGood)
df_results_good = pd.DataFrame(columns=['image', 'error'])
bienClassees, malClassees = 0, 0

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(compare_image, myListGood)

confusion_matrix = np.array([[bienClassees, malClassees], [0, 0]])
print(confusion_matrix)