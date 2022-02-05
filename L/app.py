from flask import Flask, render_template, request, redirect, url_for
# Initialize the Flask application
app = Flask(__name__)
 
 
@app.route('/')
def index():
   return render_template('log_in.html')
    
@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST' and request.form['txtemail'] == 'nicole@gmail.com' and request.form['txtpass'] == 'nicole123' :
      return redirect(url_for('success'))
   else:
      return redirect(url_for('errorlogin'))
 
@app.route('/success')
def success():
   return '<h1>logged in successfully</h1>'
  
@app.route('/errorlogin')
def errorlogin():
   return '<h1>Bad Credentials. Please login again <a href = "/">login</a></h1>'
    
if __name__ == '__main__':
   app.run(debug = True)