my_dict = dict()
print(type(my_dict))


#or 

my_dict = {}
print(type(my_dict))

# exemple
my_dict = {
	"this is a key" : "this is a value", 
	"this is a second key" : "this is a value associated to the second key"
}



#taille d'un dictionnaire
my_dict = {"key1" : 0, "key2" : [1,2,3]}
print(len(my_dict))


#concaténation dictionnaire

my_dict_1 = {"key1" : 0, "key2" : [1,2,3]}
my_dict_2 = {"key2" : 0, "key3" : "i’m a value"}
my_dict_1.update(my_dict_2)
print(my_dict_1)
