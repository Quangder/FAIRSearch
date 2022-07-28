import os
from flask import Flask, render_template, request
import tarfile
import glob
import time

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/fair/<part_num>')
    def searchFAIR(part_num):
        stripinput = part_num.strip()
        pathstrings = []
        p1 = '/**/*_*'
        p2 = '*'
        concated = p1 + stripinput + p2

        path = '//KNT-SVR-SMIC01/Public/DocumentControl/Customer/Lam/LAM FAIR'

        text_files = glob.glob(path + concated, recursive=True)

        for element in text_files:
            pathstrings.append(str(element).replace('/', '\\'))

        ret = ""
        for path in pathstrings:
            ret = ret + '<a href="file:///' + path + '>'+ path + '</a><br>'

        return render_template('results.html', pathstrings=pathstrings)

    return app