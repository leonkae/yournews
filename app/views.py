from flask import render_template
from app import app
from .request import get_articles,get_source


@app.route ('/')
def landing_page():
    '''route for landing page'''
    info = "hello world ....twende!"
    articles = get_articles('business')
    sources = get_source()
    return render_template('index.html',info=info,articles=articles,sources=sources)


@app.route ('/business')
def business():
    '''route for business link'''
    info = "hello world ....twende!"
    articles = get_articles('business')
    return render_template('business.html',info=info,articles=articles)

# @app.route ('/article/<id>')
# def article(id):
#     '''route for articles'''
#     info = "hello world ....twende!"
#     id = id
#     return render_template('article.html',info=info, id=id)

@app.route ('/sports')
def sports():
    '''route for sports page'''
    articles = get_articles ('sports')
    return render_template('sports.html',articles=articles)

@app.route ('/entertainment')
def entertainment():
    '''route for entertainment page'''
    articles = get_articles ('entertainment')
    return render_template('entertainment.html',articles=articles)
   
@app.route('/tech')
def technology():
    '''route for technology page'''
    articles = get_articles('technology')
    return render_template('tech.html',articles=articles)

