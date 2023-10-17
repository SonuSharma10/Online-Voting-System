import re
def validate_voter_id(voter_id):
    pattern = r'^[A-Z]{3}\d{7}$'
    if re.match(pattern, voter_id):
        return True
    else:
        return False

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return False

def login():
    voter_id = input("Enter your voter id: ")
    if validate_voter_id(voter_id):
        password = input("Enter your password: ")
        if validate_password(password):
            print("Login successful")
        else:
            print("Login failed. Password format is incorrect.")
    else:
        print("Login failed. Voter id format is incorrect.")

login()

