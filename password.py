class User:
    '''
    Class that generates instances of the user
    '''
    save_userlist = []
    def __init__(self,username,password):
        
        self.username = username
        self.password = password
        
    def save_user (self):
        '''
        save_user method saves a new user objectto the user list
        '''
        User.save_userlist.append(self) 
        