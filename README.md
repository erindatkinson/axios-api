# Mozilla React tutorial with axios api

![image of grape hyacinth](.github/assets/grape-hyacinth-8555017_1920.jpg)
Image by [Heike Tönnemann](https://pixabay.com/users/heikiwi-35444888/)

## Introduction

A small buildout of the [Mozilla react tutorial](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/React_todo_list_beginning) but with initial hooks into a Flask API backended by Postgres.

## Running

```sh
docker-compose up
```

will start the three services: `api`, `web`, and `db`
at which point you should be able to connect to http://localhost:8080 and persist tasks to the db via the api.

💜
