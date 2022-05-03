from flask import render_template
from app import app
from .request import get_articles,get_source


@app.route ('/')
def landing_page():
    info = "hello world ....twende!"
    articles = get_articles('business')
    sources = get_source()
    return render_template('index.html',info=info,articles=articles,sources=sources)

@app.route ('/business')
def business():
    info = "hello world ....twende!"
    articles = get_articles('business')
    return render_template('business.html',info=info,articles=articles)

@app.route ('/article/<id>')
def article(id):
    info = "hello world ....twende!"
    id = id
    return render_template('article.html',info=info, id=id)

@app.route ('/sports')
def sports():
    articles = get_articles ('sports')
    return render_template('sports.html',articles=articles)

@app.route ('/entertainment')
def entertainment():
    # info = "hello world ....twende!"
    # article = get_articles('sports')
    # return render_template('business.html',info=info,article=article)
     articles = get_articles ('entertainment')
     return render_template('entertainment.html',articles=articles)
   
@app.route('/tech')
def technology():
    articles = get_articles('technology')
    return render_template('tech.html',articles=articles)

