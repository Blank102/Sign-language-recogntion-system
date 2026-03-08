# AI Accessibility Assistant – Sign Language to Text

AI Accessibility Assistant is a desktop application that converts sign language gestures into text using a webcam. The system uses a trained deep learning model to recognize hand gestures from the ASL Alphabet dataset and display the detected letters on the screen, helping improve communication accessibility for people who rely on sign language.

## Features
- Real-time sign language recognition using a webcam  
- Desktop dashboard interface built with Python  
- Basic sentence formation from detected alphabets  
- Option to clear text or save it to a file  

## Tech Stack
- Python  
- TensorFlow / Keras  
- OpenCV  
- Tkinter  
- NumPy, Pillow  

## How to Run the Project
1. Download or clone this repository and place all the project files in the same folder on your computer.  
2. Install the required libraries using: `pip install tensorflow opencv-python pillow numpy`  
3. Open Command Prompt and navigate to the project folder using: `cd path_to_your_folder`  
4. Run the program using: `python dashboard.py`  

## How to Use
Place your hand inside the detection box shown on the screen and perform a sign language alphabet gesture. The system will recognize the gesture and display the corresponding letter in the text area. You can also clear the text, save it to a file, or exit the application.

## Dataset
The model was trained using the ASL Alphabet dataset, which contains images representing different sign language alphabet gestures.

## Future Improvements
- Improve accuracy with more training data  
- Add text-to-speech functionality  
- Improve gesture detection for better real-time performance
