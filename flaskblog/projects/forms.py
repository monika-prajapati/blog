from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    intro = StringField('Introduction', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    link = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Project')