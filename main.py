import os
from capture import capture_et_reconnaissance

def main():
    """
    Fonction principale qui appelle la fonction d'apprentissage et la fonction de capture et reconnaissance.
    """

    # Exécution de la fonction d'apprentissage du script ./learner.py
    os.system("python3 ./learner.py")

    # Capture et reconnaissance faciale
    capture_et_reconnaissance()

    ## on vide ./images/temp/
    os.system("rm ./images/temp/*")
    
if __name__ == "__main__":
    main()
