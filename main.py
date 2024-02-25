import os
from os import system
from capture import capture_et_reconnaissance
import playsound


def main():
    """
    Fonction principale qui appelle la fonction d'apprentissage et la fonction de capture et reconnaissance.
    """
    # Désactivation de la souris et du clavier
    language = 'fr'
    # Exécution de la fonction d'apprentissage du script ./learner.py
    os.system("python3 /home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/learner.py")

    # Capture et reconnaissance faciale
    result = capture_et_reconnaissance()
    ## print(result)
    ## on vide ./images/temp/
    try:
        os.system("rm /home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/images/temp/*")
        ## print("Suppression des images temporaires")
    except Exception as e:
        print(e)
        
    
    if(result == False):
        ## print("Intrus détecté")
        ## verrouiller l ecran
        os.system("gnome-screensaver-command --lock")
    else:
        print("Bienvue à la maison, Maxime !")
        ## lecture du message de bienvenue "bonjour.mp3"
        playsound.playsound('/home/max/Bureau/Work/Perso/PROJECTS/FaceRecon/bonjour.mp3', True)
        
        
if __name__ == "__main__":
    main()
