# PLIVO-POC

## LOCAL

### Installation
1. Clone the repo.
2. Run `pip install -r requirements.txt` (Use virtualenv)
3. `touch sqlite.db` in repo main dir

### Running Migrations
1. Go to project Repo.
2. Run  `python manage.py db init` to initialise migrations
3. Run `python manage.py db migrate` to generate the migrations files.
4. Run `python manage.py db upgrade` to upgrade the database.

### Run the server
1. Use `python runner.py`. Server is spawned on 5000 port.

## Testing
1. Launch a local redis server at port `6379` and db `0`
2. Run `pytest tests/`

## PROD
Domain is `https://telephony-poc.herokuapp.com`
Basic Auth username and password are `plivo`and `plivo` respectively

### ROUTES
1. HOME URL `https://telephony-poc.herokuapp.com`
2. INBOUND SMS `https://telephony-poc.herokuapp.com`
3. OUTBOUND SMS `https://telephony-poc.herokuapp.com`

### Rate Limiting
Rate limiting is done using redis basic rate limiting pattern
For outbound sms, Please check the response headers
X-Rate-Limit-Threshold → 50
X-Rate-Limit-Value → 1

### Running Migrations in Heroku
1. Run command `heroku run migrate`
2. Run command `heroku run upgrade`
