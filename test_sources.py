import unittest
from app.models import Source
class SourceTest(unittest.TestCase):
    '''
    test to  test the source class
    '''
    def setUp(self):
        '''
        setup always runs after every test
        '''
        self.newassertTrue(isinstance(self.new_source,source))

if __name__=='__main__':
    unittest.main()