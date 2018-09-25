from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url, Optional

class ArticleForm(FlaskForm):
    title = StringField('ЗАГОЛОВОК', validators=[DataRequired()])
    body = TextAreaField('ТЕКСТ', validators=[DataRequired()])
    url = URLField(validators=[url(), Optional()])
    submit = SubmitField('ОТПРАВИТЬ')


class CommentForm(FlaskForm):
    text = StringField(validators=[DataRequired()])
    submit = SubmitField('ДОБАВИТЬ')
