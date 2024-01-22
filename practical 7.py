string = input('Enter the string: ')
reverse = string[::-1]

if string == reverse:
    print('Palindrome')
else:
    print('Not Palindrome')
