#!/bin/bash

setup_api() {
    if !command -v pip &> /dev/null
    then
        echo "Please install python/pip"
        exit 1
    fi

    if ! command -v pipenv &> /dev/null
    then
        pip install pipenv
    fi
    pushd api
    pipenv install
    popd
}

setup_web() {
    if ! command -v npm &> /dev/null
    then
        echo "Please install npm"
        exit 1
    fi

    pushd web
    npm install
    popd
}

setup_api
setup_web
