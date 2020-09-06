        
class Info:
    '''
    class that generates instances of the users credentials
    '''
    info_list = []
    
    def __init__ (self,facebookp,emailp):
      self.facebookp = facebookp
      self.emailp = emailp
    
    def save_info(self):
        '''
        method created to save credentials
        '''
        Info.info_list.append(self)
    
    def delete_info(self):
        '''
        Method that deletes credentials
        '''
        Info.info_list.remove(self)
    
    
    @classmethod
    def display_info(cls):
        '''
        a class method involves the whole class the display info 
        '''     
        
        return cls.info_list
      
        