from flask import Flask, url_for, render_template
import json
import yaml
import os.path
from joy import gen_map as jgm
from Davin import gen_map as dgm

app = Flask(__name__)

DIR = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(DIR,'../UCSC_Sound_Map.csv')
with open('secrets.yaml','r') as api_file:
	gkey = yaml.load(api_file)['api_keys']['google']

DIR = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(DIR,'../UCSC_Sound_Map.csv')


#making several pages
@app.route('/')
def index(): 
    return 'welcome to a webpage'

@app.route('/hello')
def hello(): 
    return 'Hey its bre'

#making a map page
@app.route('/joy/map')
def jmap():
	return render_template(jgm.generate_map(CSV,gkey))

@app.route('/davin/map')
def dmap(): 
	return render_template(dgm.generate_map(CSV,gkey))

#json endpoint/ 
@app.route('/authors')
def authors():
    madeby = ['bre', 'davin', 'joy']
    return json.dumps(madeby)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
