# Easy Goal Backend REST API
## Dependencies
Dependencies to run:

- docker
- docker-compose

Dependancies for development:

- python3.8

## Running the API
To run REST API (from top level directory):
```
cp .env.sample .env
docker-compose up --build --force-recreate
```

The documentation is hosted at http://localhost:8080/docs/

The MongoDB database is forwarded to http://localhost:27017/ 


## Testing the API
To run unit testing (from top level directory:
```
python3 -m venv backend_env
source backend_env/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
pytest
```
