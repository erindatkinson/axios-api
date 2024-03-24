setup:
	scripts/setup.sh

dev:
	scripts/dev.sh

build: build-all
build-all: build-web build-api

build-web:
	docker-compose build web --no-cache

build-api:
	docker-compose build api --no-cache

.PHONY: build build-all build-web build-api
