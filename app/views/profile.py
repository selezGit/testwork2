from core.mixins import ViewMixin
from PyQt5.uic import loadUi

class FillProfileScreen(ViewMixin):
    def __init__(self):
        super(FillProfileScreen, self).__init__()
        loadUi('styles/fillprofile.ui', self)
