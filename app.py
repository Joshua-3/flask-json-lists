from flask import Flask, render_template
import os
import json

app = Flask(__name__)

JSON_FOLDER = 'json_files'

@app.route('/')
def index():
    try:
        elements = []

        for filename in os.listdir(JSON_FOLDER):
            if filename.endswith('.json'):
                file_path = os.path.join(JSON_FOLDER, filename)

                with open('./'+ file_path, 'r') as file:
                    data = json.load(file)

                element = {
                    'image': data.get('image', ''),
                    'heading': data.get('heading', ''),
                    'description': data.get('description', ''),  # New field
                    'link': data.get('link', '')
                }
                

                elements.append(element)

        return render_template('index.html', elements=elements)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(debug=True)