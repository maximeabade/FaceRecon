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

        ##os.system("rm /home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/temp/*") ## mise en commentaire pour analyser les photos prises pdt la reconnaissance

        if result:            
            playsound.playsound('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/bonjour.mp3', True)
            print("Bienvenue à la maison, Maxime !")
            os.system("rm /home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/temp/*")

        elif not result:
            print("Intrus détecté")
            ## for 7 seconds play the alarm sound
            start_time = time.time()
            while time.time() - start_time < 5:
                playsound.playsound('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/intrus.mp3', True)
                print("Intrus détecté")    
                os.system("rm /home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/temp/*")
                ## os.system("shutdown now") ##in comments while at school for tests
            ## au lieu de shutdown, faire un lock
            os.system("gnome-screensaver-command -l")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error as needed, you might want to log it or take specific actions.
        # For example, you can add a delay before exiting to allow logs to be written.
        raise  # Re-raise the exception after handling (if needed)


main()
