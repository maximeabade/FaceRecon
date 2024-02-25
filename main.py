import os
import playsound
from capture import capture_et_reconnaissance
from learner import learn
import time

def main():
    language = 'fr'
    learn()
    result = capture_et_reconnaissance()

    os.system("rm ./images/temp/*")

    if not result:
        print("Intrus détecté")
        ## for 10 seconds play the alarm sound
        start_time = time.time()
        while time.time() - start_time < 10:
            playsound.playsound('./intrus.mp3', True)
        ## close the sound
        
        return
    else:
        print("Bienvenue à la maison, Maxime !")
        playsound.playsound('./bonjour.mp3', True)

if __name__ == "__main__":
    main()
