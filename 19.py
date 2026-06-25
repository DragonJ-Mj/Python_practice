# Problem: Use a while loop to repeatedly prompt a user to create a password. Keep looping until they enter a password that is at least 8 characters long.
# ​Expected Behavior: * User enters "123" \rightarrow Prints "Too short!", loops again.
# ​User enters "secret123" \rightarrow Prints "Password accepted!", terminates.


user_password = input("Enter the Passward: ")
length = len(user_password)


while length <9 :
    if length>= 8:
        print("Password Accepted")
        break
    print("You entered ", user_password, "which is too short")
    loop_pass = input("Enter new password = ")
    length = len(loop_pass)
   
print("Password Accepted")