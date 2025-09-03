import json

FILE_PATH = "./users.json"


class User:
    def __init__(self, username, name, last_name, phone):
        self.username = username
        self.name = name
        self.last_name = last_name
        self.phone = phone

    def create_user_json(self):
        user = {
            "username": self.username,
            "name": self.name,
            "last_name": self.last_name,
            "phone": self.phone,
        }

        return user


def main():
    print("------ Welcome ------")

    while True:

        user_select = input(
            """ Welcome to the database
                    
                    if you want add user enter number 1 and
                    if you want see user DB enter 2 and if 
                    you want search user enter number 3 
                    
                    for exit enter 0:
                """
        )

        if user_select == "1":
            user_name = input("Pleas Enter USERNAME : ")
            user_first_name = input("Pleas Enter FIRSTNAME : ")
            user_last_name = input("Pleas Enter LASTNAME : ")
            user_phone = input("Pleas Enter PHONE : ")

            new_user = User(user_name, user_first_name, user_last_name, user_phone)
            new_user_json = new_user.create_user_json()

            with open(FILE_PATH, "r") as fp:
                information = json.load(fp)

                information["users"].append(new_user_json)

            with open(FILE_PATH, "w") as fp:
                json.dump(information, fp, indent=2)
                print(f"{user_name} added to database ...")

            break

        elif user_select == "2":
            with open(FILE_PATH, "r") as fp:
                information = json.load(fp)

                for user in information["users"]:

                    print(
                        f"""
                          User {information["users"].index(user) + 1}
                          
                          USERNAME :: {user["username"]}
                          FIRSTNAME :: {user["name"]}
                          LASTNAME :: {user["last_name"]}
                          PHONE :: {user["phone"]}
                        \n
                    """
                    )

                break

        elif user_select == "3":
            user_search = input("Pleas Enter username : ").strip()

            with open(FILE_PATH, "r") as fp:
                information = json.load(fp)

                global found
                found = False

                for item in information["users"]:
                    if item.get("username") == user_search:
                        found = True

                        print(
                            f"""                    
                          USERNAME :: {item["username"]}
                          FIRSTNAME :: {item["name"]}
                          LASTNAME :: {item["last_name"]}
                          PHONE :: {item["phone"]}
                        \n
                    """
                        )
                        break

                if not found:
                    print("User Not Found !")

                break

        elif user_select == "0":
            print("See you again !")
            break
        else:
            print("Wrong Input - try again !")
            continue


if __name__ == "__main__":
    main()
