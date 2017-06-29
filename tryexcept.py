a=10
b=1
try:
   c=a/b
   print (c)
except Exception as e:
    print(e.message)
else:
    print("everything is ok")