# Standard libraries
import os
import time, string
# These 3 are for generating list libraries
from collections import deque
from itertools import product
from string import ascii_lowercase, digits
# This is for flask
from flask import Flask, stream_with_context, request, Response, url_for

app = Flask(__name__)

# Supporting method for app using template
# DO NOT CHANGE IF NOT NECCESSARY
def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    # uncomment if you don't need immediate reaction
    ##rv.enable_buffering(5)
    return rv


# This will happen when the app is called
# The website will be delay a millisecond in order to get ready
@app.route('/')
def index():
    def delay():
            time.sleep(.1)  # an artificial delay
    return Response(stream_template('index.html', data=delay()))

# Generate a list of ID to check
def generate_words(start, length, _chars=ascii_lowercase + digits):
    remainder = length - len(start)
    if remainder < 1:
        yield start
        return
    for letters in product(_chars, repeat=remainder):
        combo = deque(letters + (start,))
        for _ in range(remainder + 1):
            yield ''.join(combo)
            combo.rotate()    

# Processing data from form
# and prepare all the result for posting
@app.route('/', methods=['POST'])
def get_data():
    # Read from the from input
    chars = request.form['chars']
    max_number = request.form['max_number']

    id_list = generate_list(chars, max_number)
    
    print id_list
    def extract_item_from_list():
        for i in id_list:
            yield i
            time.sleep(.1)  # an artificial delay
    return Response(stream_template('result.html', data=extract_item_from_list()))

# It is the main call for the application
# DO NOT CHANGE
if __name__ == '__main__':
	app.run()
