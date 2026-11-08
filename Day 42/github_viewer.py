import requests
username = input("Enter Github username: ").strip()
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("login:", data["login"])
    print("Public_repos:", data["public_repos"])
    print("Followers:",data["followers"])
    print("Location:", data.get("location") or "not shared")
elif response.status_code == 404:
    print("User not found")
else:
     print("Something went wrong. Status:", response.status_code)
     print("Message:", response.json().get("message", "no details"))
    