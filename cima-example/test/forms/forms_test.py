import pytest
import unittest
from pages.form.form_page import ConsultForm
from pages.correctForm.correctForm_page import CorrectForm

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CimaTest2(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.fm = ConsultForm(self.driver)
        self.ft = CorrectForm(self.driver)


    @pytest.mark.run(order=3)
    def test_form(self):
        self.fm.ClickAcept()
        firstResult = self.fm.Button_directly()
        assert firstResult == True
        result2 = self.fm.PersonalData()
        assert result2 == True
        result3 = self.fm.PersonalDataOff()
        assert result3 == False
        result4 = self.fm.CheckElementsForm()
        assert result4 == True
        result5 = self.fm.Propuesta_mejora()
        assert result5 == False

    @pytest.mark.run(order=4)
    def test_lastForm(self):
    # self.ft.ClickAcept()
     self.ft.ClicksElements()
     self.ft.FindBanner()




