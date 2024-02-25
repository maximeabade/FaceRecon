import os
import playsound
from capture import capture_et_reconnaissance
from learner import learn
import time

def main():
    learn()
    result = capture_et_reconnaissance()

    os.system("rm /home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/temp/*")

    if not result:
        ##print("Intrus détecté")
        ## for 10 seconds play the alarm sound
        start_time = time.time()
        while time.time() - start_time < 10:
            playsound.playsound('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/intrus.mp3', True)
            
        ## close the sound
        os.system("shutdown now")
        return
    else:
        ##print("Bienvenue à la maison, Maxime !")
        playsound.playsound('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/bonjour.mp3', True)

if __name__ == "__main__":
    main()
