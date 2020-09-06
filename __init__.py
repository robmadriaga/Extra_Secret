import os

from flask import Flask

import HowdyHackTogether

def create_app(test_config=None):

    app =Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev')

    if test_config is None:

        app.config.form_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import generator
    app.register_blueprint(generator.bp)

    @app.route('/generator', methods=('GET', 'POST'))
    def prompt():
        if request.method == 'POST':
            personsToGen=int(request.json['numPersons'])
            password= request.json['passArg']
            personsLog=''
            if(password==''):
                personsLog=personsLog + generateAccount(personsToGen)
            else:

                personsLog=personsLog + generateAccountP(personsToGen, password)

        return render_template('persons.html',persons=personsLog)

    return app

            

