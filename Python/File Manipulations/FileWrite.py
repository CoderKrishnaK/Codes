import os

def Write_File(FileName):
    if(os.path.exists(FileName)):
        print("Enter the data that you want to write in the file")
        Data = input()

        fd = open(FileName, "a")        #a indicates append and write data at end of file
        fd.write(Data)
    else:
        print("File is Not Existing")
        return

def main():
    print("Enter the file name to create")
    Name = input()

    Write_File(Name)

if __name__ == "__main__":
    main()