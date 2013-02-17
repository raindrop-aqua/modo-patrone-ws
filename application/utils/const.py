# -*- coding: utf-8 -*-


RESPONSE_RESULT_SUCCESSFUL = True
RESPONSE_RESULT_FAILED = False

NAMESPACE_LOGIN = "Author_Login"
LOGIN_TIMEOUT = 60 * 30  # 30 min

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

MESSAGE_SUCCESSFUL = u"成功しました"
MESSAGE_FAILED = u"失敗しました"
MESSAGE_ALREADY_REGISTERED = u"このメールアドレスは登録できません"
MESSAGE_ILLEGAL_REQUEST = u"入力内容に誤りがあります"
MESSAGE_ILLEGAL_ACCESS = u"認証が必要、もしくは認証に失敗、もしくはタイムアウトしました"
MESSAGE_NO_DATA = u"データがありません"

# FORM_LABEL_MARK = u"<i class='icon-caret-right'></i> "
FORM_LABEL_MARK = u""
FORM_LABEL_INFO = u"- "

FORM_LABEL_AUTHOR_NAME = FORM_LABEL_MARK + u"名前（Name）"
FORM_LABEL_AUTHOR_PASSWORD = FORM_LABEL_MARK + u"パスワード（Password）"
FORM_LABEL_AUTHOR_PASSWORD_VALIDATE = FORM_LABEL_MARK + u"パスワード（確認用）（Retype Password）"
FORM_LABEL_AUTHOR_MAIL_ADDRESS = FORM_LABEL_MARK + u"メールアドレス（E-mail）"
FORM_LABEL_STATUS = FORM_LABEL_MARK + u"状態（Status） " + FORM_LABEL_INFO + u" 無効状態ではリストに表示されません"

FORM_LABEL_KIT_NAME = FORM_LABEL_MARK + u"名称（Name）"
FORM_LABEL_KIT_CATEGORY = FORM_LABEL_MARK + u"カテゴリ（Category）"
FORM_LABEL_KIT_TAGS = FORM_LABEL_MARK + u"タグ（Tags） " + FORM_LABEL_INFO + u" カンマ区切り"
FORM_LABEL_KIT_DESCRIPTION = FORM_LABEL_MARK + u"詳細（Description）"
FORM_LABEL_KIT_FILE = FORM_LABEL_MARK + u"ファイル（File） " + FORM_LABEL_INFO + u" 最大2MBまで"

FORM_MESSAGE_LENGTH_1_30 = u"1～30文字で入力してください"
FORM_MESSAGE_LENGTH_1_100 = u"1～100文字で入力してください"
FORM_MESSAGE_LENGTH_UNDER_30 = u"30文字以内で入力してください"
FORM_MESSAGE_LENGTH_UNDER_300 = u"300文字以内で入力してください"

FORM_MESSAGE_REQUIRED_AUTHOR_NAME = u"名前を入力してください"
FORM_MESSAGE_REQUIRED_PASSWORD = u"パスワードを入力してください"
FORM_MESSAGE_REQUIRED_PASSWORD_VALIDATE = u"パスワード（確認用）を入力してください"
FORM_MESSAGE_EQUAL_TO_PASSWORD_VALIDATE = u"パスワードを確認してください"
FORM_MESSAGE_REQUIRED_MAIL_ADDRESS = u"メールアドレスを入力してください"

FORM_MESSAGE_REQUIRED_KIT_NAME = u"名称を入力してください"

FORM_CHOICES_TRUE = u"有効（Valid）"
FORM_CHOICES_FALSE = u"無効（Invalid）"
