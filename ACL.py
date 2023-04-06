acl1 = int(input("Ingrese el numero de la ACL :"))

if acl1 >= 0 and acl1 <=99:
    print("El numero "+ str(acl1)," Es una ACL ESTANDAR")
elif acl1 >= 1300 and acl1 <=1999:
    print("El numero "+ str(acl1),"Es una ACL ESTANDAR")
elif acl1 >= 100 and acl1 <=199:
    print("El numero "+ str(acl1),"Es una ACL EXTENDIDA")
elif acl1 >= 2000 and acl1 <=2699:
    print("El numero "+ str(acl1),"Es una ACL EXTENDIDA")            
else:
    print("Este valor no corresponde a una lista de acceso")