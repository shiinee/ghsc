import argparse
import requests
import simplejson

# super secret status API
url = 'https://status.github.com/status.json'

# status codes by color
# ordered by anti-rainbow, also octocat happiness level
status_code = {
    'good': 0,
    '?': 1,
    'majorproblem': 1
}

def check_status():
    r = requests.get(url)
    r.raise_for_status()
    s = simplejson.loads(r.text)
    status, last_updated = s['status'], s['last_updated']
    print "Github status %s on %s" % (status, last_updated)
    return status_code[status]

if __name__ == '__main__':
    check_status()
