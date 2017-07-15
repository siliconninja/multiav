import pprint
from multiav.core import CMultiAV, AV_SPEED_MEDIUM

path = '/root/malware'

multi_av = CMultiAV('config.cfg')
ret = multi_av.scan(path, AV_SPEED_MEDIUM)
pprint.pprint(ret)