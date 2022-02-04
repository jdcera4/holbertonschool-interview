#!/usr/bin/python3
"""
0x06. Log Parsing, task 0. Log parsing
Parses a log of HTTP GET request results from stdin to tabulate the total
counts of status codes appearing in each response, and the total file size
across all requests.
Example of expected log line input:
128.230.61.246 - [2017-02-05 23:31:23.258076] \
"GET /projects/260 HTTP/1.1" 301 292
Fields:
<IP Address> - [<date>] "<GET request>" <response status code> <file size>
"""


import sys

if __name__ == "__main__":

    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    file_size = [0]
    count = 1

    def print_stats():
        '''
        Prints file size and stats for every 10 loops
        '''
        print('File size: {}'.format(file_size[0]))

        for code in sorted(status_codes.keys()):
            if status_codes[code] != 0:
                print('{}: {}'.format(code, status_codes[code]))

    def parse_stdin(line):
        '''
        Checks the stdin for matches
        '''
        try:
            line = line[:-1]
            word = line.split(' ')
            # File size is last parameter on stdout
            file_size[0] += int(word[-1])
            # Status code comes before file size
            status_code = int(word[-2])
            # Move through dictionary of status codes
            if status_code in status_codes:
                status_codes[status_code] += 1
        except BaseException:
            pass

    try:
        for line in sys.stdin:
            parse_stdin(line)
            # print the stats after every 10 outputs
            if count % 10 == 0:
                print_stats()
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
