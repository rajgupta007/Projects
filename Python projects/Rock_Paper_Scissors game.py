import random
print("Welcome to Rock,Paper And Scissors \n")
print("Choose 0 -> Rock  1 -> Paper 2 -> Scissors \n")
loop=9
mydict = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"   
}
up=0
cp=0
while(loop):
  inp=int(input("Enter your choice :: "))%3
  rand=(random.randint(0,99)%3)
  print(rand,"  \n")    
  if(inp==0):
    print(mydict[0],"  ",mydict[rand])
    if(rand==2):
      up=up+1
    if(rand==1):
      cp=cp+1
  if(inp==1):
    print(mydict[1],"  ",mydict[rand])
    if(rand==2):
      cp=cp+1
    if(rand==0):
      up=up+1
  if(inp==2):
    print(mydict[2],"  ",mydict[rand])
    if(rand==1):
      up=up+1
    if(rand==0):
      cp=cp+1
  loop=loop-1

print("Your points :: ",up,"  computer points :: ",cp)
if up>cp :
  print("You won , hurray !!!!  \n"  )
elif cp>up :
  print("Computer won You lose oooooo !!!!!")
else :
  print("Its a Draw ........")      
