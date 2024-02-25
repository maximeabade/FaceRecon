# FACE RECOGNITION

## Introduction
This project is a simple face recognition system using OpenCV and Python. The system uses the Haar Cascade Classifier to detect faces in the video feed. The detected faces are then compared with the faces in the database. If a match is found, the device keeps the screen unlocked. If no match is found, the device is down.

## Requirements
Python 3.10

To install the required packages, run the following command:
```pip install -r requirements.txt```

## Usage

I designed it to work on my laptop unix-based system, for each time my device is unlocked as a second layer of security. 

## Before running the program

PLEASE NOTE: The program needs training, I mean I need 158 images of my face to train the model, so make sure to have enough pictures of your head in the database folder, and in multiple angles and places, and with different facial expressions. 

## Running the program
Once the previous step is done you can launch the training. Make sure to have placed the images in ``` ./images/originals/ ``` and then run the following command:
```python3 detoureur.py```
to resize the images before training the model.

Then you can run the following command to train the model:
```python3 learner.py```

Finally, you can run the following command to start the face recognition system:
```python3 main.py```

Please note that in ```main.py```  the training program is relaunched to make sure the model is up to date.

You are free to add some reinforcement learning to the model, or to add some other features to the program, like a voice recognition system, or a fingerprint recognition system, or a password system, or a combination of all of them, but do care not to fall into the trap of overlearning.


## Paths

Make sure to correct the paths in the code, especially in the ```main.py``` file, and in the ```learner.py``` file, and in the ```detoureur.py``` file.

