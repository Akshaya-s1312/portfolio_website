from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb+srv://akshaya131206_db_user:Akshaya1312*@cluster0.r25leqn.mongodb.net/")
db = client.portfolio_db

projects_collection = db.projects
messages_collection = db.messages

# Sample Project Data
if projects_collection.count_documents({}) == 0:
    projects_collection.insert_many([
        {
        "title": "AI Logistics Platform",
        "description": "Predict delivery delays and optimize routes using Machine Learning and Flask.",
        "tech": "Python, Flask, MongoDB, Machine Learning"
        },
        {   
        "title": "Credit Loan Approval System",
        "description": "Machine Learning model to predict loan approval eligibility based on customer data.",
        "tech": "Python, Machine Learning, Flask"
        },
        {
        "title": "Smart Stick For Blind People",
        "description": "AI powered smart stick designed to help visually impaired people detect obstacles and navigate safely.",
        "tech": "Artificial Intelligence, Sensors, Python"
        },
        {
        "title": "Personal Portfolio Website",
        "description": "Full stack portfolio website showcasing projects, skills and contact features.",
        "tech": "HTML, CSS, JavaScript, Flask, MongoDB"
        }
    ])

# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')

# ABOUT PAGE
@app.route('/about')
def about():
    return render_template('about.html')

# PROJECTS PAGE
@app.route('/projects')
def projects():
    all_projects = list(projects_collection.find({}, {'_id': 0}))
    return render_template('projects.html', projects=all_projects)

# CONTACT PAGE
@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        data = {
            "name": request.form['name'],
            "email": request.form['email'],
            "message": request.form['message']
        }

        messages_collection.insert_one(data)

        return """
            <h1 style='
            text-align:center;
            margin-top:250px;
            font-size:55px;
            font-style:italic;
            font-family:sans-serif;
            color:#11111;
            '>
            Message Sent Successfully 
            </h1>
        """

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)