# -*- coding: utf-8 -*-

from pprint import pprint
import time
import os
from core import CMultiAV, AV_SPEED_ALL

def exeTime(func):
    def newFunc(*args, **args2):
        t0 = time.time()
        back = func(*args, **args2)
        print "             %.3fs taken" % (time.time() - t0)
        return back
    return newFunc

@exeTime
def call_multiav(scan_path):
    multi_av = CMultiAV('./config.cfg')
    ret = multi_av.scan(scan_path, AV_SPEED_ALL)
    AV_result_list = []
    for file in os.listdir(scan_path):
        for AV_engin, AV_result in ret.items():
            for file_path, malware in AV_result.items():
                AV_result_list.append('%s : %s : %s' % (file, AV_engin, malware))
    for r in AV_result_list:
        print '             '+ r

def scan(path):
    for file_dir in os.listdir(path):
        print file_dir + ':'
        scan_path = os.path.join(path, file_dir)
        #sta = time.time()
        call_multiav(scan_path)
        #end = time.time()
        #cost = end-sta
        #print cost

if __name__ == "__main__":
    scan('/home/xiao/github/files')