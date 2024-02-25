import os
import cv2
import numpy as np

def learn():

    path = '/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/definitives/'

    try:
        os.remove(path + 'averageImage.jpg')
    except:
        pass

    myList = os.listdir(path)

    print(myList)

    target_size = (1000, 1000)
    averageImage = np.zeros(target_size, np.float32)
    count = 0

    for img in myList:
        current_image_path = os.path.join(path, img)
        current_image = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)

        # Resize current_image to match the target size
        current_image = cv2.resize(current_image, target_size)

        averageImage = cv2.add(averageImage, current_image.astype(np.float32))
        count += 1

    averageImage = (averageImage / count).astype(np.uint8)

    # Create a dark oval mask
    mask = np.zeros(target_size, np.uint8)
    center = (target_size[1] // 2, target_size[0] // 2)
    axes = (int(target_size[1] * 0.4), int(target_size[0] * 0.6))
    cv2.ellipse(mask, center, axes, 0, 0, 360, 255, -1)

    # Apply the mask to the average image
    darkenedImage = cv2.bitwise_and(averageImage, averageImage, mask=mask)

    # Save the result
    cv2.imwrite('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/definitives/averageImage.jpg', darkenedImage)

learn()
