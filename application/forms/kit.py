# -*- coding: utf-8 -*-
from application.utils import const
from wtforms import Form, HiddenField, TextField, SelectField, TextAreaField, FileField
from wtforms.validators import Length, Required
from application.services.logic.category import CategoryLogic


class CreateForm(Form):
    author_id = HiddenField(
        u"author_id"
    )
    kit_id = HiddenField(
        u"kit_id"
    )
    kit_name = TextField(
        const.FORM_LABEL_KIT_NAME,
        validators=[
            Length(min=1, max=30, message=const.FORM_MESSAGE_LENGTH_1_30),
            Required(const.FORM_MESSAGE_REQUIRED_KIT_NAME)
        ]
    )
    category_id = SelectField(
        const.FORM_LABEL_KIT_CATEGORY
    )
    tags = TextField(
        const.FORM_LABEL_KIT_TAGS,
        validators=[
            Length(min=0, max=30, message=const.FORM_MESSAGE_LENGTH_UNDER_30),
        ]
    )
    description = TextAreaField(
        const.FORM_LABEL_KIT_DESCRIPTION,
        validators=[
            Length(min=0, max=300, message=const.FORM_MESSAGE_LENGTH_UNDER_300),
        ]
    )
    kit_file = FileField(
        const.FORM_LABEL_KIT_FILE,
    )

    def init(self):
        categories = CategoryLogic.list().get("items")
        self.category_id.choices = [
            (category.get("category_id"), category.get("category_name"))
            for category in categories]


class UpdateForm(Form):
    author_id = HiddenField(
        u"author_id"
    )
    kit_id = HiddenField(
        u"kit_id"
    )
    kit_name = TextField(
        const.FORM_LABEL_KIT_NAME,
        validators=[
            Length(min=1, max=30, message=const.FORM_MESSAGE_LENGTH_1_30),
            Required(const.FORM_MESSAGE_REQUIRED_KIT_NAME)
        ]
    )
    category_id = SelectField(
        const.FORM_LABEL_KIT_CATEGORY
    )
    tags = TextField(
        const.FORM_LABEL_KIT_TAGS,
        validators=[
            Length(min=0, max=30, message=const.FORM_MESSAGE_LENGTH_UNDER_30),
        ]
    )
    description = TextAreaField(
        const.FORM_LABEL_KIT_DESCRIPTION,
        validators=[
            Length(min=0, max=300, message=const.FORM_MESSAGE_LENGTH_UNDER_300),
        ]
    )
    valid = SelectField(
        const.FORM_LABEL_STATUS,
        choices=[
            ("True", const.FORM_CHOICES_TRUE),
            ("False", const.FORM_CHOICES_FALSE)
        ]
    )
    kit_file = FileField(
        const.FORM_LABEL_KIT_FILE,
    )

    def init(self):
        categories = CategoryLogic.list().get("items")
        self.category_id.choices = [
            (category.get("category_id"), category.get("category_name"))
            for category in categories]
