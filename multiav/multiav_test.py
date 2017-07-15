# -*- coding: utf-8 -*-

from pprint import pprint
import os
from multiav.core import CMultiAV, AV_SPEED_ALL

def scan(path):
    multi_av = CMultiAV('./config.cfg')

    for file_dir in os.listdir(path):
        print file_dir + ':'
        scan_path = os.path.join(path, file_dir)
        ret = multi_av.scan(scan_path, AV_SPEED_ALL)
        AV_result_list = []
        for file in os.listdir(scan_path):
            for AV_engin, AV_result in ret.items():
                for file_path, malware in AV_result.items():
                    AV_result_list.append('%s : %s : %s' % (file, AV_engin, malware))
        for r in AV_result_list:
            print r

scan('/home/xiao/github/multiav/files')