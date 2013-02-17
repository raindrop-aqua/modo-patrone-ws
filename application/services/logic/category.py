# -*- coding: utf-8 -*-

from application.models.category import Category


class CategoryLogic(object):
    @classmethod
    def init(cls):
        def create(category_name):
            Category(
                id=Category.make_category_id_hash(),
                category_name=category_name
            ).put()

        category_names = ["Animation", "General", "Modeling", "Rendering", "Texturing"]
        [create(category) for category in category_names]
        return True

    @classmethod
    def list(cls):
        categories = [category.to_hash() for category in
                      Category.query(Category.valid == True).order(Category.category_name)]
        return dict(items=categories)
