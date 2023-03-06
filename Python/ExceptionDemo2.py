def main():
    try:
        print("Enter First Number :")
        No1 = int(input())

        print("Enter Second Number :")
        No2 = int(input())

        
        Ans = No1 / No2         # Exception Prone Code
        print("Division is :",Ans)
    except ZeroDivisionError:
        print("Inside Zero Division Error")

    except ValueError:
        print("Inside Value error")
    
    except Exception:
        print("Inside last except block")
        
    finally:
        print("Inside Finally Block")
        
if __name__ == "__main__":
    main()