# Scyll4

Small python script to use Scyll4 API

#### Usage
```
usage: scylla.py [-h] [-c COUNT] [-o OFFSET] [-t TYPE] [-q QUERY] [-C] [-b] [-s SAVE]

Python script to use Scyll4 API

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        number of records to retrieve (default is 500)
  -o OFFSET, --offset OFFSET
                        record start offset value (default is 0)
  -t TYPE, --type TYPE  Type of record data to search for (email, user_id, username, name, ip, pass_hash, password, pass_salt, domain)
  -q QUERY, --query QUERY
                        query to search
  -C, --combo           Combo output username|email:pass only
  -b, --beautify        Beautify json
  -s SAVE, --save SAVE  Save Scylla results to output file
```

#### Examples

``` sh
$ python3 scylla.py -t "username" -q "*admin*" -C      
Admin:lt184577770
admin:aa1234
eepadmin:0842875692a
Adminnin:tanin123
...

$ python3 scylla.py -t "name" -q "*johndoe*" -b -c 1
[
    {
        "id": "78fada045575e0f65f10362962e8294e",
        "fields": {
            "domain": "twitter.com",
            "password": "therock",
            "name": "johndoe1@gmail.com"
        }
    }
]

```
