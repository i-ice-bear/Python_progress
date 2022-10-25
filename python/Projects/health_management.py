import datetime

current_time = datetime.datetime.now()

get_client_name = str(input("Enter your name please : "))
print("\b [1] Get your diet")
print("\b [2] Post your diet")
select_option = int(input("Select option : "))


def get_your_diet():
    try:
        with open(f"./utilities/{get_client_name}.txt", "x") as file_generate:
            file_generate.write(f"[{current_time}]. Your diet is : Chicken")
            print(f"Mr {get_client_name} Now you're in our fitness club what you want to do")
            print("\b [1] Get your diet")
            print("\b [2] Post your diet")
            select_option = int(input("Select option : "))
    except FileExistsError as File_already_exist:
        with open(f"./utilities/{get_client_name}.txt", 'r') as existing_user_data:
            print(existing_user_data.read())
        return File_already_exist
    else:
        return ""


def post_your_diet():
    try:
        with open(f"./utilities/{get_client_name}.txt", "a") as change_file_state:
            print("\nIf it's get done then hit Ctrl+C to exit")
            clear_previous_data = str(input("Do you want to clear previous data [yes/no] : "))
            if clear_previous_data == "yes":
                with open(f"./utilities/{get_client_name}.txt", "r+") as truncation:
                    truncation.truncate(0)
            else:
                print("You will going to continue from your previous diet")
            while True:
                user_diets = str(input("Add your diet list : "))
                change_file_state.write(f"\n[{current_time}]. {user_diets}")

    except KeyboardInterrupt:
        print("You exited from program ")


if select_option == 1:
    get_your_diet()
elif select_option == 2:
    post_your_diet()
else:
    print("Not found!")