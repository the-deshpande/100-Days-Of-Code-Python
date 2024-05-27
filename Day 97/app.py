from flask import Flask, render_template, request
import json

with open('static/items.json') as file:
    items = json.load(file)

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def homepage():
    if request.method == 'POST':
        total = 0
        for item in items:
            item['in_cart'] = False
        for _id in request.form.to_dict().keys():
            items[int(_id) - 1]['in_cart'] = True
            total += items[int(_id) - 1]['price']

        items_in_cart = [item for item in items if item['in_cart']]
        return render_template('cart.html', items=items_in_cart, total=total)
    return render_template('index.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
