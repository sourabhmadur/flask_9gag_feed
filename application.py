import flask
import feedparser
import requests
from flask import Flask,request, render_template
application = app = Flask(__name__)

d_awe = feedparser.parse('https://9gag-rss.com/api/rss/get?code=9GAGAwesome&format=2')

d_comic = feedparser.parse('https://9gag-rss.com/api/rss/get?code=9GAGComic&format=2')

d_dark_humor = feedparser.parse('https://9gag-rss.com/api/rss/get?code=9GAGDarkHumor&format=2')

d_fresh = feedparser.parse('https://9gag-rss.com/api/rss/get?code=9GAGFresh&format=2')

rss_feeds = {'awesome':d_awe, 'comic': d_comic, 'dark_humor': d_dark_humor, 'fresh':d_fresh }


@app.route('/')
def hello_world():
   
    return render_template("postings.html",  feeds = rss_feeds )
    


@app.route('/genre/<feed>')
def genre(feed='awesome'):
   
    return render_template("genre.html",  feed = rss_feeds[feed] )



if __name__ == '__main__':
    app.run(debug = True)
