from validator_collection import validators, errors

email_address = input("What's your email address? ").strip().lower()
try:
    email_address = validators.email(email_address)
    print("Valid")
except errors.InvalidEmailError:
    print("Invalid")
    pass