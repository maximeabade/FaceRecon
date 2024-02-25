import os
import cv2
import numpy as np
import concurrent.futures

target_size = (1000, 1000)

def load_image(image_path):
    current_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return cv2.resize(current_image, target_size).astype(np.float32)

def learn():
    path = '/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/definitives/'
    
    try:
        os.remove(os.path.join(path, 'averageImage.jpg'))
    except FileNotFoundError:
        pass

    myList = os.listdir(path)
    
    target_size = (1000, 1000)
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        images = list(executor.map(load_image, [os.path.join(path, img) for img in myList]))

    averageImage = np.mean(images, axis=0).astype(np.uint8)

    center_x, center_y = target_size[1] // 2, target_size[0] // 2
    radius_x, radius_y = 300, 900
    mask = np.zeros_like(averageImage)
    cv2.ellipse(mask, (center_x, center_y), (radius_x, radius_y), 0, 0, 360, 255, thickness=cv2.FILLED)
    averageImage = cv2.subtract(averageImage, 90 * (mask / 255).astype(np.uint8))

    cv2.imwrite(os.path.join(path, 'averageImage.jpg'), averageImage)

learn()
