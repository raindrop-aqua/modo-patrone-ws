# -*- coding: utf-8 -*-
from application.utils import const

from wtforms import Form, HiddenField, TextField, PasswordField, SelectField
from wtforms.validators import Length, Required, EqualTo


class CreateForm(Form):
    author_id = HiddenField(
        u"Id"
    )
    author_name = TextField(
        const.FORM_LABEL_AUTHOR_NAME,
        validators=[
            Length(min=1, max=30, message=const.FORM_MESSAGE_LENGTH_1_30),
            Required(const.FORM_MESSAGE_REQUIRED_AUTHOR_NAME)
        ]
    )
    password = PasswordField(
        const.FORM_LABEL_AUTHOR_PASSWORD,
        validators=[
            Length(min=1, max=30, message=const.FORM_MESSAGE_LENGTH_1_30),
            Required(const.FORM_MESSAGE_REQUIRED_PASSWORD)
        ]
    )
    password_validate = PasswordField(
        const.FORM_LABEL_AUTHOR_PASSWORD_VALIDATE,
        validators=[
            Length(min=1, max=30, message=const.FORM_MESSAGE_LENGTH_1_30),
            Required(const.FORM_MESSAGE_REQUIRED_PASSWORD_VALIDATE),
            EqualTo("password", message=const.FORM_MESSAGE_EQUAL_TO_PASSWORD_VALIDATE)
        ]
    )
    mail_address = TextField(
        const.FORM_LABEL_AUTHOR_MAIL_ADDRESS,
        validators=[
            Length(min=1, max=100, message=const.FORM_MESSAGE_LENGTH_1_100),
            Required(const.FORM_MESSAGE_REQUIRED_MAIL_ADDRESS)
        ]
    )


class UpdateForm(Form):
    author_id = HiddenField(
        u"Id"
    )
    author_name = TextField(
        const.FORM_LABEL_AUTHOR_NAME,
        validators=[
            Length(min=1, max=30, message=const.FORM_MESSAGE_LENGTH_1_30),
            Required(const.FORM_MESSAGE_REQUIRED_AUTHOR_NAME)
        ]
    )
    mail_address = TextField(
        const.FORM_LABEL_AUTHOR_MAIL_ADDRESS,
        validators=[
            Length(min=1, max=100, message=const.FORM_MESSAGE_LENGTH_1_100),
            Required(const.FORM_MESSAGE_REQUIRED_MAIL_ADDRESS)
        ]
    )
    valid = SelectField(
        const.FORM_LABEL_STATUS,
        choices=[
            ("True", const.FORM_CHOICES_TRUE),
            ("False", const.FORM_CHOICES_FALSE)
        ]
    )


class UpdatePasswordForm(Form):
    author_id = HiddenField(
        u"Id"
    )
    password = PasswordField(
        const.FORM_LABEL_AUTHOR_PASSWORD,
        validators=[
            Length(min=1, max=30, message=const.FORM_MESSAGE_LENGTH_1_30),
            Required(const.FORM_MESSAGE_REQUIRED_PASSWORD)
        ]
    )
    password_validate = PasswordField(
        const.FORM_LABEL_AUTHOR_PASSWORD_VALIDATE,
        validators=[
            Length(min=1, max=30, message=const.FORM_MESSAGE_LENGTH_1_30),
            Required(const.FORM_MESSAGE_REQUIRED_PASSWORD_VALIDATE),
            EqualTo("password", message=const.FORM_MESSAGE_EQUAL_TO_PASSWORD_VALIDATE)
        ]
    )
