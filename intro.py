'''print(2+2)
print('w')
print("w")
print("how are you")
print("peter said 'he won't be here today'")
print('peter "said he won\'t be here today"')


#Data types
print(type('w'))
print(type(2+2))
print(type(11.5))
print(type(True))
print(type(11.5j))
print('WOW')


#Variables and string
cr= 'cristiano ronaldo'
print(cr)
c_=3
e4= 'hello'
_v= 'happy coding'
_4d=12
print(c_,e4,_v,_4d)


#Concatenation (adding two strings together)
greeting= "Good afternoon "+cr
print(greeting)

book= "i have a book called"+" "+cr
print(book)


#Adding a string and number
lucky_number= "you just won a car with lucky number"+" "+str(_4d)
print(lucky_number)

lucky_number= 'you just won a car with lucky number '+str(_4d)
print(lucky_number)

lucky_number= f"you just won a car with lucky number {_4d}"
print(lucky_number)

print(lucky_number.replace('you','I',))
print(lucky_number.replace('car','bicycle'))

#string methods
user= "benny"
print(user.upper())

user= "BENNY"
print(user.lower())

user="benny"
print(user.title())

user= "Benny"
print(user.casefold())

user= "benny him"
print(user.capitalize())

user= "benny him"
print(user.title())


#INDEX
print(lucky_number.index('car'))


#slicing
just=lucky_number[4:8]
print(just)


#STRING CONTINUATION
# Format method

fname= 'Benard'
lname= 'Jerry'
middle_name= 'Andrew'
full_name= "{} {} {}".format(lname,fname,'paul')
print(full_name)

winner= "you just won the number {}".format(40)
print(winner)

n= "welcome to class %s %s %s" %(fname,lname,middle_name)
print(n)

number= 123.64262427743
print("this number %d is formatted to 2 decimal place" %(number))
print("this number %s is formatted to 2 decimal place" %(number))


#strip
b= "         Henry"
print(b.strip())

v= '                  kenndrie'
y= 'hope        '
print(v.lstrip())
print(y.rstrip()+"  "+fname)


#count
print(n.count('e'))
h= f"i have the number {33}"
print(h.count('3'))

#partition
k= full_name.partition('Jerry')
print(k)
print(k[0])
print(k[1])
print(k[2])
print(k[1][0])

jk= "This cat of mine misbehaves everyday"
print(jk.index('T'))
print(jk.partition('cat'))
print(jk.partition('cat')[1])

ee= jk.partition('cat')
print(ee[0])
print(ee[0][1])
print(ee[0], ee[1])


#split
js= "i have a bicycle"
yy= js.split()
print(yy)
print(yy[1])
print(yy[1][2])
print(yy[1],yy[2])


#find
print(js.find('bicycle'))


#integers
#number arithmretic
n= 1
b= 2
print(n+b) #addition
print(b-n) #multiplication
print(15/3) #division
print(2*5) #multiplication
print(15//3) #floor division
print(15%2) #modulus(always shows us a reminder)
print(2**5) #power multiplication
print(pow(2,5)) #power multiplication
nn= -34
print(abs(nn)) # (absolute) changing the negative to positive

print(5.3*2.8)
print(6.2*2)
print(11+5j+2)
print(12.3+11j*3)
print((12.3+11j)*3)

bx=11.345667788888888
print(round(bx,3))

#OPERATORS
#arithmetric operator
#comparism operator
#assignment operator
#bitwise operator '''

name= 'jack'
text= 'Today is wednesday'

print(name=='paul') #Equals to
print(name !='paul') #Not equals to
print('is' in text) #membership

num1,num2,num3= 10,12,10
print(num1<num2)
print(num1>num2)

