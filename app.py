from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__, static_folder='static', static_url_path='/')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    # district_num = request.args.get('distrct', '')
    area_num = request.args.get('area', '')
    return redirect('/'+area_num+'.geojson')


app.run(port=3000)
