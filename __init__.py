import os

from flask import Flask, render_template, request, redirect

import Flask1.HowdyHackTogether



def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_mapping(
            SECRET_KEY='dev')#todo chagne dev to random key

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/')
    def Profiles():
        return render_template('ExtraSecret.html')

    @app.route('/', methods=['GET','POST'])
    def prompt():
        personsLog=''
        if request.method == 'POST':
            personsToGen=int(request.form['numPersons'])
            password= request.form['passArg']
            if(password==''):
                personsLog=personsLog + HowdyHackTogether.generateAccount(personsToGen)
            else:
                personsLog=personsLog + HowdyHackTogether.generateAccountP(personsToGen, password)


        return render_template('persons.html',persons=personsLog)

    return app

            

