from flask import Flask, render_template, abort
from main.views.forms import FormularioCadastro, FormularioLogin, FormularioBusca
from flask import redirect, url_for

from main.models.ator import Ator
from main.models.filme import Filme
from main.models.usuario import Usuario
from main.views.Sistema import Sistema
from main.views.MovieAPI import MovieAPI
from main.models.imagem import Imagem
import io
import PIL.Image as Image
from main.models.genero import Genero

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'


def retorna_imagem(f):
    b = bytearray(f)
    image = Image.open(io.BytesIO(b))
    imagem = Imagem(imagem=b, altura=image.height, largura=image.width)
    return imagem


@app.route("/", methods=["POST", "GET"])
def home():
    formulario = FormularioBusca()
    gs = MovieAPI().busca_generos()
    if formulario.validate_on_submit():
        busca = formulario.busca.data
        try:
            fs = MovieAPI().busca_filmes_home(busca)
        except Exception as e:
            print(e)
            return render_template("home.html", form=formulario, generos_buscados=gs,
                                   usuario_logado=Usuario(),
                                   message="Não há filme com este prefixo/sufixo no sistema! Tente novamente!")
        return redirect(url_for('lista_filmes', busca=busca))
    return render_template("home.html", form=formulario, generos_buscados=gs,
                           usuario_logado=Usuario())


@app.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    formulario = FormularioCadastro()
    gs = MovieAPI().busca_generos()
    if formulario.validate_on_submit():
        f = formulario.foto.data.read()
        imagem = retorna_imagem(f)
        novo_usuario = Usuario(nickname=formulario.nickname.data, email=formulario.email.data,
                               nome=formulario.nome.data, senha=formulario.senha.data, retrato=imagem)
        try:
            Sistema().cadastrar_usuario(novo_usuario)
        except Exception as e:
            print(e)
            return render_template("cadastro.html", form=formulario, generos_buscados=gs,
                                   usuario_logado=Usuario(),
                                   message="Ocorreu um erro no sistema, por favor tentar novamente!")
        return redirect(url_for('login'))
    return render_template("cadastro.html", form=formulario, generos_buscados=gs,
                           usuario_logado=Usuario())


@app.route("/login", methods=["POST", "GET"])
def login():
    formulario = FormularioLogin()
    gs = MovieAPI().busca_generos()
    if formulario.validate_on_submit():
        try:
            ok = Sistema().login_usuario(formulario.nickname.data, formulario.senha.data)
            u = None
            if ok:
                u = Usuario()

            if u is None:
                return render_template("login.html", form=formulario, generos_buscados=gs,
                                       usuario_logado=Usuario(),
                                       message="Cadastro Inválido. Tente novamente!")
            else:
                return redirect(url_for('usuario', nickname=u.nickname))
        except Exception as e:
            print(e)
            return render_template("login.html", form=formulario, generos_buscados=gs,
                                   usuario_logado=Usuario(),
                                   message="Cadastro Inválido. Tente novamente!")
    return render_template("login.html", form=formulario, generos_buscados=gs,
                           usuario_logado=Usuario())


@app.route("/filme/<str:id_filme>", methods=["POST", "GET"])
def filme(id_filme):
    gs = MovieAPI().busca_generos()
    try:
        f = MovieAPI().busca_filme_id(id_filme)
        filme_salvo = None
        u = Usuario()
        if u is not None:
            filmes_salvos = Sistema().busca_filmes_salvos_usuario(u)
            for flm in filmes_salvos:
                if flm.id == id_filme:
                    filme_salvo = flm
                    break

        return render_template("filme.html", filme_buscado=f,
                               usuario_logado=Usuario(), generos_buscados=gs,
                               filme_salvo=filme_salvo)
    except Exception as e:
        print(e)
        abort(404, description="Acesso inválido! Filme com ID inexistente!")
    return render_template("filme.html", generos_buscados=gs,
                           usuario_logado=Usuario())


@app.route("/ator/<str:id_ator>", methods=["POST", "GET"])
def ator(id_ator):
    gs = MovieAPI().busca_generos()
    try:
        a = Ator()
        fss = a.participacoes
        a.filmes_principais = fss
        ator_salvo = None
        u = Usuario()
        if u is not None:
            atores_salvos = Sistema().busca_filmes_salvos_usuario(u)
            for atr in atores_salvos:
                if atr.id == id_ator:
                    ator_salvo = atr
                    break
        return render_template("ator.html", ator_buscado=a,
                               usuario_logado=Usuario(), generos_buscados=gs,
                               ator_salvo=ator_salvo)
    except Exception as e:
        print(e)
        abort(404, description="Acesso inválido! Ator com ID inexistente!")
    return render_template("ator.html", generos_buscados=gs,
                           usuario_logado=Usuario())


