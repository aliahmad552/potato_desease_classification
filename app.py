import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Flask app setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load model and class names
model = load_model('potatoes.h5')
class_names = ['Early Blight', 'Late Blight', 'Healthy']  # Update this list according to your model

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Prediction route
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    image_path = None
    error = None

    if request.method == 'POST':
        file = request.files.get('image')
        if file:
            try:
                filename = secure_filename(file.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(image_path)

                # Preprocess image
                img = image.load_img(image_path, target_size=(256, 256))
                img_array = image.img_to_array(img)
                img_array = img_array / 255.0
                img_array = np.expand_dims(img_array, axis=0)

                # Make prediction
                preds = model.predict(img_array)
                predicted_class = class_names[np.argmax(preds[0])]
                prediction = predicted_class

            except Exception as e:
                error = f"Error processing image: {str(e)}"

    return render_template('index.html', prediction=prediction, image_path=os.path.basename(image_path) if image_path else None, error=error)

if __name__ == '__main__':
    app.run(debug=True)
