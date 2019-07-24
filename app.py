import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myTestDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:B4dmintonC0d3@myfirstcluster-tdray.mongodb.net/myTestDB?retryWrites=true&w=majority'

mongo = PyMongo(app)




#@app.route('/get_tasks')
#def get_tasks():
#    return render_template('tasks.html', tasks=mongo.db.tasks.find())

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('tasks.html', tasks=mongo.db.myFirstMDB.find())



@app.route('/upload')
def upload():
    return '''
        <form method="POST" action="/create" enctype="multipart/form-data">
            <input type="text" name="username">
            <input type="file" name="profile_image">
            <input type="submit">
        </form>
    '''

@app.route('/create', methods=['POST'])
def create():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users.insert({'username' : request.form.get('username'), 'profile_image_name' : profile_image.filename})
    
    return 'Done!'

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

@app.route('/profile/<username>')
def profile(username):
    user = mongo.db.users.find_one_or_404({'username' : username})
    return f'''
        <h1>{username}</h1>
        <img src="{url_for('file', filename=user['profile_image_name'])}">
    '''



# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if __name__ == '__main__':
    app.run(debug=True)

# The above is required for local development but
# needs to be commented out to run in Heroku and replaced with the below code

#if __name__ == '__main__':
#    from os import environ
#    app.run(debug=False, host='0.0.0.0',port=environ.get("PORT", 5000))    