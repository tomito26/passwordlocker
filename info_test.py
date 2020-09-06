import unittest
from info import Info

class TestInfo(unittest.TestCase):
    def setUp(self):
        self.new_info = Info(1234,3454,4566,6785, 'tomito','@jarvis','budds')
    
    def test_init(self):
        self.assertEqual(self.new_info.facebookp,1234)
        self.assertEqual(self.new_info.instagramp,4566)
        self.assertEqual(self.new_info.twitterp,6785)
        self.assertEqual(self.new_info.emailp,3454)
        self.assertEqual(self.new_info.facebookusername,'tomito')
        self.assertEqual(self.new_info.twitusername,'@jarvis')
        self.assertEqual(self.new_info.instagramusername,'budds')
        
    def test_save_info(self):
        '''
        to test if the user info is saved
        '''
        self.new_info.save_info()
        self.assertEqual(len(Info.info_list),1)
        
    def test_display_creds(self):
        self.assertEqual(Info.display_info(),Info.info_list)



if __name__ =='__main__':
    unittest.main()
        