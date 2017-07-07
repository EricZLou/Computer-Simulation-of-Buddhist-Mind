# generic JSON encoder to help with inheritance
import json

def makeJSON(obj):
    if hasattr(obj, 'makejson'):
        return obj.makejson()
    else:
        return obj.__dict__

# how to build up a class hierarchy from a json or dict from json?
def makeobj(jobj):
    #jobj = json.loads(jmsg)
    # jobj = dict()
    classname = [x for x in jobj.keys()][0]
    print(classname)
    #obj = makeObjectFromDict(classname, jobj[classname])
    # unless object can be constructed with a dictionary or by class factory
    # can we do match purely based on json string or unpacked python (nested) dictionary?

# generic JSON match algorithm
# jmsg: json string
# features: set of names
def matchJSONFeature(jmsg, features):
    return 1.0

'''
# example showing nested JSON encoding!
import json

class Identity:
    def __init__(self):
        self.name="abc name"
        self.first="abc first"
        self.addr=Addr()
    def reprJSON(self):
        return dict(name=self.name, firstname=self.first, address=self.addr)

class Addr:
    def __init__(self):
        self.street="sesame street"
        self.zip="13000"
    def reprJSON(self):
        return dict(street=self.street, zip=self.zip)

class Doc:
    def __init__(self):
        self.identity=Identity()
        self.data="all data"
    def reprJSON(self):
        return dict(id=self.identity, data=self.data)

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)
'''