from core.mixins import ViewMixin
from PyQt5.uic import loadUi


class ProfileScreen(ViewMixin):
    title = 'profile'

    def __init__(self):
        super(ProfileScreen, self).__init__()
        loadUi('styles/profile.ui', self)
