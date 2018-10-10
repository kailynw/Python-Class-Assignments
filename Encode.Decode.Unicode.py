def main():
    print("This program converts a textual message into a sequence")
    print ("of numbers representing the Unicode encoding of the message.\n")
    # Get the message to encode
    message = input("Please enter the message to encode: ")
    print("\nHere are the Unicode codes:")
    # Loop through the message and print out the Unicode values
    print("Decoded: ")
    list=[]
    for ch in message:
        print(ord(ch),end=" ")
        list.append(ord(ch))
    print(" ")

    print("Re-encoded: ")
    message=""
    for i in range(len(list)):
        message=message+ chr(list[i])
    print(message)
    
main()
