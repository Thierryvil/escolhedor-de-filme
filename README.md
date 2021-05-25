# Escolhedor de Filme
Uma micro aplicação feito em Python, utilizando Flask, HTML, CSS e JavaScript

![escolher-de-fime.gif](https://i.imgur.com/7UOpy2g.gif)


Na hora de escolher um filme é muito fácil nós ficarmos minutos e minutos só olhando as opções que estão na nossa frente, com essa micro aplicação esse problema acabou.
Aplicação filtra os filme com base no genero que você escolher. 

Para isso utilizaremos a api do [The Movie Database](https://www.themoviedb.org/). 

# Começando
Você iria precisar se registar, basta seguir os passos clicando [aqui](https://developers.themoviedb.org/3/getting-started/introduction).
Depois de registrado, _crie um arquivo_ **.env** com sua chave de api disponível pelo The Movie Database.

```bash
API_KEY=f650d6e5cbea1f05498048503b5d4df3
```
<br/>

# Configurando o ambiente
## Criando ambiente virtual
```bash
python -m venv .venv
```

## Inicialziando ambiente virtual
```bash
.venv/Scripts/activate
```

## Instalando Requisitos
```bash
pip install -r requirements.txt
```

## Rodando os testes
```bash
pytest -v
```
