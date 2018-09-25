# -*- coding: utf-8 -*-

from myapp import app, db
from myapp.models import Article, Comment
from flask import render_template, redirect, flash, url_for, json
from myapp.forms import ArticleForm, CommentForm


@app.route('/read')
def read():
    results = Article.query.all()
    articles = results[::-1]
    return render_template('read.html', articles=articles)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read/article/<id>', methods=["GET", "POST"])
def detail(id):
    form = CommentForm()
    article = Article.query.get(id)
    comments = article.comments.all()
    if form.validate_on_submit():
        comment = Comment(text=form.text.data, com=article)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('detail', id=id))
    return render_template('detail.html', article=article, comments=comments, form=form)


@app.route('/write', methods=['GET', 'POST'])
def write():
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(
                        title=form.title.data,
                        body=form.body.data,
                        url = form.url.data or None)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('write.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')