@app.route("/usuario/<nickname>", methods=["POST", "GET"])
def usuario(nickname):
    gs = MovieAPI().busca_generos()
    u = Usuario()
    if u is None or u.nickname != nickname:
        abort(404, description="Acesso inválido! Usuario não está logado!")
    else:
        u_filmes_salvos = Sistema().busca_filmes_salvos_usuario(u)
        u_atores_salvos = Sistema().busca_atores_salvos_usuario(u)
        return render_template("usuario.html", usuario_logado=u, extensao=u.imagem.return_image_format(),
                               imagem_usuario=u.imagem.image_bytearray_to_encode64(), u_filmes_salvos=u_filmes_salvos,
                               u_atores_salvos=u_atores_salvos, generos_buscados=gs)
    return render_template("usuario.html", generos_buscados=gs,
                           usuario_logado=Usuario())


@app.route("/lista_filmes/<busca>", methods=["POST", "GET"])
def lista_filmes(busca):
    gs = MovieAPI().busca_generos()
    try:
        fs = MovieAPI().busca_filmes_home(busca)
        return render_template("lista_filmes.html", filmes_buscados=fs, generos_buscados=gs,
                               usuario_logado=Usuario())
    except Exception as e:
        print(e)
        abort(404, description="Não foi possível efetuar a busca! Erro no sistema!")
    return render_template("lista_filmes.html", generos_buscados=gs,
                           usuario_logado=Usuario())


@app.route("/melhores_filmes", methods=["POST", "GET"])
def melhores_filmes():
    gs = MovieAPI().busca_generos()
    try:
        fs = MovieAPI().busca_melhores_rankeados()
        return render_template("lista_filmes.html", filmes_buscados=fs, generos_buscados=gs,
                               usuario_logado=Usuario())
    except Exception as e:
        print(e)
        abort(404, description="Não foi possível efetuar a busca! Erro no sistema!")
    return render_template("lista_filmes.html", generos_buscados=gs,
                           usuario_logado=Usuario())


@app.route("/filmes_por_genero/<genero>", methods=["POST", "GET"])
def filmes_por_genero(genero):
    gs = MovieAPI().busca_generos()
    try:
        fs = MovieAPI().busca_filmes_por_genero(Genero(nome=genero))
        return render_template("lista_filmes.html", filmes_buscados=fs, generos_buscados=gs,
                               usuario_logado=Usuario())
    except Exception as e:
        print(e)
        abort(404, description="Não foi possível efetuar a busca! Erro no sistema!")
    render_template("lista_filmes.html", generos_buscados=gs,
                    usuario_logado=Usuario())


@app.route("/salva_filme_usuario/<str:id_filme>", methods=["POST", "GET"])
def salva_filme_usuario(id_filme):
    try:
        f = Filme()
        u = Usuario()
        Sistema().salva_filme_usuario(u, f)
    except Exception as e:
        print(e)
    return redirect(url_for('filme', id_filme=id_filme))


@app.route("/exclui_filme_usuario/<str:id_filme>", methods=["POST", "GET"])
def exclui_filme_usuario(id_filme):
    try:
        f = Filme()
        u = Usuario()
        Sistema().exclui_filme_usuario(u, f)
    except Exception as e:
        print(e)
    return redirect(url_for('filme', id_filme=id_filme))


@app.route("/salva_ator_usuario/<str:id_ator>", methods=["POST", "GET"])
def salva_ator_usuario(id_ator):
    try:
        a = Ator()
        u = Usuario()
        Sistema().salva_ator_usuario(u, a)
    except Exception as e:
        print(e)
    return redirect(url_for('ator', id_ator=id_ator))


@app.route("/exclui_ator_usuario/<str:id_ator>", methods=["POST", "GET"])
def exclui_ator_usuario(id_ator):
    try:
        a = Ator()
        u = Usuario()
        Sistema().exclui_ator_usuario(u, a)
    except Exception as e:
        print(e)
    return redirect(url_for('ator', id_ator=id_ator))


@app.route("/logout", methods=["POST", "GET"])
def logout():
    Sistema().logout_usuario()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3000)
