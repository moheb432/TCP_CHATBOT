import socket as sk
import threading
import pickle

V_S=[{"heart rate",60},{'temp',35},{'bloodpressure',"180/60"}]
V_S=pickle.dumps(V_S)
HOST = sk.gethostbyname(sk.gethostname())
s = sk.socket(sk.AF_INET, sk.SOCK_STREAM) 
s.connect((HOST, 5555))

s.sendall(V_S)
nick=input("hello mr please enter you nickname : ")

questions=["do you have fever : ",
      "do you have diarria : ",
      "do you have heartburn : " ,
      "do you have difficult in breathing : ",
      "do you have vomiting : "]
ans1=[]
print(f"please mr {nick} answer following quetion with 1 or 0 only :\nplease choose f&v")
    
for ques in questions:
    ans=int(input(ques))
    if (ans==0 or ans==1):        
        ans1.append(ans)
    else :
        print('wrong answer please try again')
        continue
       
s.sendall(str(ans1).encode('ascii'))
data = s.recv(1024)
print(data.decode('ascii'))