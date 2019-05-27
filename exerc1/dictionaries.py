d = {}
# d = dict {"george":24, "tom": 34}
d["george"] = 24 #key is george value is 24
d["tom"] = 32
d["jenny"] =20
print(d["george"])

d["jenny"] = 22
print(d["jenny"]) # keys are strings or numbers

d[10] = 100
print(d[10])
for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)