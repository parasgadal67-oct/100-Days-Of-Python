# Using the regular expressions creating the phone number extractor.
import re
text = "Contact Authorities : 9876054348,  personal: 763-489-2398 for emergencies:701 115 9888"
pattern = r'\d{3}[-\s]?\d{3}[-\s]?\d{4}'
phone_number = re.findall(pattern, text)
print(phone_number)