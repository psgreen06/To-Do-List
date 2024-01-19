#35 To-Do List
#Pharah G.
grocerylist = ["Celery", "Beef", "Cumin", "Apples", "Soda", "Ice Cream", "Candy", "Canned Corn"]

#Functions 
def toDo():
    print("Welcome to your grocery list! Your current list includes: ")
    print(grocerylist)
    addition = input(("Would you like to add an item?"))
    if addition == "Yes" or "yes": 
        add= input(("What would you like to add? "))
        grocerylist.append(add)
    print("Your new grocery list is: " )
    print(grocerylist)
    if addition == "no" or "No":
        



#Main 
toDo()