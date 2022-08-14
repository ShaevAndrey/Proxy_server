
from bottle import route, run, template, get, request
from modify import ModifyPage
import requests

URL = 'https://news.ycombinator.com/'
LETTER_NUMBER=4

@get('/<context>')
def index(context):
    id = request.query.id
    response = requests.get(f'{URL}{context}?id={id}')
    page=ModifyPage(response.text, LETTER_NUMBER)
    page.modify_page()
    return page.get_modify_page()

run(host='localhost', port=8080)