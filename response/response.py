from validator_collection import validators
import sys

email_address = input("What's your email address? ").strip().lower()
try:
    email_address = validators.email(email_address)
    print("Valid")
except ValueError:
    sys.exit("Invalid")