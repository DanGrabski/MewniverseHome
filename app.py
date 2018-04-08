#!/usr/local/bin/python

from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask import Response, stream_with_context

import json
import sys

# imports from Nest stuff
#from sample import views, auth, data_store
#from errors import APIError, error_result
#from wwn import nest_data as models, nest_api as api, port as wwn_port

app = Flask(__name__)

app.config['APPLICATION_ROOT'] = '/Mewniverse'

@app.route('/')
def render_home():
    # render the home landing page with access to all sections

@app.route('/Nest')
def render_nest_home():
    # render the home landing page for the nest control page

@app.route('/Weather')
def render_home_weather():
    # render the home landing page for the weather station