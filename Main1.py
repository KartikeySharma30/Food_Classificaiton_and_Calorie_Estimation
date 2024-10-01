# Importing All the Libraries 
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox as mb
import cv2
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import os 
import google.generativeai as genai
import pyttsx3

genai.configure(api_key="#Upload Your Google Genrative API Key Here#")



# Loading the Trained Model
model = load_model('/Users/kartikeysharma/Desktop/Hanuman/Projects/Food Classification & Detection + Calorie Counter/New Model/food_classification_model1.h5')

# Global Variables 
image_f=None
all_txt=None





# Text To Speech Models
def text_to_speech(text=None):
    if text != None:

        engine = pyttsx3.init()
        text = text.replace('~', ' Approximately ').replace('-', ' to ').replace('kcal', ' Calories ')
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 125)
        engine.say(text)
        engine.runAndWait()

    # Checking If the Image is Uploaded or Not 
    else:
        print("No Image is Yet Uploaded Pls Upload")
        mb.showerror("Error","Please Upload Image First!")





# Two Line Generation About the food using Gemini API
def generate_ingredients(food):
    prompt="""You are ingredient specifier . You have to basically specify the ingredients used in the food.
    Provide information in around 50 words and just specify the ingredient and the diet (carbohydrates , fats , proteins
    ,etc.) covered in that food. Do not add bold characters or new line . Write in a just a paragraph .
    Specify in this format Cream(fats) and the food for which you have to specify the ingredients is : """
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+food)
    return response.text





# Uploading Image to the Interface and Storing Refference for Processing
def upload_image():
    global image_f
    file_path = filedialog.askopenfilename(title="Select the Image to Upload")
    img = cv2.imread(file_path) # Using OpenCV for Reading the Image File
    display_image(img) # Displaying the Image into Tkinter Window
    image_f=file_path   #         |
                        #         |
                        #         |
                        #         |
                        #         v
# Function For Displaying the Image in Tkinter Window
def display_image(img):
    # Convert OpenCV image to PIL format and display in Tkinter
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_pil = img_pil.resize((250,300))
    img_tk = ImageTk.PhotoImage(img_pil)
    box.create_image(0, 0, anchor='nw', image=img_tk) # Adding the Picture to the Canvas 
    box.image = img_tk
    




# PreProcessing the Uploaded Image to Send the Image to the Model's Format  
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))  # Resize to 150x150
    img_array = image.img_to_array(img)  # Convert image to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize pixel values to 0-1
    return img_array





# Model 
def predict_image(image_f):
    
    if image_f!=None:
        preprocessed_img=preprocess_image(image_f)
        prediction = model.predict(preprocessed_img)
        predicted_cls=np.argmax(prediction,axis=1)
        cal_data = pd.read_csv("/Users/kartikeysharma/Desktop/Hanuman/Projects/Food Classification & Detection + Calorie Counter/New Model/Food and Their Calorie(Sheet1).csv")
        r1= cal_data['Food Item Name'].iloc[predicted_cls].item()
        r2= cal_data['Calorie'].iloc[predicted_cls].item()
        ai_gen_txt=generate_ingredients(r1) # Generating Text for Food about its - Ingredients
        txt_w.tag_configure("left", justify="left", lmargin1=10, lmargin2=10)
        txt_w.insert(tk.END,f" \n\nFood Item   : {r1}\nCalories    : {r2}\n\nIngredients :\n{ai_gen_txt}","left")

        # All the Text Consolidated Together to Pass it to the text to speech model 
        global all_txt
        all_txt="Food Item "+r1+"Calories "+r2+"Ingredients "+ai_gen_txt 
        
    # Checking If the Image is Uploaded or Not     
    if image_f==None:
        print("No Image is Yet Uploaded Pls Upload")
        mb.showerror("Error","Please Upload Image First!")





# For Perfoming Exit from the Application
def exit():
    mb.showinfo("Thank You","Thank You For Choosing us for the Health!")
    main.destroy()




# Main Window Creation with All its Element
# Main
main = tk.Tk()
main.geometry("650x500")
main.maxsize(650,500)
main.minsize(650,500)
main.title("Food Classification & Calorie Estimation")
bgImg=Image.open("/Users/kartikeysharma/Desktop/Hanuman/Projects/Food Classification & Detection + Calorie Counter/New Model/Background Images and Test Images /Bg9.jpeg")
bgImg = bgImg.resize((650, 500))
bgImgTk = ImageTk.PhotoImage(bgImg)
bglab=tk.Label(main,image=bgImgTk).place(x=0,y=0,relwidth=1,relheight=1)
main.configure(bg=bglab)

# Image Uploading Box
box = tk.Canvas(main,width=250,height=300,bg='grey')
box.place(x=50,y=50)
box.create_text(130,150,text="Upload Image")

# Output Box 
scb=tk.Scrollbar(main)
txt_w=tk.Text(main,height=23,width=35,bg='white',fg='black',wrap='word',yscrollcommand=scb.set)
txt_w.place(x=350,y=50)
scb.place(x=598,y=50,height=304)

# Buttons 
uploadimg_btn = tk.Button(main,text = 'Upload Plate Image',command=upload_image,borderwidth=0, highlightthickness=0,padx=20).place(x=90,y=400)
classify_btn=tk.Button(main,text="Classify & Estimate Calorie",command=lambda:predict_image(image_f),borderwidth=0, highlightthickness=0).place(x=370,y=400)
p=tk.PhotoImage(file="/Users/kartikeysharma/Desktop/Hanuman/Projects/Food Classification & Detection + Calorie Counter/l1.png")
listen_btn=tk.Button(main,text="Listen Report" , image=p,command=lambda:text_to_speech(all_txt),borderwidth=0, highlightthickness=0).place(x=580,y=400)
exit_btn = tk.Button(main,text="Exit",command=exit,borderwidth=0, highlightthickness=0).place(x=300,y=450)

main.mainloop()
