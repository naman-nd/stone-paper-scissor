import random 

c= random.choice([1,2,3])

dict_com={ 1: "stone",
       2: "paper",
       3: "scissor"}
comp_choice = (dict_com[c])


dict_u={"s":"stone",
        "p":"paper",
        "c":"scissor"}
print('''[Choose from (s,p,c])
[s= stone, p= paper, c= scissor] ''')
print(" ")
user=input("input : ")
u = (dict_u[user])
print(f"you choose : {u}")
print(f"Computer's choice : {comp_choice}")

if (comp_choice==u):
  print("Its a draw")
  
elif (comp_choice=="stone" and u=="paper"):
    print("You win")
elif(comp_choice=="stone" and u=="scissor"):
    print("You Loose")
  
elif (comp_choice=="paper" and u=="scissor"):
    print("You win")
elif(comp_choice=="paper" and u=="stone"):
    print("You Loose")
  
elif (comp_choice=="scissor" and u=="stone"):
    print("You win")
elif(comp_choice=="scissor" and u=="paper"):
    print("You Loose")
else:
  print("something went wrong")
