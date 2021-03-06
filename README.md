# Serapis :musical_note:

## Description
This is a full stack Python/Django site with dynamically displaying content. The site features show dates, an editable home page text area, featured audio and video content on the home page as well as an archive of audio, videos and photos. The band members can add content and update it via the Django admin interface.

## Technologies used
- Languages:
    - Python
    - JavaScript
    - HTML5
    - CSS3

- Design:
    - Bulma CSS
    - Google Fonts
    - Font Awesome icons

- Build:
    - Visual Studio Code
    - SQLite database
    - Python Anywhere hosting

## Features
6 models:
- Home text
- Show dates
- Band member cards
- Latest video
- Video (gallery on Music page)
- Photo (Photos page)

Mobile-responsive design


## Installation Instructions

- git clone git@github.com:mollycarroll/serapis-rocks.git
- cd serapis-rocks
- create a virtualenv with your preferred env manager. I use pyenv,
- pyenv virtualenv 3.8.0 serapis
- pyenv activate serapis
- pip install -r requirements.txt
- python manage.py collectstatic
- python manage.py runserver

