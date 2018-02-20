import socket


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = []

operation = input(
    """
        Net-Centric Math Server
        
        Please select an operation to perform:
        1 - Addition   2 - Subtraction     3 - Multiplication
                    4 - Division    5 - Modulus
    """
)

message.append(str(operation))

inputa = input('please enter the value a: ')
inputb = input('please enter the value b: ')

message.append(str(inputa))
message.append(str(inputb))

message = ','.join(message)

socket.sendto(message, ('localhost', 5555))

result, server = socket.recvfrom(1024*4)
print('server result: ' + result)

socket.close();
