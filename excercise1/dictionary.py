data={100:'Ravi' ,101:'Vijay' ,102:'Rahul'}
print (data)


plant={}
plant[1]='Dina'
plant[2]='Mani'
plant['name']='bobo'
plant[4]='josh'
print (plant[2] )
print (plant['name'])
print (plant[1])
print (plant)

data1={'Id':11, 'Name':'Dinamani', 'Profession':'Faculty'}
data2={'Id':12, 'Name':'joshila', 'Profession':'Faculty'}
print ("Id of 1st employer is",data1['Id'])
print ("Id of 2nd employer is",data2['Id'])
print ("Name of 1st employer:",data1['Name'])
print ("Name of 2nd employer:",data2['Name'])
print ("Profession of 1st employer:",data1['Profession'])
print ("Profession of 2nd employer:",data2['Profession'])


data2['Name']='Bobo'
data1['Profession']='Manager'
data2['Salary']=20000
data1['Salary']=35000
print (data1)
print (data2)