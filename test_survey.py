import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn(('English', my_survey.responses))

    def test_store_responses(self):
        question = 'What language did you first learn to speak？'
        my_survey = AnonymousSurvey(question)
        reponses = ['English', 'Spanish','Mandarin']
        for response in reponses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__=='__main__':

