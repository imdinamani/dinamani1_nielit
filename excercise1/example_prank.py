import os
#from string import digits
a= os.listdir('C:\\Users\\Dinamani\\Desktop\\prank')
print (a)

os.chdir('C:\\Users\\Dinamani\\Desktop\\prank')
#os.renames.a.strip("0123456789")
for file in a:
    o_name= file
    print (o_name)
   # n_name = o_name.strip("digits")
    n_name= o_name.strip("0123456789")
    print (n_name)
   # os.rename(file_name, file_name.strip("0123456789"))
    os.rename(o_name, n_name)
    print (os.getcwd())