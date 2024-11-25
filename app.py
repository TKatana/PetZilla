from flask import Flask, render_template, url_for
import os
import random
app = Flask(__name__)
# Path to the images directory (this assumes you have a folder 'static/img/banner')
images_dir = os.path.join(app.root_path, 'static', 'img', 'banner')
mfp_img = os.path.join(app.root_path, 'static', 'img', 'mfp')


@app.route("/")
def index():
        # Get all image files with specific extensions
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
    images = [f for f in os.listdir(images_dir) if f.split('.')[-1].lower() in valid_extensions]

    # Select a random image
    random_image = random.choice(images)
    return render_template('index.html', random_image=random_image)

 


if __name__=="__main__":
    app.run(debug=True, use_reloader=False)