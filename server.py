
from bottle import route, run, template, get, request
import requests

from modify import ModifyPage

URL = 'https://news.ycombinator.com/'
LETTER_NUMBER = 6
# Определяет заданное количество букв в слове

@get('/<context>')
def index(context):
    id = request.query.id
    site = request.query.site
    goto = request.query.goto
    response = requests.get(f'{URL}{context}?id={id}&site={site}&site={site}&goto={goto}')
    page=ModifyPage(response.text, LETTER_NUMBER)
    page.modify_page()
    return page.get_modify_page()
    
if __name__ == '__main__':
    run(host='localhost', port=8000)