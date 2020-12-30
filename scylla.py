import json
from collections import OrderedDict
import requests
import argparse
import urllib3

urllib3.disable_warnings()

parser = argparse.ArgumentParser(description='scylla.sh CLI tool')

parser.add_argument('-c', '--count', help='number of records to retrieve (default is 500)', default='500')
parser.add_argument('-o', '--offset', help='record start offset value (default is 0)', default='0')
parser.add_argument('-t', '--type',
                    help='Type of record data to search for (email, user_id, user, name, ip, pass_hash, password, pass_salt, domain)',
                    default='email')
parser.add_argument('-q', '--query', help='query to search')
parser.add_argument('-C', '--combo', action='store_true', help='Combo output user:pass only')
parser.add_argument('-b', '--beautify', action='store_true', help='Beautify json')
parser.add_argument('-s', '--save', help='Save Scylla results to output file')

args = parser.parse_args()

url = "https://scyll4.com/search?q={}:{}*&size={}&start={}".format(args.type, args.query, args.count,
                                                                   args.offset)

response = requests.request("GET", url, verify=False)

if args.combo:
    output = ''
    for p in response.json():
        try:
            output += "{}:{}\n".format(p['fields']['email'], p['fields']['password'])
        except:
            pass
    '\n'.join(list(OrderedDict.fromkeys(output.split('\n'))))
    output.rstrip()

else:
    output = response.json()
    if args.beautify:
        output = json.dumps(output, indent=4)

if args.save:
    file = open(args.save, "w")
    file.write(output)
    file.close()
else:
    print(output)
