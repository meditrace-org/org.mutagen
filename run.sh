git submodule foreach "docker compose down"
git submodule update --recursive
git submodule foreach "docker compose up -d"
