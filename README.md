# Scyll4

Small python script to use Scyll4 API

```
usage: scylla.py [-h] [-c COUNT] [-o OFFSET] [-t TYPE] [-q QUERY] [-C] [-b] [-s SAVE]

Python script to use Scyll4 API

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        number of records to retrieve (default is 500)
  -o OFFSET, --offset OFFSET
                        record start offset value (default is 0)
  -t TYPE, --type TYPE  Type of record data to search for (email, user_id, user, name, ip, pass_hash, password, pass_salt, domain)
  -q QUERY, --query QUERY
                        query to search
  -C, --combo           Combo output user:pass only
  -b, --beautify        Beautify json
  -s SAVE, --save SAVE  Save Scylla results to output file
```