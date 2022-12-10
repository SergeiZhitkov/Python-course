def main():
    message = input("Enter your message: ").strip()
    omitting_vowels(message)




def omitting_vowels(m):
    for letter in m:
        if letter in "aeiouAEIOU":
