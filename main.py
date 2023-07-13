import os

def enden(fileName):
    fileName2 = fileName + ".disabled"
    fileChecker = os.path.isfile(fileName)

    print("trying to find " + fileName + "...")

    if fileChecker:
        print(fileName + " found!\ndisabling file...")
        os.rename(fileName, fileName2)
        print("\n" + fileName + " successfully disabled!\n")
    elif not fileChecker:
        filechecker = os.path.isfile(fileName2)
        if filechecker:
            print(fileName2 + " found!\nenabling file...")
            os.rename(fileName2, fileName)
            print("\n" + fileName + "successfully enabled!\n")
        else:
            print(fileName.upper() + " NOT FOUND\n")

enden("dinput8.dll")
enden("version.dll")
enden("NativeTrainer.asi")
enden("ScriptHookRDR2.dll")

input("press enter to terminate program ")
