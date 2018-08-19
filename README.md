# Cookiecutter EOS

![EOS 1.1.x](https://img.shields.io/badge/EOS-1.1.x-green.svg) ![EOS 1.2.x](https://img.shields.io/badge/EOS-1.2.x-red.svg)

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

- **project_name**: Name of the project. Default value: **My EOS project**
- **app_name**: Name of the main applicaction. Default value: **notechain**
- **dir_name**: Name of the directory to install. Default value: **notechain**
- **eos_dev_tag**: Tag version of eos-dev [docker's image](https://hub.docker.com/r/eosio/eos-dev/tags/). Default value: **v1.1.0**
- **eosio_container**: Name of container. Default value: **notechain_container**
- **default_account**: Name of default account. Default value: **notechai.acc**
- **default_wallet**: Name of default wallet. Default value: **eosiomain**
- **default_contract**: Name of the first contract will be created. Default value: **notechain**
- **default_contract_wallet**: Name of the wallet's contract. Default value: **notechain_wallet**

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

- At this moment it only works on v1.1.x release
