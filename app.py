from flask import Flask, Response, render_template
from scrape_streams import ScrapeStreams
import requests

app = Flask(__name__)

def get_video_stream(url):
    response = requests.get(url, stream=True)
    for chunk in response.iter_content(chunk_size=1024):
        yield chunk

@app.route('/')
def index():
    return 'Hello from streamsnipe'

@app.route('/stream')
def stream():
    # attempt to load stream directly
    url = 'https://<snipped>'
    return Response(get_video_stream(url), mimetype='video/mp4')

@app.route('/streams')
def streams():
    streams = ScrapeStreams.scrape_streameast()
    return render_template('streams.html', streams=streams)


if __name__ == '__main__':
    app.run(debug=True)
