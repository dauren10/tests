import unittest
from survey import AnonymousSurvey

class TestAnonmySurvey(unittest.TestCase):

    def setUp(self):
        question='Какой язык программирования для вас наиболее интересен?'
        self.my_survey=AnonymousSurvey(question)

    def test_store_single_response(self):
       
        self.my_survey.store_response('Java')
        self.assertIn('Java',self.my_survey.responses)

    def test_five_response(self):
        l=['Java','C++','Python']
        for i in l:
            self.my_survey.store_response(i)
        for i2 in l:
            self.assertIn(i2,self.my_survey.responses)


unittest.main()