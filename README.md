# Cookiecutter EOS

Creation of the skeleton of necessary files for programming contracts.

## Prerequisites

Install [cookiecutter](https://github.com/audreyr/cookiecutter)

```bash
pip install cookiecutter
```

## Create a project

```bash
cookiecutter gh:xusy2k/cookiecutter-eos
```

It will ask you some parameters:

- **project_name**: Name of the project
- **app_name**: Name of the main applicaction
- **dir_name**: Name of the directory to install
- **eos_dev_tag**: Tag version of eos-dev [docker's image](https://hub.docker.com/r/eosio/eos-dev/tags/)
- **eosio_container**: Name of container
- **default_account**: Name of default account
- **default_wallet**: Name of default wallet
- **default_contract**: Name of the first contract will be created
- **default_contract_wallet**: Name of the wallet's contract

Finally you will get inside **dir_name** all necessary files to begin to work based on repository [eosio-project-boilerplate-simple](https://github.com/EOSIO/eosio-project-boilerplate-simple) but customized for your own values

### Non interactive mode

Cookiecutter also accepts parameter **--no-input** making all parameters as optional. If you don't specify its value it will get its default value.

```bash
cookiecutter --no-input gh:xusy2k/cookiecutter-eos \
    project_name='My EOS Project' \
    app_name=my_chain \
    dir_name=my_chain \
    eos_dev_tag=v1.1.0 \
    eosio_container=my_chain_container \
    default_account=mychain.acc \
    default_wallet=eosiomain \
    default_contract=mycontract \
    default_contract_wallet=mycontract.acc
```

## Caveats

- At this moment it only works on v1.1.x realease
