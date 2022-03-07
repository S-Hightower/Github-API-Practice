from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        login = request.form['login']

        github_url = requests.get(
            f'https://api.github.com/users/{login}')

        userData = github_url.json()

        avatar_url = (userData['avatar_url'])
        bio = (userData['bio'])
        name = (userData['name'])

    return render_template('index.html', avatar_url=avatar_url, bio=bio, name=name, login=login)

if __name__=="__main__":
    app.run(debug=True)