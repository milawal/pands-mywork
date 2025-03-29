# Accounts
# This program reads a 10 character account number and prints outputs (account number) showing only the last 4 digits
# author: Michael Lawal
# Reference: Python string manipulation and input/output operations.

def mask_account_number(account_number):
    if len(account_number) == 10:
        return 'XXXXXX' + account_number[-4:]
    else:
       return "Invalid account number"

# To read the account number from the user
account_number = input("Enter a 10-digit account number: ")

# For the output of the masked account number
masked_account = mask_account_number(account_number)
print("Masked Account Number:", masked_account)

# Modifying the program above to consider account number of any length
def mask_account_number(account_number):
    length = len(account_number)
    if length > 4:  # If the account number is longer than 4 characters, mask the first (length - 4) characters and last 4 digits remain unchanged
        return 'X' * (length - 4) + account_number[-4:]
    else:
        return account_number  # If the account number is 4 or less than 4, no masking is required

# To read account number from the user
account_number = input("Enter your account number: ")

# For the output of the masked account number
masked_account = mask_account_number(account_number)
print("Masked Account Number:", masked_account)
