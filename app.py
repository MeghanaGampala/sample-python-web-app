import os
import platform
import requests
import json
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from version import app_version 

app = Flask(__name__)

# Initialization
debug = bool(os.getenv('DEBUG'))
print(debug)

#Main page
@app.route('/')
def main():

    # Check for any headers starting with "Kollegehill and pass them downstream"
    request_headers = request.headers
    if debug:
        print("Request headers: %s " % request_headers)
    pass_headers = {}
    for k,v in request_headers.items():
        if str(k).startswith("Kollegehill"):
            pass_headers[k] = v
    
    print("Adding headers: %s " % pass_headers)

    # Image placeholders
    cat_fact_image_url = 'https://placekitten.com/300/200'
    
    

    # Get the cat caption
    catfact_uri = 'https://catfact.ninja/fact'
    image_caption = get_catfact(catfact_uri)
    
 
    
    # Get basic system info
    uname = platform.uname()

    response = render_template('index.html',
                                cat_image = cat_fact_image_url,
                                caption = image_caption,
                                uname = uname)
    return response
    

def get_catfact(uri):
    response = requests.get(uri, headers = {'accept': 'application/json'}).json()
    value = response['fact']
    return value

#system info page
@app.route('/system_info')
def get_system_info():
    platform_data = {} 
    uname = platform.uname()
    platform_data['System'] = uname.system
    platform_data['Node'] = uname.node
    platform_data['Release'] = uname.release
    platform_data['Version'] = uname.version
    platform_data['Machine'] = uname.machine
    return platform_data

#verion page
@app.route('/version')
def get_version():
    return app_version

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')