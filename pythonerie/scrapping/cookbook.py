# import requests
# import json
# results = requests.get("http://172.18.0.2/users")
# data = json.loads(results.content)
# for user in data :
# 	print(user["mail"])
	


# import requests
# import json
# results = requests.get("http://172.18.0.2/users")
# data = json.loads(results.content)
# blood_groups = set()
# for user in data :
# 	blood_groups.add(user["blood_group"])
# print(blood_groups)
# blood_groups_lst = list(blood_groups)


# import random
# if random.randint(0, 1) == 0 :
# 	print("I’m printed 50% of the trials")
	


#######  Filter data
# # # si le job des utilisateurs contient le mot engineer (en utilisant le mot-clé in), et si cette condition est vraie, nous ajoutons 
# # # l’utilisateur en question dans une liste dédiée.
# import requests
# import json
# results = requests.get("http://172.18.0.2/users")
# data = json.loads(results.content)
# engineers = []
# for user in data :
# 	if "engineer" in user["job"] :
# 		engineers.append(user)
# 		print(engineers)



######### EXEMPLE SCRAPPER
#### deux paramètres de requête : skip et limit sont souvent rencontrés sur les API de serveurs
import requests
import json

def create_query_parameters(skip = 0, limit = 10):
    return {
        "skip": skip,
        "limit": limit
    }

page_size = 10
skip = 0
limit = page_size 

scrapped_data = []

while True:
    params = create_query_parameters(skip, limit)
    results = requests.get("http://172.18.0.2/users", params)
    if results.status_code >= 200 and results.status_code < 300:
        data = json.loads(results.content)
        scrapped_data += data
    elif results.status_code >= 500:
        print("The server returned an error")
        break
    else:
        print("There is an unmanaged error ")
        break    
    
    if len(data) == 0:
        break

    skip = skip + page_size
    limit = limit + page_size

print(len(scrapped_data))