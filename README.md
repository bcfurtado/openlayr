# openlayr

[![Build Status](https://travis-ci.org/bcfurtado/openlayr.svg?branch=master)](https://travis-ci.org/bcfurtado/openlayr)


## installation

``` sh
git clone git@github.com:bcfurtado/openlayr.git
cd openlayr
mkvirtualenv $(cat .virtual-environment) -p $(which python3)
pip install -r requirements.txt
```

## configuration
```sh
python manage.py createsuperuser
```

## running

``` sh
python manage.py migrate
python manage.py runserver
```
