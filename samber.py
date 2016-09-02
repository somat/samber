#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psutil

class Samber():
    def gen_process(self):

        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['username', 'exe', 'pid', 'name' ])
            except psutil.NoSuchProcess:
                pass
            else:
                yield pinfo


    def get_user_process(self):
        gen = self.gen_process()
        filtered_gen = (item for item in gen if item['username'] != 'root')

        return filtered_gen


if __name__ == '__main__':
    samber = Samber()
    proc = samber.get_user_process()

    for item in proc:
        print item