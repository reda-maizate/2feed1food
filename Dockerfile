FROM python:3.7.7

RUN pip3 install pipenv

ENV PROJECT_DIR usr/src/2feed1food

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["pipenv", "run", "flask", "run", "-h", "0.0.0.0"]
