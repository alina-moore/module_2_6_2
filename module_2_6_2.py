def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    
print_params() #ok 1 строка True

#print_params(2, 3, 5, 6) #ошибка

print_params(b = 25) #ok 1 25 True

print_params(c = [1,2,3]) #1 строка [1, 2, 3]

c = [1, 2, 3]
print_params(*c)  #ok 1 2 3

values_list = [1, True, "Hello"]
print_params(*values_list)  #ok 1 True Hello


values_dict = {"a" : 173 , "b" : False, "c" : "Bye-bye"}
print_params(**values_dict) #ok 173 False Bye-bye


values_list_2 = [True, 15]
print_params(*values_list_2, 42) #ok True 15 42

