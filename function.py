def address(street = "5 - 1", postal_code = "362738"):
    if len(p_c)>6:
        print("Pincode is invalid")
        return
    print("Your address is:", street, "St.,",  postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
# c = input("City: ")
address(s, p_c)
# Output:
#     Street: eluru
# Postal Code: 5430000324
# Pincode is invalid
# Output: 2
# Street: elur
# Postal Code: 534001
# Your address is: elur St., 534001

    