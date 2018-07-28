# PLIVO-POC

## Installation
1. Clone the repo.
2. Run `pip install -r requirements.txt` (Use virtualenv)
3. `touch sqlite.db` in repo main dir

## Running Migrations
1. Go to project Repo.
2. Run  `python manage.py db init` to initialise migrations
3. Run `python manage.py db migrate` to generate the migrations files.
4. Run `python manage.py db upgrade` to upgrade the database.

## Using Shell
1. Go to project repo.
2. Run `python manage.py shell`


## Run the server
1. Use `python runner.py`. Server is spawned on 5000 port.


## Testing
1. Launch a local redis server at port `6379` and db `0`
2. Run `pytest tests/`
