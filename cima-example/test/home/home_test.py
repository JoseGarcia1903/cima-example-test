import pytest
import unittest
from pages.modal.modal_page import ModalPage
from pages.consultfield.consultField_pages import ConsultField


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CimaTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.mp = ModalPage(self.driver)
        self.cf = ConsultField(self.driver)


    @pytest.mark.run(order=1)
    def test_modal(self):
       element1 = self.mp.ModalFirstTime()
       assert element1 == True
       self.mp.ClickNoAcpt()
       element2 = self.mp.ClickAcept()
       assert  element2 == False

    @pytest.mark.run(order=2)
    def test_sendElements(self):
        self.cf.ColorChange()
        self.cf.SendCharacter(caracter="af", color="#c10015")
        check1 = self.cf.BannerInChecking("pdkwd")
        assert check1 == True
        check2 = self.cf.BannerClosed(close="5dp5e")
        assert  check2 == True

