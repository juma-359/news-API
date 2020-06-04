from flask import render_template
from . import main
from ..requests import get_source,get_articles

@main.route('/')
def index():
    news_source=get_source()
    print(news_sources)
    title='Welcome to the new highlighter'
    return render_template('index.html', title=title, source=news_sources)

@main.route('/articles/<string:id>')
def source(id):
    articles=get.get_articles(id)
    print(articles)
    return render_template('articles.html',articles=articles)