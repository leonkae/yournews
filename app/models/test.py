from cgi import test
import http
import unittest


from article import Article

class ArticleTest(unittest.TestCase):
    
    def setUp(self):
        self.articles = Article("JohnDoe","TeslaStock","Stock is up","http://","http://","content","date")
        
            
    def test_init(self):
        self.assertEqual(self.new_user.f_name,"John")
        self.assertEqual(self.new_user.l_name,"Doe")
        self.assertEqual(self.new_user.u_name,"John Doe")
        self.assertEqual(self.new_user.email,"pseudo@gmail.com")
        self.assertEqual(self.new_user.password,"123john")    

    def test_instance(self):
        self.assertTrue(isinstance(self.articles,Article)) 
        
if __name__ == '__main__' :
    unittest.main
        