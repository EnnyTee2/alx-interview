#!/usr/bin/python3
""" Log Parsing """

import sys
import re


match = '.*\..*\..*\..*\s\-\s\[.*?]\s".*"\s(200|301|400|401|403|404|405|500)\s(\d*)'

line_count = 0
total_size = 0
status_code = ['200', '301', '400', '401', '403', '404', '405', '500']
status_count = dict([(code, 0) for code in status_code])

def initialize():
    global line_count
    global total_size

    line_count = 0
    total_size = 0
    for code in status_code:
        status_count[code] = 0
    return

def status_writer():
    global line_count
    global total_size

    for line in sys.stdin:
        if line_count == 10:
            print(f"File size: {total_size}")
            for status_code,number in status_count.items():
                print(f"{status_code}: {number}")
            initialize()

        capture = re.findall(match, line)
        try:
            total_size += int(capture[0][1])
            status_count[capture[0][0]] += 1
        except IndexError:
            line_count += 1
            continue

        line_count += 1
    
try:
    while True:
        status_writer()

except KeyboardInterrupt:
    initialize()
    status_writer()
