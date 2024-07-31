# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# フォームの情報を入れるための箱
class InputForm(FlaskForm):  # FlaskFormを継承
    id  = StringField('名前：',validators=[DataRequired('入力必須')])
    pw  = PasswordField('パスワード：',validators=[DataRequired('入力必須')])
    submit = SubmitField('送信')