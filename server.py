from flask import Flask, render_template, url_for, request, redirect
import csv #replace with pandas or some shit, this shit's ass

app = Flask(__name__)

@app.route('/') #decorator: every time we hit '/' we print the text
def landing():
    return render_template('index.html') #Here, flask will automatically look for the 'templates' folder

@app.route("/favicon.ico")
#

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route("/blog/2024/designing_this_website")
def blog2 ():
    return 'forgor a lot of html'

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except: "Your request could not be processed."
    else: 
        return 'It would appear something went wrong.'
    
### General funcs from here
def write_to_db(data):
    with open("database.txt", mode = 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open("database.csv", mode = 'a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(database2, delimiter = ',', quotechar='$', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])