# import socket
# my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# uri = "172.18.0.2"
# for port in range(65536):
#     destination = (uri, port)
#     connection_result = my_socket.connect_ex(destination)
#     print("Port", port, "responded", connection_result)
#     my_socket.close()


integers = (i for i in range(100))
print(integers)


# symmetric_integers = ((i, -i) for i in range(100))
# print(symmetric_integers)