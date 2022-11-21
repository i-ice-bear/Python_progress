import os


def __scan_directory():
    __scanned_directory_elements = os.scandir('C:/Users/Dell/Desktop/testing')

    for __each__dir_file in __scanned_directory_elements:
        path = "C:/Users/Dell/Desktop/testing/"
        _for_capitalization_file_name = str(__each__dir_file)
        __capital_name = _for_capitalization_file_name.capitalize()
        print(__capital_name)

        with open("C:/Users/Dell/Desktop/testing/myfile.txt", "r") as file_synonyms:
            read__data = file_synonyms.readline()
            converted__data = str(read__data)
            print(converted__data)

            if converted__data.__contains__("this, that"):
                print("Invalid arguments")
            else:
                oldFile = __each__dir_file
                print(oldFile)
                os.rename(oldFile, "myfile.txt")
                file_synonyms.close()


__scan_directory()
