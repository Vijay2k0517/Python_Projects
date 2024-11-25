def palindrome_checker():
    text = input("Enter the text:")

    while True:

        clean_text = ''.join(char for char in text if char.isalnum()).lower()

        reversed_text = clean_text[::-1]

        if clean_text == reversed_text:
            print("YEAH! That's pallindrome")

        else:
            print("NAH! That is not a pallindrome")

        loop = input("Do you want to do again? (y/n)").lower()

        if loop !="y" :
            break

palindrome_checker() 
