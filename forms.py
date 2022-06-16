from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, URL


##WTForm
class NewTaskForm(FlaskForm):
    task = StringField(validators=[DataRequired()], label='', render_kw={"placeholder": "Type new task here"})
    submit = SubmitField("Add")


class OldTaskForm(FlaskForm):
    # task = StringField()
    done = SubmitField("Mark Done")

# class CreatePostForm(FlaskForm):
#     title = StringField("Blog Post Title", validators=[DataRequired()])
#     subtitle = StringField("Subtitle", validators=[DataRequired()])
#     img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
#     submit = SubmitField("Submit Post")
#
#
# class RegisterForm(FlaskForm):
#     email = StringField("Email", validators=[DataRequired()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     name = StringField("Name", validators=[DataRequired()])
#     submit = SubmitField("Sign Me Up!")
#
#
# class LoginForm(FlaskForm):
#     email = StringField("Email", validators=[DataRequired()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     submit = SubmitField("Let Me In!")
