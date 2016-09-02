#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apt

class CheckApt(object):

    def __init__(self):
        self.cache = apt.Cache()

    def list_installed(self):
        pkgs = [i for i in self.cache if i.is_installed]

        return pkgs

def main():
    check = CheckApt()
    p = check.list_installed()

    for i in p:
        print i.name

if __name__ == '__main__':
    main()
