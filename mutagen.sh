#!/bin/bash

start() {
    echo "Starting services..."
    export $(grep -v '^#' .env | xargs) } || true
    docker network create mutagen-backend || true
    git submodule foreach "docker compose up -d"
}

stop() {
    echo "Stopping services..."
    git submodule foreach "docker compose down"
    docker network rm mutagen-backend
}

update() {
    stop

    echo "Updating submodules..."
    git fetch && git pull
    git submodule update --recursive

    start
}

case "$1" in
    "start")
        start
        ;;
    "stop")
        stop
        ;;
    "update")
        update
        ;;
    *)
        echo "Usage: $0 {stop|start|update}"
        exit 1
        ;;
esac