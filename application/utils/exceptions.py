# -*- coding: utf-8 -*-

import const

class AlreadyRegisteredError(Exception):
    '''
    すでに登録済みの場合の例外
    '''
    def __init__(self, *args, **kwargs):
        self.message = const.MESSAGE_ALREADY_REGISTERED

class IllegalRequestError(Exception):
    '''
    入力内容に誤りがある場合の例外
    '''
    def __init__(self, *args, **kwargs):
        self.message = const.MESSAGE_ILLEGAL_REQUEST

class IllegalAccessError(Exception):
    '''
    アクセス権限に引っかかった時の例外
    '''
    def __init__(self, *args, **kwargs):
        self.message = const.MESSAGE_ILLEGAL_ACCESS

class NoDataError(Exception):
    '''
    データが存在しなかった場合の例外
    '''
    def __init__(self, *args, **kwargs):
        self.message = const.MESSAGE_NO_DATA
