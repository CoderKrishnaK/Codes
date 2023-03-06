def CreateFile(FileName):

    fd = open(FileName,"w")     # w indicate create file in current directory

def main():
    print("Enter the file name to create")
    Name = input()

    CreateFile(Name)

if __name__ == "__main__":
    main()