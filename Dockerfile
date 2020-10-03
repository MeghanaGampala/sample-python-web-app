FROM python:3.8-slim-buster
WORKDIR /sample-python-web-app
ADD . /sample-python-web-app
RUN pip install -r requirements.txt
ENV FLASK_APP /sample-python-web-app/app.py
EXPOSE 5000
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]