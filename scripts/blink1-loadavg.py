#!/usr/bin/python

import re
from subprocess import call
from subprocess import check_output
from time import sleep

# Change this to the number of CPU cores (not physical or virtual processors)
# in your system. Added because 1.0 load on a multicore system does not
# actually mean 100% CPU load.
NUM_CORES = 1 

LOAD_RE = re.compile('.+averages:\s(\d+\.\d+)\s(\d+\.\d+)\s(\d+\.\d+)')

if __name__ == '__main__':
    print 'Modulating blink(1) to the load averages...'
    print ''
    print 'Press Ctrl+C to quit.'
    try:
        while True:
            load_averages = LOAD_RE.match(check_output(['uptime'])).groups()
            one, five, fifteen = [(float(l) / NUM_CORES) * 255 for l in load_averages]
            params = ['blink1-tool', '-q']
            if one > 255 or five > 255 or fifteen > 255:
                m = max(one, five, fifteen)
                one *= 255 / m
                five *= 255 / m
                fifteen *= 255 / m
                rgb_val = '{0:.0f},{1:.0f},{2:.0f}'.format(one, five, fifteen)
                params += ['--rgb', rgb_val]
                if one > 1275 or five > 1275 or fifteen > 1275:
                    params += ['-m', '250', '--blink', '20']
                else:
                    params += ['-m', '500', '--blink', '10']
                call(params)
            else:
                rgb_val = '{0:.0f},{1:.0f},{2:.0f}'.format(one, five, fifteen)
                params += ['-m', '5000', '--rgb', rgb_val]
                call(params)
                sleep(5)
    except KeyboardInterrupt:
        pass