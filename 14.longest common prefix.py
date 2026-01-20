strs=['flower','flow','flight']
if not strs:
    print("")
prefix=strs[0]
for i in strs[1:]:
    while i.find(prefix)!=0:
        prefix=prefix[:-1]
        if not prefix:
            print(" ")
print(prefix)

        