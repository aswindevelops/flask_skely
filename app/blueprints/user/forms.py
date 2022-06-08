from wtforms import StringField
from wtforms.validators import InputRequired, Optional
from flask_wtf import FlaskForm


class UserRegistrationForm(FlaskForm):
    """
    WTF form class for validating the create_user API request.
    """

    class Meta:
        csrf = False

    user_name = StringField('user_name', validators=[InputRequired()])
    email_id = StringField('email_id', validators=[Optional()])
