import getpass
    #importing getpass libray to hide password from user
class Tokens():
    '''class init funtion'''
    def __init__(self,Name,ID,Tokens,Balance,Passwd):
        self.Name = Name
        self.ID = ID
        self.Tokens = Tokens
        self.Balance = Balance
        self.Passwd = Passwd

        #string representation
    def __str__(self):
        return f'User ID\t\t:{self.ID}\nUser Name\t:{self.Name}\nTokens\t\t:{self.Tokens}\nUser Balance\t:{self.Balance}'
        
        #function for creating tokens
    def adding_tokens(self):     
        passwd = getpass.getpass('Please enter password to add tokens: ') 
        if passwd == self.Passwd:
            amt = getpass.getpass('enter the amount: ')
            if self.Balance >= int(amt):
                token = int(amt)/20
                self.Tokens += token
                self.Balance-=int(amt)
            else:
                return 'No Sufficant funds'
        return f'{token} Tokens has been added successfully'
            #function for adding funds
    def topup_money(self):
        passwd = getpass.getpass('Please enter password to add amount: ') 
        if passwd == self.Passwd:
            amount= int(input('Enter amount to this account: '))
            self.Balance+= amount
        else:
            return 'Please enter the correct passwd'
        return f'Your account has been Updated; Balance : ${self.Balance}'


        
#Logic

#Getting input form the user
Name = input('Please enter your name : ')
ID = ''
while True:
    ID = input('Please enter your ID: ')
    if len(ID) == 4:
        break
    else:
        continue             
Token = 0
Balance = 0
Password = getpass.getpass('Please enter your password : ')
# creating user Id 
def userId(Name,ID):
    username=Name+ID
    return username
username = userId(Name,ID)
print(f'Kudos! Your username is {username}')
# adding the given data to the token class

username = Tokens(Name,ID,Token,Balance,Password)




# Fetching balance of token and amount

# Adding funds and amount
