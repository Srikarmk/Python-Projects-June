#some ways to concatenate a string 
'''
name=input("What is your Name")

print("Your name is "+ name)
print("your name is {}".format(name))
print(f"your name is {name}")
'''
name=input("Name: ")
place=input("Place: ")
verb=input("Verb: ")
funny=input("funny_name: ")
belief=input("Your belief: ")
actor=input("actor/actress name: ")
show=input("Favourite Show: ")
madlib=f"I am {name} , I live in {place} , i like to {verb}.My nickname is {funny}, Programming is {belief}.My favourite actor is {actor} and i love watching {show}."
  
print(madlib)