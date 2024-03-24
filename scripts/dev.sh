#!/bin/bash

docker-compose up api db -d
pushd web
npm run dev
popd