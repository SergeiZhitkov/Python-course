import validator_collection

email_address = input("What's your email address? ").strip().lower()
try:
    email_address = validators.email(None)
    # Will raise an EmptyValueError
except errors.EmptyValueError:
    # Handling logic goes here
except errors.InvalidEmailError:
    # More handlign logic goes here