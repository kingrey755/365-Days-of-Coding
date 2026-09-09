import re

password = input("enter password: ")
score = min(len(password) * 3, 40)
score += 15 if re.search("[a-z]", password) else 0
score += 15 if re.search("[A-Z]", password) else 0
score += 15 if re.search("[0-9]", password) else 0
score += 15 if re.search("[^A-Za-z0-9]", password) else 0
print(f"Score: {min(score, 100)}/100")
