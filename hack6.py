def print_full_name(first_name,last_name):
    #first_name=input(str())
    #last_name=input(str())
    if len(first_name)<=10 and len(last_name)<=10:

        print("Hello",first_name,last_name,"!You just delved into python.")
    else:
        print("")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)