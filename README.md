# hackers-news-proxy

Прокси должен модифицировать текст на страницах сайта Hacker News следующим образом: после каждого слова из шести букв должен стоять значок «™».

Пример:

The visual description of the colliding files, at http://shattered.io/static/pdf_format.png, is not very helpful in understanding how they produced the PDFs, so I took apart the PDFs and worked it out. Basically, each PDF contains a single large (421,385-byte) JPG image, followed by a few PDF commands to display the JPG. The collision lives entirely in the JPG data - the PDF format is merely incidental here. Extracting out the two images shows two JPG files with different contents (but different SHA-1 hashes since the necessary prefix is missing). Each PDF consists of a common prefix (which contains the PDF header, JPG stream descriptor and some JPG headers), and a common suffix (containing image data and PDF display commands).

Через ваш прокси: http://127.0.0.1:8000/item?id=13713480

The visual™ description of the colliding files, at http://shattered.io/static/pdf_format.png, is not very helpful in understanding how they produced the PDFs, so I took apart the PDFs and worked™ it out. Basically, each PDF contains a single™ large (421,385-byte) JPG image, followed by a few PDF commands to display the JPG. The collision lives entirely in the JPG data - the PDF format™ is merely™ incidental here. Extracting out the two images™ shows two JPG files with different contents (but different SHA-1 hashes™ since the necessary prefix™ is missing). Each PDF consists of a common™ prefix™ (which contains the PDF header™, JPG stream™ descriptor and some JPG headers), and a common™ suffix™ (containing image data and PDF display commands).


Установка зависимостей:
```
pip install -r requirements.txt
```
Запуск django проекта:
```
python manage.py runserver
```
