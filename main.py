import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        # Specify the directory where you want to save the uploaded file
        upload_dir = '/home/pwk/upload'  # Update this with your desired directory

        # Ensure the directory exists or create it
        os.makedirs(upload_dir, exist_ok=True)

        # Save the uploaded file to the specified directory
        file.save(os.path.join(upload_dir, file.filename))

        # You can return a response here, such as a success message
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

