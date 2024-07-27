from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired,Email

# フォームの情報を入れるための箱
class InputForm(FlaskForm):  # FlaskFormを継承
    name   = StringField('名前：',validators=[DataRequired('入力必須')])
    email  = EmailField('メールアドレス',validators=[Email('メールアドレスのフォーマットではありません。')])
    submit = SubmitField('送信')