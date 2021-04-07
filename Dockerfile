FROM python:3.7.7

RUN pip3 install pipenv

ENV PROJECT_DIR /code

WORKDIR ${PROJECT_DIR}

COPY . .

RUN  pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["run.py"]
