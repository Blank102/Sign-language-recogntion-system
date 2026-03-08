AI Accessibility Assistant – Sign Language to Text
Overview

This project is an AI-based accessibility tool that converts sign language gestures into text in real time using a webcam.

The system uses a Convolutional Neural Network (CNN) trained on the ASL Alphabet Dataset to recognize hand signs. The application captures video from the webcam, processes the hand gesture, and displays the corresponding alphabet as text on the screen.

The goal of this project is to help improve communication accessibility for people who rely on sign language, especially in situations where others may not understand sign language.

Features

Real-time sign language recognition using a webcam

Converts detected gestures into text

Desktop dashboard built with Python

Basic sentence formation using detected alphabets

Options to clear text or save it to a file

Technologies Used

Python

TensorFlow / Keras

OpenCV

Tkinter (for the dashboard UI)

NumPy

How to Run the Project
1. Download the Project

Download or clone this repository to your computer.

You should have the following files in one folder:

dashboard_tk.py
asl_cnn_29_classes400.h5

(Your folder may contain additional files depending on the version.)

2. Install Required Libraries

Open Command Prompt and install the required libraries:

pip install tensorflow opencv-python pillow numpy
3. Navigate to the Project Folder

In Command Prompt, move to the folder where the project files are located.

Example:

cd C:\Users\YourName\Desktop\ASL_Project

Replace the path with the location of your folder.

4. Run the Program

Once you are inside the folder, run:

python dashboard_tk.py

This will open the application window.

How to Use the Application

Place your hand inside the green box shown on the screen.

Show a sign language alphabet.

The system will detect the gesture and convert it into text.

The detected characters will appear in the text area.

You can also:

Clear the text

Save the text to a file

Exit the application

Dataset

The model was trained using the ASL Alphabet Dataset, which contains images representing different sign language gestures.

Limitations

Accuracy may vary depending on lighting and background conditions.

Some gestures may look similar and may occasionally be misclassified.

Future Improvements

Improve accuracy using more training data

Add text-to-speech functionality

Improve gesture detection using hand tracking
