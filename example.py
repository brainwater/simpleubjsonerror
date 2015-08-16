import simpleubjson


bytestring = b'Dr8@\xbbnR\x8c\xe4\xe1+\x82e\xc0\xea?\x99\x83YWH\xb6\xc1\xfa\xab\x93\xe5\xbat}'

document = {
    "Key1": "Value1",
    "Key2": bytestring,
}

ubjdata = simpleubjson.encode(document)

decoded = simpleubjson.decode(ubjdata)

for key in document:
    if document[key] != decoded[key]:
        print("Error, non matching key:", key)


