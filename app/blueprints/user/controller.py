# instance of delivery app blueprint
import json

from flask import Blueprint

from averich.blueprints.user.forms import UserRegistrationForm
from averich.generic.functions import generate_final_data, populate_errors

user_blueprint = Blueprint("user", __name__, url_prefix='/user')


@user_blueprint.route('/', methods=["GET"])
def get_users():
    final_data = generate_final_data("SUCCESS")
    final_data['result'] = []

    return final_data


@user_blueprint.route('/<id>', methods=["GET"])
def get_user_by_id(id):
    final_data = generate_final_data("SUCCESS")
    final_data['result'] = {"user_id": id}

    return final_data


@user_blueprint.route('/', methods=["POST"])
def create_user():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user_data = {"user_name": form.user_name.data, "email": form.email_id.data}
        final_data = generate_final_data("SUCCESS")
        final_data['result'] = user_data
    else:

        # Form validation error.
        final_data = generate_final_data('FORM_ERROR')
        final_data['errors'] = populate_errors(form.errors)

    return final_data


@user_blueprint.route('/custom_api', methods=["POST"])
def custom_api():

    return generate_final_data("CUSTOM_SUCCESS", "You can perform custom actions too")