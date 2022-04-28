import wtforms
from flask_wtf import FlaskForm
from wtforms.validators import Required, Length

class RecordForm(FlaskForm):
    title = wtforms.StringField('Title', validators=[Required(), Length(1,50)])
    text = wtforms.TextAreaField('Text')
    submit = wtforms.SubmitField('Push')


