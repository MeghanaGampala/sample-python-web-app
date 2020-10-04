# sample-python-web-app

## Sample python application for testing

This appplication is for testing containers, python, flask, HTML, &c.  There are three initial routes:

| Path | Description |
| --- | --- |
| `/`  | The homepage|
|`/system_info` | System information about the host running the application. |
| `version` | Application and program versions |

## Directions

### Run locally

```
pip -r requirements.txt
FLASK_APP=./app.py python -m flask run --host=0.0.0.0
```

### Run in container

```
docker build -t sample-python-app .
docker run --rm -p 5000:5000 sample-python-app

```

## To-do

- Javascript stuff
- Jenkinsfile
- Other CI/CD build configuration
- More routes
