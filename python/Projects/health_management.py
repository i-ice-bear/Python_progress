import datetime

current_time = datetime.datetime.now()

get_client_name = str(input("Enter your name please : "))
print("\b [1] Get your diet")
print("\b [2] Post your diet")
print("\b [3] Get your exercise plan")
print("\b [4] Post your exercise plan")
select_option = int(input("Select option : "))


def get_your_diet():
    try:
        with open(f"./utilities/{get_client_name}-diet.txt", "x") as file_generate:
            file_generate.write(f"[{current_time}]. Your diet is : Chicken")
            print(f"Mr {get_client_name} Now you're in our fitness club what you want to do")
            print("\b [1] Get your diet")
            print("\b [2] Post your diet")
            select_option = int(input("Select option : "))
            return "You joined our club successfully!"
    except FileExistsError as File_already_exist:
        with open(f"./utilities/{get_client_name}-diet.txt", 'r') as existing_user_data:
            print(existing_user_data.read())
        return File_already_exist
    else:
        return ""


def post_your_diet():
    try:
        with open(f"./utilities/{get_client_name}-diet.txt", "a") as change_file_state:
            print("\nIf it's get done then hit Ctrl+C to exit")
            clear_previous_data = str(input("Do you want to clear previous data [yes/no] : "))
            if clear_previous_data == "yes":
                with open(f"./utilities/{get_client_name}-diet.txt", "r+") as truncation:
                    truncation.truncate(0)
            else:
                print("You will going to continue from your previous diet")
            while True:
                user_diets = str(input("Add your diet list : "))
                change_file_state.write(f"\n[{current_time}]. {user_diets}")

    except KeyboardInterrupt:
        print("You exited from program ")


def get_your_exercise_plan():
    try:
        with open(f"./utilities/exercise/{get_client_name}-exercise-plan.txt", "x") as file_generate:
            file_generate.write(f"[{current_time}]. Your diet is : ")
            print(f"Mr {get_client_name} Now you're in our fitness club what you want to do")
            print("\b [1] Get your diet")
            print("\b [2] Post your diet")
            select_option = int(input("Select option : "))
            return "You joined our club successfully!"
    except FileExistsError as File_already_exist:
        with open(f"./utilities/exercise/{get_client_name}-exercise-plan.txt", 'r') as existing_user_data:
            print(existing_user_data.read())
        return File_already_exist
    else:
        return


def post_your_exersice_plan():
    try:
        with open(f"./utilities/exercise/{get_client_name}-exercise-plan.txt", "a") as exercise_file_state:
            print("\n if it's get done then hit ctrl+c to exit")
            clear_previous_data = str(input("Do you want to clear previous data [yes/no] : "))
            if clear_previous_data == "yes":
                with open(f"./utilities/exercise/{get_client_name}-exercise-plan.txt", "r+") as truncation:
                    truncation.truncate(0)
            else:
                print("You will going to continue from your previous diet")
            while True:
                user_diets = str(input("Add your diet list : "))
                exercise_file_state.write(f"\n[{current_time}] Exercise : {user_diets}")

    except KeyboardInterrupt:
        print("You exited from program ")


if select_option == 1:
    get_your_diet()
elif select_option == 2:
    post_your_diet()
elif select_option == 3:
    get_your_exercise_plan()
elif select_option == 4:
    post_your_exersice_plan()
else:
    print("Invalid option!")
