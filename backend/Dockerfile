FROM python:3.11

WORKDIR /code
COPY ./ /code

RUN pip3 install pipenv && \
    pipenv --python /usr/local/bin/python sync

CMD [ "pipenv", "run", "python", "src/routes.py" ]
