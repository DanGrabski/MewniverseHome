#!/usr/local/bin/python

from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask import Response, stream_with_context

import PrefixMiddleware

import json
import sys

# imports from Nest stuff
#from sample import views, auth, data_store
#from errors import APIError, error_result
#from nest_wwn import nest_data as models, nest_api as api, port as wwn_port
from nest_wwn import nest_data, nest_api, port as wwn_port

app = Flask(__name__)
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/Mewniverse')

# done: need to get rid of Application_Root
# ToDo: bring in packages for Nest comms
# ToDo: set up authorization for Nest
# ToDo: basic webpage to test data reporting from Nest

@app.route('/')
def render_home():
    # render the home landing page with access to all sections
    return render_template('index.html')

@app.route('/Nest')
def render_nest_home():
    # render the home landing page for the nest control page
    return render_template('index_nest.html')

@app.route('/Weather')
def render_home_weather():
    # render the home landing page for the weather station
    return render_template('index_weather.html')


def start_app():
    # get command-line options and configuration
    # use_redis = False
    # if len(sys.argv) >= 2:
    #     use_redis = sys.argv[1] == '--use-redis'
    # print "Use Redis for server-side session: ", use_redis
    # if use_redis:
    #     from third_party import redis_session
    #     from redis import Redis
    #     from os import environ
    #     redis_host = environ.get("REDIS_HOST", "localhost")
    #     redis_port = environ.get("REDIS_PORT", 6379)
    #     redis_inst = Redis(host=redis_host, port=redis_port)
    #     app.session_interface = redis_session.RedisSessionInterface(redis=redis_inst)

    app.debug = True
    app.secret_key = "test"
    port = wwn_port
    host = '0.0.0.0'
    app.run(host=host, port=port, threaded=True)


if __name__ == "__main__":
    start_app()
