import os

path = "dinput8.dll"
path2 = "dinput8.dll.disabled"
fileChecker = os.path.isfile(path)

if fileChecker:
    print("dinput8.dll found!\ndisabling file...")
    os.rename(path, path2)
    print("\ndinput8.dll successfully disabled!\n")
elif not fileChecker:
    filechecker = os.path.isfile(path2)
    if filechecker:
        print("dinput8.dll.disabled found!\nenabling file...")
        os.rename(path2, path)
        print("\ndinput8.dll successfully enabled!\n")
    else:
        print("DINPUT8.DLL NOT FOUND\ntrying to find version.dll...\n")

path = "version.dll"
path2 = "version.dll.disabled"
fileChecker = os.path.isfile(path)

if fileChecker:
    print("version.dll found!\ndisabling file...")
    os.rename(path, path2)
    print("\nversion.dll successfully disabled!")
    input("press enter to terminate program ")
elif not fileChecker:
    filechecker = os.path.isfile(path2)
    if filechecker:
        print("version.dll.disabled found!\nenabling file...")
        os.rename(path2, path)
        print("\nversion.dll successfully enabled!")
        input("\npress enter to terminate program")
    else:
        print("VERSION.DLL NOT FOUND")
        input("\npress enter to terminate program")

