#data filtering through list comprehension.
# filtering words by len and uppercasing them. 
words = ["python", "list", "comprehension", "data", "ai", "engineering"]
long_words = [word.upper() for word in words if len(word) > 4]
print(long_words)