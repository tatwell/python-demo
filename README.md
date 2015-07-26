# Python Demo

- App Engine Site: https://tatwell-python-demo.appspot.com/
- Trello Board: https://trello.com/b/j0yRbilt/python-demo


## Flask App Engine Application

The Flask App Engine application is based on the [GoogleCloudPlatform Flask App Engine
skeleton](https://github.com/GoogleCloudPlatform/appengine-python-flask-skeleton).

To install, first install the [Google App Engine
SDK](https://cloud.google.com/appengine/downloads), then clone this repository:


## Development Server

To launch the local development server:

    dev_appserver.py --port=3000 --admin_port=3001 --api_port=3002 .

Application will run on [http://localhost:3000](http://localhost:3000).


## Tests

No tests yet.


## Deployment

To deploy the App Engine application:

    appcfg.py --oauth2 -A python-demo -e YOUR_USER_NAME update .
