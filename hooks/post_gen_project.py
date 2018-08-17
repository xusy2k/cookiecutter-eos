#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
ERROR = "\x1b[1;31m [ERROR]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def apply_patch(major, minor, patch):
    if major >= 1 and minor >= 2:
        for file_name in ['init_blockchain.sh', 'continue_blockchain.sh']:
            filepath = os.path.join(os.getcwd(),
                                    'eosio_docker', 'scripts', file_name)
            with open(filepath) as f:
                filedata = f.read()
            filedata = filedata.replace(
                '--plugin eosio::wallet_plugin', ' ')
            filedata = filedata.replace(
                '--plugin eosio::wallet_api_plugin', ' ')
            if file_name == 'init_blockchain.sh':
                filedata = filedata.replace('cleos wallet create -n',
                                            'cleos wallet create --to-console -n')

            with open(filepath, 'w') as f:
                f.write(filedata)


def check_eos_dev_tag(eos_dev_tag):
    if eos_dev_tag == 'latest':
        pass
    else:
        eos_dev_tag_list = eos_dev_tag.replace('v', '').split('.')
        if len(eos_dev_tag_list) == 3:
            try:
                major = int(eos_dev_tag_list[0])
                minor = int(eos_dev_tag_list[1])
                patch = int(eos_dev_tag_list[2])
                apply_patch(major, minor, patch)
            except (TypeError, ValueError, UnboundLocalError) as e:
                print('\n{}ERROR:\n\n{}\'{}\'{} {}\n {}'.format(
                    ERROR, WARNING, eos_dev_tag, ERROR, e, TERMINATOR))
        else:
            print('\n{}ERROR:\n\n{}\'{}\'{} has not a valid format\n {}'.format(
                ERROR, WARNING, eos_dev_tag, ERROR, TERMINATOR))


def main():
    dir_name = '{{ cookiecutter.dir_name }}'
    check_eos_dev_tag('{{ cookiecutter.eos_dev_tag }}')
    print(SUCCESS + "Project initialized! For quickstart: \n\n" +
          "cd " + dir_name + "; ./quick_start.sh\n" + TERMINATOR)


if __name__ == "__main__":
    main()
