# backend


## Run
First, switch into the virtual environment by running the following:

    >$  source venv/bin/activate

Next, start the `run_server.sh` script. It's only a couple commands,
but is provided for convenience.

    >$  ./run_server.sh

## Deployment
Edit `run_server.sh` and change line 2 to the following:

    export FLASK_ENV=production;