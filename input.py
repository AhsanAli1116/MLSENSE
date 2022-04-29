
def user_input(message):
   return input(message)

user_name = user_input("Enter Your name") 
while user_name.isdigit():
    user_name=user_input("Please Enter correct Name")
