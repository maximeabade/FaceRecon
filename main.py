import os
import playsound
from capture import capture_et_reconnaissance
from learner import learn
import time


def main():
    try:
        learn()
        result = capture_et_reconnaissance()
        start_time = time.time()

        os.system("rm /home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/temp/*")

        if result:
            ## faire une pause de 20 secondes pour laisser le temps à la personne de rentrer
            
            ##playsound.playsound('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/bonjour.mp3', True)
            print("Bienvenue à la maison, Maxime !")


        elif not result:
            ##print("Intrus détecté")
            ## for 10 seconds play the alarm sound
            start_time = time.time()
            while time.time() - start_time < 10:
                ##playsound.playsound('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/intrus.mp3', True)
                print("Intrus détecté")    
            ## close the sound
            os.system("shutdown now")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error as needed, you might want to log it or take specific actions.
        # For example, you can add a delay before exiting to allow logs to be written.
        raise  # Re-raise the exception after handling (if needed)


main()
