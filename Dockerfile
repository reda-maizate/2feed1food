FROM python:3.7.7

RUN pip3 install pipenv

ENV PROJECT_DIR usr/src/2feed1food

WORKDIR ${PROJECT_DIR}

COPY . .

RUN  pip install --upgrade pip &&  pip install pipenv && pipenv install --skip-lock

EXPOSE 5000

ENV FLASK_APP=run.py

CMD ["pipenv", "run", "flask", "run", "-h", "0.0.0.0"]
