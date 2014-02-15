

import os
import itertools
import time
from flask import Flask, stream_with_context, request, Response, url_for

app = Flask(__name__)

def stream_template(template_name, **context):
    # http://flask.pocoo.org/docs/patterns/streaming/#streaming-from-templates
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    # uncomment if you don't need immediate reaction
    ##rv.enable_buffering(5)
    return rv


@app.route('/')
def index():
    def g():
        for i in range(1,500):
            if i%2 == 0:
                yield i
            time.sleep(.1)  # an artificial delay
    return Response(stream_template('index.html', data=g()))


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    def g():
        for i,c in enumerate(processed_text):
            yield i,c
            time.sleep(.1)  # an artificial delay
    return Response(stream_template('result.html', data=g()))
    #return processed_text

# It is the main call for the application
# Do not make change or modify   
if __name__ == '__main__':
	app.run()
