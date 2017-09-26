# dictionary helper

def compareDictByKey(dict1, dict2):
    # dictionaries are unordered, so we can keep keys in a set and compare set
    s1 = set(dict1.keys())
    s2 = set(dict2.keys())
    s0 = s1.difference(s2)
    return len(s0)==0

# feat0: dict
# feat1: dict
def matchFeature(feat0, feat1):
    keymatch =  compareDictByKey(feat0, feat1)
    valmatch = 0.0
    if keymatch:
        # try value match
        for k in feat0.keys():
            v0 = feat0[k]
            v1 = feat1[k]
            valmatch += (v0 == v1)
        valmatch /= len(feat0)
    return valmatch