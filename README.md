# Projeto de desenvolvimento de software

### Assunto simplificado: Aplicação para visualizar filmes e atores

### Diretórios importantes:
  * **/softMoviesProjectTests/main**  : Contém todos os arquivos esqueletos da implementação do software;
  * **/softMoviesProjectTests/tests** : Contém todos os arquivos de teste para o que foi implementado no módulo **main**;

### Breve introdução dos pacotes de implementação do software:
  - **models**      : Contém todos os arquivos de entidades-núcleo do sistema. Ex.: Usuario, Filme, Ator etc;
  - **exceptions**  : Contém todos os arquivos de exceções para possíveis erros no banco de dados;
  - **persistence** : Contém todos os arquivos que são responsáveis não só pela comunicação com o BD, mas também por transformar os dados em informações utilizáveis;
  - **views**       : Contém os arquivos que lidam com requisições do usuário e formam a lógica do sistema;
  - **templates**   : Contém os arquivos HTML que representam a interface do sistema.
  #### Vai ser possível perceber que está faltando um pacote, que é o de arquivos 'estáticos', onde conteríamos os arquivos CSS. Mas como este não é o foco do trabalho, este arquivo foi ocultado.

### Artigo descrevendo o projeto:
  * [Artigo.pdf](https://github.com/matheusrnk/trab-source-soft/blob/main/Artigo.pdf)

### Recomendação:
  * Será possível perceber que têm-se um arquivo **venv.zip** dentro do diretório **/softMoviesProjectTests/**. Ele é responsável pelo ambiente Python em que se foi desenvolvido a aplicação. Se não for possível rodá-la sem ele, é sugerido que extraia o conteúdo do arquivo e tente rodar o projeto na IDE de preferência.
