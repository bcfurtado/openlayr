# openlayr

## installation

``` sh
git clone git@github.com:bcfurtado/openlayr.git
cd openlayr
mkvirtualenv $(cat .virtual-environment) -p $(which python3)
pip install -r requirements.txt
```

## running

``` sh
python manage.py migrate
python manage.py runserver
```
