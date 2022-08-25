import os


def soldier(pathOfdir, filetoopen, format):
    os.chdir(pathOfdir)
    forRename = 1

    for tocapital in os.listdir():
        TrueOrFalse = "True"
        with open(filetoopen) as f:
            notTocapitalize = f.read().split("\n")
            # for i in notTocapitalize:
            #     if i == tocapital:
            #         TrueOrFalse = "False"
            #         break
        # if TrueOrFalse == "True":
        #     os.rename(tocapital, tocapital.capitalize())
        if tocapital not in notTocapitalize:
            os.rename(tocapital, tocapital.capitalize())

        if tocapital.__contains__(f".{format}"):
            os.rename(tocapital, f"{forRename}.{format}")
            forRename = forRename+1


# pathofdir = input("Enter the path:")
pathofdir = r"f:/python"
# filetoopen = input("Enter the name of file:")
filetoopen = r"file.txt"
# format = input("Enter the type of format:")
format = r"data"
soldier(pathofdir, filetoopen, format)
