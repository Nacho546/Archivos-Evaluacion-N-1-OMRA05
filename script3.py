aclNum = int(input("Cual es el numero ipv4 ACL? "))
if aclNum >= 1 and aclNum <= 99:
    print("Este es un ACL ipv4 estandar.")
elif aclNum >= 100 and aclNum <= 199:
    print ("Este es una ACL ipv4 extendida")
else:
    print("Esta ACL ipv4 no es extendida o estandar .")
    