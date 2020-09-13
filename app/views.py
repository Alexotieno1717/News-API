from flask import Flask, render_template
from app import app
from .request import NewsRequests


@app.route('/')
def index():
    n = NewsRequests()
    # return news.get_top_headlines()
    sport_news = n.get_top_headlines(category='sports')
    return render_template('index.html', sport=sport_news['articles'])
