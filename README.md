# Potato Disease Classification Web App

This is a **Potato Disease Classification Web App** built using **Flask** and **Deep Learning**. The app allows users to upload an image of a potato leaf and predict whether the leaf is **healthy** or has a disease such as **Early Blight** or **Late Blight**.

## Features
- Upload an image of a potato leaf for disease classification.
- Predict whether the leaf is healthy or has a disease.
- Display the uploaded image along with the predicted result.
- Beautiful user interface with a blurry background image of the potato leaf.

## Project Structure

potato_disease_classification/
├── app.py # Flask backend file
├── static/
│ ├── images/
│ │ └── logo.png # Logo image used as background
│ └── uploads/ # Folder to store uploaded images
│ └── css/
│ └── style.css # Styling for the web app
├── templates/
│ └── index.html # Frontend HTML for the app
├── potatoes.h5 # Trained model file
├── requirements.txt # Python dependencies
└── README.md # This README file

bash
Copy
Edit

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd potato_disease_classification
Install dependencies:

It's recommended to create a virtual environment for your project. You can install the required libraries using pip:

bash
Copy
Edit
pip install -r requirements.txt
Alternatively, you can manually install the dependencies:

bash
Copy
Edit
pip install flask tensorflow numpy werkzeug
Place the model file:

Make sure you have the trained model file potatoes.h5 in the root directory of the project. This file is used for prediction.

Run the Flask app:

Once everything is set up, you can run the Flask application with the following command:

bash
Copy
Edit
python app.py
This will start the web server, and you can access the app in your browser at http://127.0.0.1:5000/.

Usage
Navigate to http://127.0.0.1:5000/ in your browser.

Upload a potato leaf image by clicking the "Choose File" button.

After uploading the image, the model will predict whether the leaf is Healthy, has Early Blight, or Late Blight.

The prediction will be displayed along with the uploaded image.

Example Image (Uploaded and Predicted)
Example of the uploaded image and predicted result will appear below the form after submitting the file.

Project Dependencies
The project uses the following Python libraries:

Flask: Web framework for creating the web app.

TensorFlow: Deep learning library used for the model.

NumPy: For numerical operations.

Werkzeug: Used for secure filename handling.

ImageDataGenerator: For data augmentation and image preprocessing during model training.

File Descriptions
app.py: Main Flask backend file which handles image upload, preprocessing, prediction, and rendering results.

potatoes.h5: The trained model file that is used for making predictions on the uploaded potato leaf image.

static/images/logo.png: Background image used for the app's design.

static/uploads/: Folder where the uploaded images are temporarily stored.

static/css/style.css: Contains styles for the webpage (including the background, buttons, etc.).

templates/index.html: Frontend HTML that displays the form for image upload and results.

requirements.txt: List of Python libraries required for the project.

Contributing
Feel free to fork the repository, make improvements, or report any issues. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy
Edit

---

### 🚀 Instructions:

1. **Replace `<repository_url>`** with your actual GitHub repository URL (if hosted on GitHub).
2. **Add the correct `LICENSE` file** (if you want to specify any license for the project).
3. **Update** the model classes in the readme (`Early Blight`, `Healthy`, and `Late Blight`) if your model's class names are different.

Aap is `README.md` ko apne GitHub repository ya local project mein directly copy kar sakte h
