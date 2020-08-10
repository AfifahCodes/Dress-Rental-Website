from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/merlin.html')
def home():
    return render_template("merlin.html") 

@app.route('/products.html')
def Products():
    return render_template("products.html") 

@app.route('/contact.html')
def ContactUS():
    return render_template("contact.html") 

@app.route('/login.html', methods=['GET','POST'])
def Login():
    return render_template("login.html") 

@app.route('/index.html')
def index():
    return render_template("index.html") 


@app.route('/profile/<username>')
def profile(username):
	return 'Hey there %s' % username

if __name__ == "__main__":
    app.run(debug=True)

