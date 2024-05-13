from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import face_recognition
import cv2

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Fake bank database (name, account balance, face encoding)
users = {
    'Bob': {'balance': 99999999, 'face_encoding': None},
    'Alice': {'balance': 1.3, 'face_encoding': None},
}

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the known face images and encode them
for name in users:
    image_path = f"known_faces/{name}.jpg"  # Path to the known face image
    known_image = face_recognition.load_image_file(image_path)
    users[name]['face_encoding'] = face_recognition.face_encodings(known_image)[0]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    # Ensure that the 'uploads' directory exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Initialize camera
    cap = cv2.VideoCapture(0)
    
    # Capture multiple frames
    for _ in range(10):  # Capture 10 frames
        ret, frame = cap.read()
        cv2.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], 'temp.jpg'), frame)

        # Load the captured image and encode it
        unknown_image = face_recognition.load_image_file('uploads/temp.jpg')
        face_locations = face_recognition.face_locations(unknown_image)

        # If at least one face is detected, break the loop
        if len(face_locations) > 0:
            break

    cap.release()

    if len(face_locations) > 0:
        # Encode the detected face
        unknown_encoding = face_recognition.face_encodings(unknown_image, known_face_locations=face_locations)[0]
        
        # Compare the face encoding with the known face encoding
        for name, data in users.items():
            result = face_recognition.compare_faces([data['face_encoding']], unknown_encoding)
            if result[0]:
                flash(f'Welcome, {name}! Your account balance is ${data["balance"]}')
                os.remove('uploads/temp.jpg')
                return redirect(url_for('index'))
        
        flash('Access denied! Your face is not recognized.')
    else:
        flash('No face detected in the captured image')

    os.remove('uploads/temp.jpg')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
