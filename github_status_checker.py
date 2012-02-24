import argparse
import requests
import simplejson

# super secret status API
url = 'https://status.github.com/status.json'

# status codes
# ordered by anti-rainbow, also octocat happiness level
status_code = {
    'good': 0,
    '?': 1,
    'majorproblem': 1
}

def check_status(verbose=False):
    r = requests.get(url)
    r.raise_for_status()
    s = simplejson.loads(r.text)
    status, last_updated = s['status'], s['last_updated']
    if verbose:
        print "Github status %s on %s" % (status, last_updated)
    return status_code[status]
    
def main():
    parser = argparse.ArgumentParser(description="GitHub status checker.")
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                        help="print status to stdout")
    args = parser.parse_args()
    check_status(args.verbose)

if __name__ == '__main__':
    main()
