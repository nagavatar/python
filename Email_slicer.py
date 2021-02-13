#strip function removes all unncessary spaces(aka trim) in front and end
email = input("Enter Your Email: ").strip()
#username becomes email selected upto @
username = email[:email.index("@")]
#domain_name becomes text after @
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)