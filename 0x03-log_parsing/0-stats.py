#!/usr/bin/python3
""" A script for log parsing from stdin"""


import sys
import re


match = r'.*\..*\..*\..*\s\-\s\[.*?]\s".*"\s(200|301|400|401|403|404|405|500)\s(\d*)'

def status_writer():
    """ Extracts the data fields from the stream
        and prints the status log
    """
    line_count = 0
    total_size = 0
    status_code = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_count = dict([(code, 0) for code in status_code])

    try:
        for line in sys.stdin:
            capture = re.findall(match, line)
            try:
                total_size += int(capture[0][1])
                status_count[capture[0][0]] += 1
            except IndexError:
                continue
            line_count += 1
            
            if line_count == 10:
                line_count = 0
                print(f"File size: {total_size}")
                for status_code, number in status_count.items():
                    if number != 0:
                        print(f"{status_code}: {number}")

    except KeyboardInterrupt:
        print(f"File size: {total_size}")
        for status_code, number in status_count.items():
            if number != 0:
                print(f"{status_code}: {number}")


if __name__ == '__main__':
    status_writer()
