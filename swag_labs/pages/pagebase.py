from pylenium.driver import Pylenium
from swag_labs.pages.navigation import Navigation


class PageBase:
    def __init__(self, py: Pylenium):
        self.navigation = Navigation(py)
