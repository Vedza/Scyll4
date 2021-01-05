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
$ python3 scylla.py -t "username" -q "admin" -b -c 1 -o 9 
[
    {
        "id": "08e7105b287bb60f70d245c9910f3a78",
        "fields": {
            "username": "Admin",
            "domain": "hostinger.com",
            "ip": "79.102.128.13",
            "password": "lt184577770",
            "email": "mielupis@gmail.com"
        }
    }
]
```

``` sh
$ python3 scylla.py -t "name" -q "John Doe" --beautify --count 1 --offset 40 
[
    {
        "id": "028da885127160204e848656e311288e",
        "fields": {
            "domain": "000webhost.com",
            "name": "john doe",
            "ip": "12.48.220.131",
            "password": "18jam93",
            "email": "jdoedjoh@aol.com"
        }
    }
]
```

``` sh
$ python3 scylla.py -t "email" -q "*JohnDoe*" --count 2 --offset 2 --combo
johndoe@hotmail.com:sprite
johndoe021@gmail.com:combsoma47
```
