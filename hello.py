

import os
from flask import Flask, stream_with_context, request, Response, url_for

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello Worldasd123'

def stream_template(template_name, **context):
    # http://flask.pocoo.org/docs/patterns/streaming/#streaming-from-templates
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    # uncomment if you don't need immediate reaction
    ##rv.enable_buffering(5)
    return rv


@app.route('/test/')
def index():
    def g():
        yield """<!doctype html>
<title>Send javascript snippets demo</title>
<style>
  #data {
    text-align: center;
  }
</style>
<script src="http://code.jquery.com/jquery-latest.js"></script>
<div id="data">nothing received yet</div>
"""

        for i, c in enumerate("hello"):
            yield """
<script>
  $("#data").text("{i} {c}")
</script>
""".format(i=i, c=c)
            time.sleep(1)  # an artificial delay
    return Response(g())

# It is the main call for the application
# Do not make change or modify   
if __name__ == '__main__':
	app.run()
