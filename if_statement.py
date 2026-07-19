# # age =int(input("Enter your age: "))
# # if age>18:
# #     print("You are eligible to vote.")
# # else:
# #     print("You are not eligible to vote.")

# # print("done")

# physics=int(input("Enter your physics marks: "))
# chemistry=int(input("Enter your chemistry marks: "))
# # if physics>=33 and chemistry>=33:
# #     print("You are pass in both subjects.")
# # else:
# #     print("You are fail in one or both subjects.")
# if physics>=33 and chemistry>=33:
#     print("You are pass in both subjects.")
# elif physics<33 and chemistry>=33:
#     print("You are fail in physics.")
# elif physics>=33 and chemistry<33:
#     print("You are fail in chemistry.")
# else:
#     print("You are fail in both subjects.")

age=int(input("Enter your age: "))
certificate=input("Do you have a certificate? (yes/no): ").strip().lower() == 'yes'
if age>18:
    if certificate==True:
        print(" you are hired for job")
    else:
        print("your r not eligible for job due to lack of certificate 23")
else:
    print("your r not eligible for job")
