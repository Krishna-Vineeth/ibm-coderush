from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/sofa')
def sofa():
    return render_template('sofa.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/electronics')
def electronics():
    return render_template('electronics.html')

@app.route('/sports')
def sports():
    return render_template('sports.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')




if __name__ == '__main__':
    app.run(debug=True)