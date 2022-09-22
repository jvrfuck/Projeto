# para fazer os comando para criar uma nova merge

```
aonde tem <nome> e literalmente o nome do arquivo que foi ou ira ser criado, 
no caso do exemplo que foi feito pelo colega joao rios ficou como release-1.0
```

- git checkout -b <nome>

# para fazer a branch no git hub 

- git push origin <nome>'''

# para fazer o merge do arquivo release1.0 para o main

- git pull origin <nome>:main 

# Para trabalhar na merge que foi criada do projeto

- git checkout dev 

- git checkout -b <nome>
(que dai nao ira modificar nem o main e nem o dev )
(ai depois puxa para a dev com git pull origin <nome> :dev)



```markdown
no proximo passo foi passados os arquivos que nao sao do app em si para dentro da pasta django e apos passados para a pasta da raiz excluindo o django para nao ter mais ambiente virtual.
Apos foi feita a criaçao da nova estrutura com o virtual ambiente novamente.
Feito o ambiente virtual fazer a instalaçao do pip 
<pip install -r requirements.txt>
```

<!-- ```markdown
criar arquivo <Procfile> dentro do arquivo colocar a segunda linha em branco e a primeira segue a baixo:

- web: gunicorn proj.wsgi

para saber a versao do python:

- python --version

ai o proximo comando para finalizar:

- python --version>runtime.txt
``` -->

```
Criar conta no Heroku e criar um app no mesmo (apenas 1 pessoas fazendo ta bom)
Instalar o client do Heroku
apos instalaçao abrir e fechar Vscode
Testar no terminal se está funcionando com o codigo:

- heroku --version

- heroku login 
<faça login no navegador >
```

# Para saber qual sao as versoes disponiveis dos remote:

- git remote -v 
(deve aparecer:)
- origin .....
- origin ....

# Ai se nao tiver a do heroku adicionar atraves do comando:

heroku git:remote -a agendaieletronica

# Para confirmar 

- git remote -v 
(deve aparecer:)
- origin .....
- origin ....
- heroku .....
- heroku .....

# Para adicionar no heroku 

no heroku so tem 2 merge a main ou a master escolha qual vai usar, em 80% das vezes e a main, no caso o joao usou a main:

- git push heroku <nome> 

<!-- ```markdown
Na Pasta do <Proj> criar um novo arquivo <local_setings.py> e realocar alguns do <settings.py> para esse, segue os codigo no arquivo (nao vou copiar tudo) do git 

Dentro da pasta <settings.py>

try: 
    SECRET_KEY = os.getenv('SECRET_KEY')
except ImportError:
    pass

``` -->

# para configurar a senha no heroku 
(entrar no Python (so digitar python e dar enter no terminal), a senha fica salva na propria configuraçao do heroku no site)

- import secrets
- secrets.token_hex(50)
```
aqui vai geral um <codigo> para colar no comando abaixo 
```
- heroku config:set SECRET_KEY= <codigo>

<!-- # No settings.py, colocar:
<na parte do MIDDLEWARE>

- whitenoise.middleware.WhiteNoiseMiddleware

import django_heroku
import dj_database_url

ALLOWED_HOSTS = ['127.0.0.1', <Site heroku>

try:
    DATABASE_URL = os.getenv('DATABASE_URL')
except ImportError:
    pass

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

<no final do arquivo >

try:
    EMAIL_BACKEND=os.getenv('EMAIL_BACKEND')
    EMAIL_HOST=os.getenv('EMAIL_HOST')
    EMAIL_PORT=os.getenv('EMAIL_PORT')
    EMAIL_HOST_USER=os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD=os.getenv('EMAIL_HOST_PASSWORD')


try:
    from . local_settings import *
except ImportError:
    pass -->

# fazer os import do pip ou usar o pip requirements

- pip install middleware
- pip install psycopg2
- pip install gunicorn 

<!-- # No arquivo local_settings
< no final de cada variante do email colocar, provalmente no arquivo nosso ja esta completado >
Ex:

- heroku config:set EMAIL_HOST = smtp.gmail.com

- Apos jogar no terminal para subir ao heroku  -->

# Para Centralizar os arquivos staticos em um unico arquvio: 
<quando mudar o css ou alguma imagem usar o comando:>
obs: vai ficar duplicado o arquivo ou seja tera na pasta static e na app

- python manage.py collectstatic

<!-- - heroku config:set DISABLE_COLLECTSTATIC=1  -->

# Comando para rodar heroku
(para fazer os comando normais de createsuperuser, runserver, etc., manter o heroku)

-heroku run python manage.py migrate    