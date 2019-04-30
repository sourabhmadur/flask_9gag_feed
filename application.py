import flask
import feedparser
import requests
from flask import Flask,request, render_template
application = app = Flask(__name__)

d_awe = feedparser.parse('https://9gag-rss.com/api/rss/get?code=9GAGAwesome&format=2')

d_comic = feedparser.parse('https://9gag-rss.com/api/rss/get?code=9GAGComic&format=2')

d_dark_humor = feedparser.parse('https://9gag-rss.com/api/rss/get?code=9GAGDarkHumor&format=2')

d_fresh = feedparser.parse('https://9gag-rss.com/api/rss/get?code=9GAGFresh&format=2')

rss_feeds = [d_awe, d_comic, d_dark_humor, d_fresh ]


@app.route('/')
def hello_world():
   
   # return rss_feeds[0].entries[0].summary
    return render_template("postings.html",  feeds = rss_feeds )
    


@app.route('/temp/<feed>')
def temp(feed=0):
   
    return render_template("temp.html",  feed = rss_feeds[int(feed)] )



if __name__ == '__main__':
    app.run(debug = True)
