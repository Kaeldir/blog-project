from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Your e-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Your password (it must be at least 8 letters long)",
                             validators=[DataRequired(), Length(min=8)])
    name = StringField("Your nickname", validators=[DataRequired()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Your e-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Your password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class CommentForm(FlaskForm):
    comment = CKEditorField("Your comment", validators=[DataRequired()])
    submit = SubmitField("Send")
