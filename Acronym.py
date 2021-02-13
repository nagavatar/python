user_in = str(input("Please enter phrase to be acronymed : "))
u_list = user_in.split()
a = ""
for i in u_list:
    a+=str(i[0].upper())
print("The Phrase after acronyming is ",a)