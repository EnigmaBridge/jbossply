#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'dusanklinec'


import jbossparser
import fileinput
import json


def main():
    """
    Reads stdin jboss output, writes json on output
    :return:
    """
    buff = ''
    for line in fileinput.input():
        buff += line

    parser = jbossparser.JbossParser()
    result = parser.parse(buff)
    print(json.dumps(result))


if __name__ == '__main__':
    main()

