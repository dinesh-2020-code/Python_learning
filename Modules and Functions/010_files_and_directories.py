import os

def list_directories(s):

    def dir_lists(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_lists(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)


    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_lists(s)
    else:
        print(s + " does not exist")


# listing = os.walk('.')
# for root, directories, files in listing:
#     print("ROOTDIR is ", root)
#     for d in directories:
#         print(d)
#     for file in files:
#         print(file)
list_directories('.')


'''
    global keyword tells the python to look variable in the global scope which is the module's name space
    but the `nonlocal` keyword tells the python to look the variable in the enclosing scope.
    It doesn't look for variable in the global scope.
    nonlocal variable must exist in the enclosing scope but not be global. Non local variables can't be created
'''