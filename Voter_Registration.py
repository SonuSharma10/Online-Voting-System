import re
def validate_voter_id(voter_id):
    pattern = r'^[A-Z]{3}[0-9]{7}$'
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
def validate_aadhar_number(aadhar_number):
    pattern = r'^[0-9]{12}$'
    if re.match(pattern, aadhar_number):
        return True
    else:
        return False
def register():
    voter_id = input("Enter your voter id: ")
    if validate_voter_id(voter_id):
        password = input("Enter your password: ")
        if validate_password(password):
            aadhar_number = input("Enter your aadhar number: ")
            if validate_aadhar_number(aadhar_number):
                print("Registration successful")
            else:
                print("Registration failed. Invalid aadhar number.")
        else:
            print("Registration failed. Password format is incorrect.")
    else:
        print("Registration failed. Voter id format is incorrect.")
register()


