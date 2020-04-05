# C19 Symptoms registration API

## Development
You need Python 3.6 or above.

Include current directory in your Python environment:
`export PYTHONPATH=.`

Start a local server on http://localhost:5000:
```
virtualenv venv
. venv/bin/activate
pip3 install -r requirements.txt
python3 run.py
```

## Gunicorn
Includes Gunicorn WSGI HTTP server for simple Heroku deployments.
Start locally with:
```
virtualenv venv
. venv/bin/activate
pip3 install -r requirements.txt
gunicorn run:app
```

## Heroku
The local server can also be started with heroku
```
heroku local
```
This starts an instance on http://localhost:5000.


### Push to Heroku from CLI
You need an account on Heroku.

Steps on Ubuntu:
```
sudo snap install heroku --classic
heroku login
cd path/to/regc19-api
heroku create regc19-api
git push heroku master
```

In GitHub you can setup automatic Heroku deploy using the Heroku GitHub integration.
https://devcenter.heroku.com/articles/github-integration

## Usage

An OpenAPI specification will be published later

GET, POST, PUT and DELETE `/c19/registrations`
