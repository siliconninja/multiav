# -*- coding: utf-8 -*-

from pprint import pprint
import time
import os
from core import CMultiAV, AV_SPEED_ALL

def call_multiav(scan_path):
    multi_av = CMultiAV('./config.cfg')
    ret = multi_av.multi_scan(scan_path, AV_SPEED_ALL)
    AV_result_list = []
    for file in os.listdir(scan_path):
        for AV_engin, AV_result in ret.items():
            for file_path, malware in AV_result.items():
                AV_result_list.append('%s : %s : %s' % (file, AV_engin, malware))
                break
    return AV_result_list

def scan(path):
    count = 1
    total_cost = 0.0
    total = len(os.listdir(path)[0:100])
    for file_dir in os.listdir(path)[0:100]:
        print '(%d/%d)%s :' % (count, total, file_dir)
        scan_path = os.path.join(path, file_dir)
        t0 = time.time()
        AV_result_list = call_multiav(scan_path)
        cost = time.time() - t0
        for r in AV_result_list:
            print '             '+ r
        print "             %.3fs taken" % (time.time() - t0)
        count += 1
        total_cost += cost
    ava_cost = total_cost/total
    return ava_cost

if __name__ == "__main__":
    re = scan('/home/xiao/text/')
    print re