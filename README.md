# Example simpleubjson error

### Setup
From the directory containing this README file, simply run the environmentsetup.bash script. It requires that you have python-virtualenv or python3-virtualenv installed.
```bash
$ cd simpleubjsonerror
$ ./environmentsetup.bash
```

### Running
After activating the virtualenvironment, simply run the example.py file
```bash
$ cd simpleubjsonerror
$ . env/bin/activate
$ python example.py
```

When I run this, I get the error:
```
$ python example.py 
Traceback (most recent call last):
  File "/home/blake/code/minprojs/simpleubjsonerror/env/lib/python3.4/site-packages/simpleubjson/draft9.py", line 425, in encode_bytes
    obj.decode('utf-8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbb in position 4: invalid start byte

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "example.py", line 11, in <module>
    ubjdata = simpleubjson.encode(document)
  File "/home/blake/code/minprojs/simpleubjsonerror/env/lib/python3.4/site-packages/simpleubjson/__init__.py", line 85, in encode
    res = _draft9_encoder(default).encode_next(data)
  File "/home/blake/code/minprojs/simpleubjsonerror/env/lib/python3.4/site-packages/simpleubjson/draft9.py", line 372, in encode_next
    return bytes().join(res)
  File "/home/blake/code/minprojs/simpleubjsonerror/env/lib/python3.4/site-packages/simpleubjson/draft9.py", line 468, in encode_dict
    yield self.encode_next(value)
  File "/home/blake/code/minprojs/simpleubjsonerror/env/lib/python3.4/site-packages/simpleubjson/draft9.py", line 367, in encode_next
    res = self.dispatch[tobj](self, obj)
  File "/home/blake/code/minprojs/simpleubjsonerror/env/lib/python3.4/site-packages/simpleubjson/draft9.py", line 427, in encode_bytes
    raise EncodeError('Invalid UTF-8 byte string: %r' % obj)
simpleubjson.exceptions.EncodeError: Invalid UTF-8 byte string: b'Dr8@\xbbnR\x8c\xe4\xe1+\x82e\xc0\xea?\x99\x83YWH\xb6\xc1\xfa\xab\x93\xe5\xbat}'
```