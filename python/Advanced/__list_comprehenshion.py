import datetime

current_time = datetime.datetime.now().second


def __list__comprehension():
    list_i = []

    for i in range(100):
        if i % 2 == 0:
            list_i.append(i)

    print(list_i)
    print(len(list_i))

    # One liner function via list comprehension
    # Method 1
    list_i = [i for i in range(100) if i % 3 == 0]
    print(list_i)


def __dictionary___comprehension():
    _dict_comprehension = {
        i: f"item {i}"
        for i in range(5)
        if i % 3 == 0
    }
    _dict_comprehension = {value: key for key, value in _dict_comprehension.items()}
    print(_dict_comprehension)


# __dictionary___comprehension()


def __set__comprehension_():
    print(main for main in ["main1", "main2", "main3"])


# __set__comprehension_()


def __generator_comprehension():
    even__numbers = (i for i in range(100) if i % 2 == 0)
    for item in even__numbers:
        print(item)


# __generator_comprehension()


def __generate_a_list():
    print("Do you want to print a list!")
    print('''
     ██████╗██╗  ██╗ ██████╗  ██████╗ ███████╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
    ██╔════╝██║  ██║██╔═══██╗██╔═══██╗██╔════╝██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
    ██║     ███████║██║   ██║██║   ██║███████╗█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
    ██║     ██╔══██║██║   ██║██║   ██║╚════██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
    ╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
     ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    ''')
    print('''
    =============== Choose the type ===============
    [1] List comprehension
    [2] Set comprehension
    [3] Dictionary Comprehension
    ''')

    _print_comprehension = int(input("Choose the type > "))

    if _print_comprehension == 1:
        print('''
        ██╗     ██╗███████╗████████╗     █████╗ ██████╗ ██████╗  █████╗ ██╗   ██╗
        ██║     ██║██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
        ██║     ██║███████╗   ██║       ███████║██████╔╝██████╔╝███████║ ╚████╔╝ 
        ██║     ██║╚════██║   ██║       ██╔══██║██╔══██╗██╔══██╗██╔══██║  ╚██╔╝  
        ███████╗██║███████║   ██║       ██║  ██║██║  ██║██║  ██║██║  ██║   ██║   
        ╚══════╝╚═╝╚══════╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                         
        ''')
        _range_choice = int(input("\nEnter your range:"))
        _print_to_list = [list_i for list_i in range(_range_choice)]
        print(_print_to_list)
        print("Done")

    if _print_comprehension == 2:
        print('''
        ███████╗███████╗████████╗                                                                                   
        ██╔════╝██╔════╝╚══██╔══╝                                                                                   
        ███████╗█████╗     ██║                                                                                      
        ╚════██║██╔══╝     ██║                                                                                      
        ███████║███████╗   ██║                                                                                      
        ╚══════╝╚══════╝   ╚═╝                                                                                      
                                                                                                                    
         ██████╗ ██████╗ ███╗   ███╗██████╗ ██████╗ ███████╗██╗  ██╗███████╗███╗   ██╗███████╗██╗ ██████╗ ███╗   ██╗
        ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝████╗  ██║██╔════╝██║██╔═══██╗████╗  ██║
        ██║     ██║   ██║██╔████╔██║██████╔╝██████╔╝█████╗  ███████║█████╗  ██╔██╗ ██║███████╗██║██║   ██║██╔██╗ ██║
        ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██╔══██╗██╔══╝  ██╔══██║██╔══╝  ██║╚██╗██║╚════██║██║██║   ██║██║╚██╗██║
        ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║  ██║███████╗██║  ██║███████╗██║ ╚████║███████║██║╚██████╔╝██║ ╚████║
         ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
        ''')
        _range_choice = int(input("\nEnter your range:"))
        _print_to_list = {list_i: f'item{list_i}' for list_i in range(_range_choice)}
        print(_print_to_list)
        print("Done")

    if _print_comprehension == 3:

        print('''
        ██████╗ ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██████╗ ██╗   ██╗
        ██╔══██╗██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
        ██║  ██║██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████║██████╔╝ ╚████╔╝ 
        ██║  ██║██║██║        ██║   ██║██║   ██║██║╚██╗██║██╔══██║██╔══██╗  ╚██╔╝  
        ██████╔╝██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║██║  ██║██║  ██║   ██║   
        ╚═════╝ ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                                   
         █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗    ██╗██╗               
        ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    ██║██║               
        ███████║   ██║      ██║   ███████║██║     █████╔╝     ██║██║               
        ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗     ╚═╝╚═╝               
        ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗    ██╗██╗               
        ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝╚═╝               
        ''')

        _range_choice = int(input("\nEnter your range:"))
        _print_to_list = (list_i for list_i in range(_range_choice))
        for item_list in _print_to_list:
            print(item_list)
        print("Done")


__generate_a_list()

end_time_mod = datetime.datetime.now().second

__function_initial_time__loop = end_time_mod - current_time
print(f"Time taken for function execution : {__function_initial_time__loop}")
