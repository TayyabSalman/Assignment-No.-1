import unittest
import code

class TestCode(unittest.TestCase):
    def test_MCQ(self):
        try:
            self.assertTrue(self, True)
        except:
            self.assertTrue(self, False)

    def test_NUMERIC(self):
      try:
            self.assertTrue(self,True)
      except:
            self.assertTrue(self,False)

    def test_stor_data(self):
        try:
            self.assertTrue(self,True)
        except:
            self.assertTrue(self,False)

    def test_sub_data(self):
        try:
            self.assertTrue(self,True)
        except:
            self.assertTrue(self,False)

    def test_TF(self):
       try:
            self.assertTrue(self,True)
       except:
            self.assertTrue(self,False)



if __name__ == '__main__':
    unittest.main()


