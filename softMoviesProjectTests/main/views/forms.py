from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import InputRequired, Email, EqualTo


class FormularioCadastro(FlaskForm):
    foto = FileField('Foto', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    nickname = StringField('Nickname', validators=[InputRequired()])
    email = StringField('Email',
                        validators=[InputRequired(), Email()])
    senha = PasswordField('Senha', validators=[InputRequired()])
    confirma_senha = PasswordField('Confirme a senha',
                                   validators=[InputRequired(), EqualTo('senha')])
    nome = StringField('Nome')
    submit = SubmitField('Cadastrar-se')


class FormularioLogin(FlaskForm):
    nickname = StringField('Nickname',
                           validators=[InputRequired()])
    senha = PasswordField('Senha', validators=[InputRequired()])
    submit = SubmitField('Login')


class FormularioBusca(FlaskForm):
    busca = StringField('Busca', validators=[InputRequired()])
    submit = SubmitField('Buscar')
