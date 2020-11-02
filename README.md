# backend
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Disjoin-Covid-19/backend/)

## Run
First, switch into the virtual environment by running the following:

    >$  source venv/bin/activate

Next, start the `run_server.sh` script. It's only a couple commands,
but is provided for convenience.

    >$  ./run_server.sh

## Deployment
Edit `run_server.sh` and change line 2 to the following:

    export FLASK_ENV=production;

Also change the IP mask we're using to tolerate all public addresses. Append
the `host` argument to line 3 of `run_server.sh`:

    flask run --host=0.0.0.0

## API

### Mock Data
The mock data, as retrieved from the frontend repo, can be accessed via
GET request to the `/data` route. For example,

    http://localhost:5000/data
