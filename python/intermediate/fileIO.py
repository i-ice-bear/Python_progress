"""
    Use the file IO in python you can simply access the non-volatile memory,
    there are two types of memory in the system.

    1. Non-volatile-memory.
    -> Volatile memory is a type of memory that maintains,
       its data only while the device is powered.
       If the power is interrupted for any reason, the data is lost.
    2. Non-volatile-memory:
    -> Non-volatile memory (NVM) or non-volatile storage is a type of computer memory
       that can retain stored information even after power is removed.

    # types of opening file
    1. "r" : (read-mode) : Open the file in reading mode. (default)
    2. "w" : (write-mode) : Open the file in writing mode as well as reading mode.
    3. "x" : (exclusive-creation) : Creates file if not exist.
                                    If exist then it break or throw error.
    4. "a" : (append) : Add more content to a file from end...
    5. "t" : (text-mode) : Open file in text mode. to deal with string (default)
    6. "b" : (binary-mode) : Open the files in binary mode
    7. "+" : (read-and-write) : Read and write of the file.

    """


def open_fileFunc():
    """
        First file is opened and then along with read-binary arguments and
        then passed the .read() function along with the file variable into
        a new variable then we closed the file.
    """
    open_file = open("../../generated/jimmy.txt", "rb")
    content_file = open_file.read()
    print(content_file)
    open_file.close()


def read_lineByLine():
    open_fileNew = open("../../generated/jimmy", "r")
    # content = open_fileNew.read()
    print(open_fileNew.readlines())

    for lines in open_fileNew:
        print(lines)



def writing_and_appending():
    """
       This function is interconnected with read_Files()
       to Read the file. without any content change.

    """
    open_file_init = open("../../generated/Jimmy.txt", "w")
    open_file_init.write("Hello,")
    open_file_init.write("\nI love chain-smokers music")
    open_file_init.write("\nAnd I love blackpink also ")
    open_file_init.write("\nAlok is the best brazillian slap house producer")
    print(open_file_init.fileno(), "\n")
    open_file_init.close()


writing_and_appending()


def read_Files():
    """
       This function is interconnected with writing_and_appending()
       to add content in file . without any data loss and error.
    """

    openFileDatas = open("../../generated/Jimmy.txt", 'r')
    print(openFileDatas.read())


read_Files()
