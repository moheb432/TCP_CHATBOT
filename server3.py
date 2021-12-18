import socket as sk
import threading
import pickle
host_IP = sk.gethostbyname(sk.gethostname())
server =sk.socket(sk.AF_INET,sk.SOCK_STREAM)
print(host_IP)

questions = ['what do you suffer from ?',"fever"]
server.bind((host_IP,5555)) 

clients = {} 
diseases=['fever','diarria','heartburn','breath_diff','vomiting']

def initial_diag(mess,client):
    f=int(mess[0])#fever
    d=int(mess[1])#diarria
    hb=int(mess[2])#heartburn
    bd=int(mess[3])#breathing diff
    v=int(mess[4])#vomiting
    if v&d:
        client.sendall('you had stomach flu suggested pill : antinnal '.encode('ascii'))
    if f&v&bd:
        client.sendall('you had covid-19 please Consult a doctor ASAP'.encode('ascii'))
    if f&v&bd:
        client.sendall('you had covid-19 please Consult a doctor ASAP'.encode('ascii'))
    print(f"responded to {client}")
    return
        
def NEW_client(client,address):
    print(f"\nNEW CONNECTION {address} connected.")
    new_c=1
    client.settimeout(20)
    message = pickle.loads(client.recv(1024))
    client.settimeout(None)
    
    print(f"\nvital signs : {message}")
    
    while new_c:
        try:
            client.settimeout(20)
            message = client.recv(1024).decode('ascii')
            
            client.settimeout(None)
            if message=="disconnect" :
                print(f"{address} is disconnected ")
                new_c=0
                continue 
            if message :
                mess=list(message.strip("[").strip("]").split(","))
                clients.update({address[1]:mess})
                initial_diag(mess,client)
               
   
                
                
                
        except:
            client.sendall('{} left!'.format(address[1]).encode('ascii'))
            break
    
    del clients[address[1]]    
    client.close()             
        
def connect ():
    print("server is on ")
    server.listen()
    while (1):
        client,address=server.accept()
        thread=threading.Thread(target=NEW_client,args=(client, address))
        thread.start() 
        print(f'clients = {threading.activeCount()}')
        
def receive():
        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=NEW_client, args=(client,))
        thread.start()

connect()