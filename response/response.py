from validator_collection import validators

email_address = input("What's your email address? ").strip().lower()
if email_address := validators.email(email_address):
    print("Valid")
else:
    print("Invalid")