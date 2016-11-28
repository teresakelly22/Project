from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')
	
@app.route('/home')
def Home():
	return render_template('home.html')

@app.route('/about')
def About():
	return render_template('about.html')

@app.route('/prototype')
def Prototype():
	return render_template('prototype.html')
	
@app.route('/contact')
def Contact():
	return render_template('contact.html')
	
@app.route('/map')
def Map():
	return render_template('map.html')
	
if __name__ == "__main__":
    app.run()




