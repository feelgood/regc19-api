# C19 symptoms registration API
  
## Development

### Requirements
#### Python
You need **Python 3.6** or above.

Include current directory in your Python environment:
`export PYTHONPATH=.`


#### Redis
You'll also need Redis. An own local installation or a cloud installation.
On Ubuntu you can install Redis with:
```
sudo apt install redis
```
this installs and starts Redis on localhost:6379.
Stop and start Redis with `systemctl stop|start redis-server.service`

Configure your redis connection with environment variable `REDIS_URL`.
```
export REDIS_URL=redis://localhost:6379/0
```
This is the default url on a fresh local installation.



### Start dev server
Start a local server on http://localhost:5000:
```
virtualenv venv
. venv/bin/activate
pip3 install -r requirements.txt
python3 run.py
```

### Gunicorn
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

Steps on Ubuntu for creating Heroku instance with Redis addon:
```
sudo snap install heroku --classic
heroku login
cd path/to/regc19-api
heroku create regc19-api --region eu
heroku addons:create heroku-redis:hobby-dev -a regc19-api --region eu
git push heroku master
```

In GitHub you can setup automatic Heroku deploy using the Heroku GitHub integration.
https://devcenter.heroku.com/articles/github-integration

## Usage

An OpenAPI specification will be published later

GET, POST, PUT and DELETE `/c19/registrations`
