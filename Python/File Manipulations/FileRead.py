import os

def Read_File(FileName):
    if(os.path.exists(FileName)):
        fd = open(FileName, "r")        #r indicates read mode
        Data = fd.read()
        print("Data from the file is :-")
        print(Data)
        
    else:
        print("File is Not Existing")
        return

def main():
    print("Enter the file name to create")
    Name = input()

    Read_File(Name)

if __name__ == "__main__":
    main()