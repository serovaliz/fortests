

def create_user(username, is_admin=False):
    if is_admin:
        print(f"User {username} is an admin.")
    else:
        print(f"User {username} is a regular user.")

create_user("Alice")  # is_admin == False
create_user("Bob", is_admin=True)  # is_admin == True
create_user("Karl", True)  # is_admin == True

def create_profile(name, age, job):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Job: {job}")

create_profile(age = 28, name = "John",  job = "Developer")