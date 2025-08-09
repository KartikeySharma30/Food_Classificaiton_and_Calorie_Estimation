# Food Classification and Calorie Estimation System

- Overview
This project is an innovative Food Classification and Calorie Estimation System designed to help users classify food items from images and estimate their calorie content using deep learning techniques. The system is built around a Convolutional Neural Network (CNN), which processes food images and classifies them into 34 predefined categories and each class contains around 2000 images of that food item and Specifies the Calories about that item. In addition, it leverages Google's Generative AI API to generate ingredient information, providing insights into the nutritional makeup of the classified food items. Furthermore, the system offers a voice-based output using text-to-speech (TTS) functionality,as it helps to enhance accessibility for users by also making it usable for visually imapared persons.
With the rise of health-conscious behavior, this project aims to offer a practical solution that can benefit fitness enthusiasts, dieticians, and anyone looking to monitor their food intake. It combines deep learning, interactive graphical interfaces, and AI-driven content generation to deliver an engaging user experience.

## How to Run :
- **File Exectution Order : FCCES -> save the model -> Main1.py**

## Features and Functionality
- **Food Image Classification**
The core of the project is a *Convolutional Neural Network (CNN)*, built using TensorFlow and Keras, trained on a large dataset of food images. The CNN can classify food items into one of 34 categories with a high degree of accuracy.
The model architecture includes several layers of convolutional filters and pooling layers that detect features in the image and make classifications based on learned patterns.

- **Calorie Estimation**
The system estimates the calorie content of the classified food items. A CSV file contains the calorie data mapped to the 34 food classes. Once an image is classified, the system retrieves the corresponding calorie value from the dataset and displays it to the user.

- **Ingredient Generation with Google Gemini AI**
Integrating the Google Gemini API to generate a short description of the food’s ingredients and nutritional information. After classifying the food, the system sends the name of the food item to the API, which returns a concise summary of its key ingredients and the nutrients it contains (fats, carbohydrates, proteins, etc.).

- **Text-to-Speech (TTS) Functionality**
For a more interactive experience, the system uses the pyttsx3 library to convert the text output into speech. This makes the application accessible for visually impaired users or those who prefer auditory feedback. The system reads out the food classification, calorie estimation, and generated ingredients.

- **Graphical User Interface (GUI)**
The system features a Tkinter-based GUI that allows users to upload images, classify them, and receive results in a user-friendly interface. The GUI includes buttons for uploading images, classifying food, estimating calories, and activating the TTS function. The results are displayed in a scrollable text widget, ensuring ease of use.

## Tech Stack
**1. Deep Learning Frameworks**
TensorFlow and Keras are used for building the CNN model. These frameworks provide efficient ways to construct, train, and deploy deep learning models for image classification.

**2. Computer Vision**
OpenCV is used to handle image processing tasks, such as reading and displaying the uploaded food images. It allows for seamless interaction between the user-uploaded files and the classification model.

**3. API Integration**
Google Gemini API is used to generate content related to food ingredients and nutritional components. This integration brings additional AI-driven insights into the system, providing users with a richer understanding of their food choices.

**4. Tkinter for GUI Development**
The GUI is created using Tkinter, a Python library for building graphical interfaces. It includes features like image upload, real-time classification, and results display, making the project user-friendly and interactive.

**5. Text-to-Speech Engine**
The pyttsx3 library is used to enable the TTS functionality, which converts the classification results and calorie estimation into speech. This adds a layer of accessibility and interaction to the system

## How It Works
**Image Upload**: The user uploads a food image via the Tkinter GUI.

**Preprocessing**: The image is preprocessed and resized to fit the input size required by the CNN model (150x150 pixels).

**Prediction**: The preprocessed image is fed into the CNN model, which predicts the class (i.e., the food item) based on learned patterns.

**Calorie Estimation**: Once the food item is classified, its calorie value is retrieved from a CSV file containing calorie data for all 34 classes.

**Ingredient Generation**: The system sends the classified food item’s name to Google Gemini API, which generates a summary of its ingredients and nutritional content.

**Display Results**: The GUI displays the classified food item, its calorie content, and the generated ingredients in a scrollable text box.

**Text-to-Speech**: The system reads out the results using TTS, providing auditory feedback to the user.

<img width="334" alt="Screenshot 2024-10-01 at 9 52 28 PM" src="https://github.com/user-attachments/assets/33eacf31-0059-4810-b708-8750931ef916">

<img width="288" alt="Screenshot 2024-10-01 at 9 52 54 PM" src="https://github.com/user-attachments/assets/f6ae50e3-a551-411c-a880-a9e5f4f977bb">

<img width="281" alt="Screenshot 2024-10-01 at 9 53 11 PM" src="https://github.com/user-attachments/assets/c581f086-fdfe-4d52-aa74-433b3f3a1668">

## Prerequisites:
Ensure you have Python 3.x installed along with the following libraries:

- TensorFlow
- Keras
- Tkinter
- OpenCV
- PIL (Python Imaging Library)
- pyttsx3
- pandas
- numpy
- google-generativeai

**Just ensure to put the API KEY in the main file for googles generativeai lib**

## Future Enhancements
**Expand the Food Dataset**: Incorporate additional food items to increase the variety of classifications.
**Mobile Integration**: Develop a mobile app version of the project for easier use on smartphones.
**Advanced Nutritional Breakdown**: Provide more detailed nutritional information (e.g., vitamins, minerals) for each food item.
**Meal Planning**: Add functionality to create meal plans based on calorie intake and user preferences.
