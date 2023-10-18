from email_validator import validate_email,EmailNotValidError

def check(email):
    try:
        v=validate_email(email)
        print("Valid Email")
    except Exception as e:
        print(e)

email=input("Enter your Email address: ") #g@g.in

c=check(email)




