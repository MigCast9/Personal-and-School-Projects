################################################################################
# Author: Miguel Castilho Oliveira
# Date: 04/23 /2021
# Description Function to determine, grant or revoke the orivileges of users
################################################################################

class Privileges():
    #instantiation
    def __init__(self, privs = ['interact', 'post']):
        self.privs = privs
       
    #granting and revoking privileges
    def grant(self, string):
        self.privs.append(string)
        print("Granted", string)
        
    def revoke(self, string):
        self.privs.remove(string)
        print("Revoked", string)
    #transforms the set into a sorted list and prints it into a string
    def get_privs(self): #this function transfers the content from the set to the list, then sorts, then transfers it back to the empty set sorted
        
        return(', '.join(sorted(self.privs)))
            
class User(Privileges):
    def __init__(self, name, email):
        self.email = email
        self.name = name
        self.privs = Privileges()
    
    def describe_user(self):
        print('User Profile')
        print('  Name:', self.name)
        print('  Email:', self.email)
        print('  Privs:', self.privs.get_privs())

def main():
    alice = User('Alice', 'alice@example.com')
    #calling it all
    alice.describe_user()
    alice.privs.grant('teleport')
    alice.describe_user()
    alice.privs.revoke('post')
    alice.describe_user()
    

if __name__ == '__main__':
    main()
