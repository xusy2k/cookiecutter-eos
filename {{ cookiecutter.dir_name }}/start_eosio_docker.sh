#!/usr/bin/env bash
set -o errexit

# change to script's directory
cd "$(dirname "$0")/eosio_docker"

if [ -e "data/initialized" ]
then
    script="./scripts/continue_blockchain.sh"
else
    script="./scripts/init_blockchain.sh"
fi

echo "=== run docker container from the eosio/eos-dev image ==="
docker run --rm --name {{ cookiecutter.eosio_container }} -d \
-p 8888:8888 -p 9876:9876 \
--mount type=bind,src="$(pwd)"/contracts,dst=/opt/eosio/bin/contracts \
--mount type=bind,src="$(pwd)"/scripts,dst=/opt/eosio/bin/scripts \
--mount type=bind,src="$(pwd)"/data,dst=/mnt/dev/data \
-w "/opt/eosio/bin/" eosio/eos-dev:{{ cookiecutter.eos_dev_tag }} /bin/bash -c "$script"


if [ "$1" != "--nolog" ]
then
    echo "=== follow {{ cookiecutter.eosio_container }} logs ==="
    docker logs {{ cookiecutter.eosio_container }} --follow
fi
