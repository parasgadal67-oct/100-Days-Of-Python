# Creating the contact info extractor using regular expression(regex)
# In this we will extract the email and contact number of the user's input
import re
text = """
Paras : parasgadal814@gmail.com 83948334507,
Ayush : ayushbartwal2003@gmail.com ,contact info : 7895364210 
Ally Willson email is willsonally97@gmail.com for contacting her ring her at 8956743021
"""
email_pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(?:com|edu|net|org)"
contact_pattern = r'\d{10}'

emails = re.findall(email_pattern, text)
contacts = re.findall(contact_pattern, text)

print("Here are all the emails:", emails)
print("Here are these emails contact:", contacts)