# 🥔 Potato Disease Classification - Deep Learning Project

A deep learning web application built with **TensorFlow** and **Flask** that classifies potato leaf diseases from uploaded images. The app predicts whether the leaf is:

- Early Blight 🍂  
- Late Blight 🧫  
- Healthy ✅


---

## 🚀 Features

- Image upload and real-time prediction  
- Clean, responsive frontend with **CSS styling**  
- Background image with **blur effect**  
- Trained on custom dataset using **Convolutional Neural Networks**  
- Outputs the disease class only (no probability/confidence)

---

## 🧠 Model Overview

- Input shape: `256x256x3`
- 6 Conv2D layers with ReLU and MaxPooling  
- Dense layers for final classification (Softmax)
- Model saved as `potatoes.h5`

---

## 🗂️ Project Structure

Potato-Disease-Classification/
│
├── app.py # Flask backend
├── potatoes.h5 # Trained model
├── requirements.txt # Python dependencies
│
├── static/
│ ├── css/
│ │ └── style.css # App styling
│ └── images/
│ └── logo.png # Background image
│
├── templates/
│ └── index.html # Main HTML page
│
└── README.md # Project description

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

### ✅ 1. Clone the repo

```bash
git clone https://github.com/aliahmad552/Potato-Disease-Classification.git
cd Potato-Disease-Classification
```

### ✅ 2. Install dependencies
```bash
pip install -r requirements.txt
```
### ✅ 3. Run the Flask app
```bash
python app.py
Now visit: http://127.0.0.1:5000
```
### 📂 Dataset
Custom dataset with three classes (Early Blight, Late Blight, Healthy)

Train/Validation/Test split handled using ImageDataGenerator

Image size: 256x256, normalized between 0-1

### 💻 Author
Ali Ahmad
BS Software Engineering – The Islamia University of Bahawalpur
GitHub: aliahmad552

