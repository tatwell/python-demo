# Python Demo

- App Engine Site: https://tatwell-python-demo.appspot.com/
- Trello Board: https://trello.com/b/j0yRbilt/python-demo


## Flask App Engine Application

The Flask App Engine application is based on the [GoogleCloudPlatform Flask App Engine
skeleton](https://github.com/GoogleCloudPlatform/appengine-python-flask-skeleton).

To install:

1. Install the [Google App Engine Python SDK](https://cloud.google.com/appengine/downloads).

2. Clone this repository:

    git clone https://github.com/tatwell/python-demo.git python-demo

3. Install the required libraries using Pip:

    cd python-demo/app-engine
    pip install -r requirements.txt -t lib


## Development Server

To launch the local development server:

    dev_appserver.py --port=3000 --admin_port=3001 --api_port=3002 ./app-engine

Application will run on [http://localhost:3000](http://localhost:3000).


## Tests

No tests yet.


## Deployment

To deploy the App Engine application:

    appcfg.py --oauth2 -A python-demo -e YOUR_USER_NAME update ./app-engine
