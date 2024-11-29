from flask import Flask, render_template, url_for, jsonify, request
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

 
# Sample product data
products_data = {
    'all': [
        {'name': 'Toy Car', 'image': 'images/toy_car.jpg', 'availability': 'In Stock', 'price': 500},
        {'name': 'Toy Train', 'image': 'images/toy_train.jpg', 'availability': 'Out of Stock', 'price': 800},
        {'name': 'Toy Doll', 'image': 'images/toy_doll.jpg', 'availability': 'In Stock', 'price': 400}
    ],
    'toys': [
        {'name': 'Toy Car', 'image': 'images/toy_car.jpg', 'availability': 'In Stock', 'price': 500},
        {'name': 'Toy Train', 'image': 'images/toy_train.jpg', 'availability': 'Out of Stock', 'price': 800}
    ],
    'medicine': [
        {'name': 'Pain Reliever', 'image': 'images/pain_reliever.jpg', 'availability': 'In Stock', 'price': 150},
        {'name': 'Cough Syrup', 'image': 'images/cough_syrup.jpg', 'availability': 'In Stock', 'price': 250}
    ]
}

@app.route('/get_products')
def get_products():
    category = request.args.get('category', 'all')  # Default to 'all' if no category is provided
    if category not in products_data:
        return jsonify({'error': 'Category not found'}), 404

    # Return the product data for the selected category
    return jsonify(products_data[category])

if __name__=="__main__":
    app.run(debug=True, use_reloader=False)