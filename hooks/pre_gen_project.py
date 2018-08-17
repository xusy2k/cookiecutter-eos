#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import re
import sys

TERMINATOR = "\x1b[0m"
ERROR = "\x1b[1;31m [ERROR]: "
# WARNING = "\x1b[1;33m [WARNING]: "
ERROR = "\x1b[1;31m"
WARNING = "\x1b[1;33m"

MODULE_REGEX = r'^[a-z12345.]+$'


def check_account(default_account):
    if (len(default_account) > 12
            or not re.match(MODULE_REGEX, default_account)):
        print('\n{}ERROR:\n {}\'{}\'{} is not a valid account name.\n\n'
              'By using base32 encoding account names up to 12 characters \n'
              'long consisting of the characters: '
              '[a-z12345.]\n {}'.format(ERROR, WARNING, default_account,
                                        ERROR, TERMINATOR))

        # exits with status 1 to indicate failure
        sys.exit(1)


def check_eos_dev_tag(eos_dev_tag):
    if eos_dev_tag == 'latest':
        print('\n{}ERROR:\n\n{}\'{}\'{} {}\n {}'.format(
            ERROR, WARNING, eos_dev_tag, ERROR, 'Please, use named version',
            TERMINATOR))
        # exits with status 1 to indicate failure
        sys.exit(1)
    else:
        eos_dev_tag_list = eos_dev_tag.replace('v', '').split('.')
        if len(eos_dev_tag_list) == 3:
            try:
                major = int(eos_dev_tag_list[0])
                minor = int(eos_dev_tag_list[1])
                patch = int(eos_dev_tag_list[2])

                if major == 1 and minor >= 2:
                    print('\n{} [WARNING]: \'{}\' is not fully tested\n {}'
                          .format(WARNING, eos_dev_tag, TERMINATOR))
            except (TypeError, ValueError) as e:
                print('\n{}ERROR:\n\n{}\'{}\'{} {}\n {}'.format(
                    ERROR, WARNING, eos_dev_tag, ERROR, e, TERMINATOR))
                # exits with status 1 to indicate failure
                sys.exit(1)
        else:
            print('\n{}ERROR:\n\n{}\'{}\'{} has not a valid format\n {}'
                  .format(ERROR, WARNING, eos_dev_tag, ERROR, TERMINATOR))
            # exits with status 1 to indicate failure
            sys.exit(1)


def main():
    check_account('{{ cookiecutter.default_account }}')
    check_eos_dev_tag('{{ cookiecutter.eos_dev_tag }}')


if __name__ == "__main__":
    main()
