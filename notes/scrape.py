'Learn the skill of "Screen scraping":  Capturing useful data from HTML'

import urllib
import re

url = 'https://pypi.python.org/pypi'

def number_of_packages():
    'Return the current number of packages on PyPI'
    u = urllib.urlopen(url)
    page = u.read()
    mo = re.search(r'(\d+)(?:\s*</strong>)?\s*packages', page)
    return int(mo.group(1))

if __name__ == '__main__':
    print number_of_packages()
