# Shortener
Encurtador de link, onde o usuário informa qualquer url, e será gerado uma url menor. Para o processo de encurtar as urls, foi utilizado a biblioteca `pyshorteners`.

## Executar projeto
- Crie um ambiente virtual e ative
```
python -m venv venv
source /venv/bin/activate (linux)
/venv/script/activate (windows)
```
- Instale as dependências
```
pip install -r requirements.txt
```
- Execute as migrations para o banco de dados
```
python manage.py migrate
```
- Executar os testes.
```
python manage.py test
```
- Executar aplicação.
```
python manage.py runserver
```

## Frameworks e Bibliotecas
- [Django](https://www.djangoproject.com/)
- [pyshorteners](https://pyshorteners.readthedocs.io/en/latest/)