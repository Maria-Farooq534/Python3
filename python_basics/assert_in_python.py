assert type(5//2) == int
# assert type(5.0//2) == int # gives error bcz its result is float not int

lst = ['a' , 'b' , 'c','d']
first_type = type(lst[0]) # check the type of first element in lst and store it in first_type variable
                           # first_type variable is highlight bcz it has python built in type.

for item in lst:
    print(item)
    assert type(item) == first_type # code run smoothly bcz all the elements of list have same type 'string'

print(" ") # space

lst2 = ['a' , 'b' , 'c' , 17]

first_type_2 = type(lst2[0]) # get the type of 1st element from the lsit.

for i in lst2:
    
    print(i)
    #assert type(i) == first_type_2  #This is going to give an error bcz the last item in int , and  is != to str



lst3 = [1,2,3]

assert len(lst3) < 10 # True
assert len(lst3) >5 #False , error