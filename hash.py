import hashlib
c={}
for i in range (1000,10000):
    i=str(i)
    b=(hashlib.sha256((i).encode('utf-8')).hexdigest())
    c[i]=b
newc={value:key for key, value in c.items()}
print(newc['85432a9890aa5071733459b423ab2aff9f085f56ddfdb26c8fae0c2a04dce84c'])
