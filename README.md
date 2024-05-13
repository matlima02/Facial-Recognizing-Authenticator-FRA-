# Facial-Recognizing-Authenticator (FRA)

Facial-Recognizing-Authenticator (FRA) is a simple authentication system that uses facial recognition technology to authenticate users. It is designed to work with a fake bank database, allowing users to access their bank accounts securely using their faces.

## Usage

To test the Facial-Recognizing-Authenticator, follow these steps:

1. Ensure you have Python installed on your system.

2. Install the required Python packages by running the following command: pip install -r requirements.txt

3. Put the photo of the person you want to authenticate in the "known_faces" directory. Make sure to update the name of the person in the filename and their bank information in the `app.py` script.

4. Run the Flask application by executing the following command: python app.py

5. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the Facial-Recognizing-Authenticator interface.

6. Click on the "Capture Your Photo" button to capture a photo using your webcam. The system will compare your face with the stored faces in the "known_faces" directory.

7. If your face is recognized, you will be granted access to the fake bank database, and your account balance will be displayed. Otherwise, access will be denied.

## Note

This is a basic implementation of a facial recognition authentication system using Flask and the face_recognition library. It is intended for educational purposes and demonstration only. For real-world applications, consider using more robust authentication methods and security measures.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 

