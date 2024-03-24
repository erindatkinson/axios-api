FROM python:3.12
RUN pip install pipenv
RUN mkdir /opt/app
WORKDIR /opt/app
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install
COPY . .
ENTRYPOINT [ "pipenv", "run", "gunicorn", "--bind", "0.0.0.0:5000", "-w", "4", "app:app" ]