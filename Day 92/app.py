from flask import Flask, render_template, request
from form import ImageForm
from dotenv import dotenv_values
from flask_bootstrap import Bootstrap5
from PIL import Image
import numpy as np

env = dotenv_values()

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = env['SECRET_KEY']


@app.route('/', methods=['GET', 'POST'])
def homepage():
    image_name = 'sample.jpg'
    count = 10

    form = ImageForm()
    if form.validate_on_submit():

        img = request.files[form.image.name].read()
        image_name = str(form.image.data).split('\'')[1]
        count = form.num_of_colors.data
        with open(f'./static/{image_name}', 'wb') as file:
            file.write(img)

    colors = check_most_frequent(image_name, count)
    return render_template('index.html', form=form, image_name=image_name, colors=colors)


def check_most_frequent(image_name: str, count: int) -> list:
    image = np.array(Image.open(f"./static/{image_name}"))
    total_pixels = image.shape[0] * image.shape[1]

    line = np.zeros(image.shape[0:2], dtype=np.int64)

    # convert the 3 different numbers into one 9 digits number
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            line[i, j] = int('{:03d}{:03d}{:03d}'.format(image[i, j, 0], image[i, j, 1], image[i, j, 2]))

    line = line.flatten()
    # compare the numbers for top 10
    freq = sorted(list(np.asarray(np.unique(line, return_counts=True)).T), key=lambda x: x[1], reverse=True)

    # Convert int to proper 9 digits string
    line = [('{:09d}'.format(x[0]), x[1]*100/total_pixels) for x in freq[:count]]
    # Convert the 9 digit string to hex
    line = [('#{:02x}{:02x}{:02x}'.format(int(x[0][:3]), int(x[0][3:6]), int(x[0][6:])), x[1]) for x in line]

    return line


if __name__ == '__main__':
    app.run(debug=True)
