#!/bin/bash

log() {
    PURPLE='\033[0;35m'
    NC="\033[0m"
    echo -e "${PURPLE}[mutagen]${NC} ${1}"
}

start() {
    log "Starting services..."
    export $(grep -v '^#' .env | xargs) || true
    docker network create mutagen-backend || true
    git submodule foreach "docker compose up -d"
}

stop() {
    log "Stopping services..."
    git submodule foreach "docker compose down"
    docker network rm mutagen-backend
}

update() {
    stop

    log "Updating submodules..."
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
        log "Usage: $0 {stop|start|update}"
        exit 1
        ;;
esac