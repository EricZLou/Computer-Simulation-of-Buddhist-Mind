# generic JSON encoder to help with inheritance
import utils.dicthelper as jut

# test dict compare by keys
dct1 = {'name':'lou','val':3}
dct2 = {'name':'eric','val':4}
rslt = jut.compareDictByKey(dct1, dct2)
print(rslt)  # True

dct3 = {'name':'eric','value':4}
rslt = jut.compareDictByKey(dct1, dct3)
print(rslt)  # False
