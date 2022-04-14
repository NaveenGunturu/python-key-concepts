listx=[34,353,534,344,53,43,356,34,534,6,34,53,5,35,34,534,534,3,34]
result=filter( lambda x:True if x%2==0 else False,listx)
print(list(result))

result2 = filter(lambda x:True if x>1000 else False,listx)
print(list(result2))
#filter also needs a callback to be passed
# the callback has to return boolean and the callback will be called for each
# each element in the collection if the callback returns true the element
# would be kept in tact otherwise filter will be called
# in the result only filtered elements ll be present 
# if the input list has n elements output list will have <=n elements