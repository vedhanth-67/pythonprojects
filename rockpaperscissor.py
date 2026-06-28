import random 
options=("Rock","Paper","Scissors")
computer=random.choice(options)
player=0
c=0

x=None
while True:
            print("1.Rock,2.Paper,3.Scissor")
            x=input("enter your choice(Q for quit):")
            if x=="Rock" and computer=="Paper":
                c+=1
            elif x=="Paper" and computer=="Scissor":
                c+=1
            elif x=="Scissor" and computer=="Rock":
                c+=1
            elif x.lower()=="q":
                break
            elif x not in options:
                 continue
            elif computer==x:
                 print("Tie")
            else:
                player+=1
        
            print(f"Player:{x}")
            print(f"Compuer:{computer}")
            print(f"Points Computer={c} Player={player}")
            
