#Bank
#This program should prompt users to enter amount, read in two money amounts and print answer in Euro format
#author: Michael Lawal

prompt1 = 'Enter First Amount (in cents):'
Amount1= int(input(prompt1))
prompt2 = 'Enter Second Amount (in cents):'
Amount2= int(input(prompt2))
Total_amount = Amount1 + Amount2
Euros = Total_amount //100
Cents = Total_amount %100
print(f"Total amount is €{Euros}.{Cents:02d}")
