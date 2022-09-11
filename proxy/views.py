import re
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from hnproxy.settings import HOST

IGNOR_LIST = ['meta', 'style', 'script', 'head', 'a']

def proxy(request, path) -> HttpResponse:

    url = f'{HOST}{path}'
    try:
        content = requests.get(url, params=request.GET)
    except Exception as e:
        return HttpResponse(e)
    content_type = content.headers['Content-Type']
    status_code = content.status_code
    
    if 'text/html' in content_type:
        content = BeautifulSoup(content.text, 'html5lib')
        content = change_ahrefs(content)
        content = modify_content(content)
        content = str(content)

    return HttpResponse(content, status=status_code,
                        content_type=content_type)


def change_ahrefs(soup) -> BeautifulSoup:

    for ahref in soup.findAll('a', href=True):
        ahref['href'] = ahref['href'].replace(HOST[:-1],'')
    return soup


def modify_content(soup) -> BeautifulSoup:

    for tag in soup.findAll(text=True):
        if tag.parent.name in IGNOR_LIST:
            continue
        else:
            text = tag.string
            tag.replace_with(re.sub(r'\b(?<!&amp;)(?<!&)([а-яёa-z-]{6})\b', r'\1™', text, flags=re.IGNORECASE))
    
    return soup