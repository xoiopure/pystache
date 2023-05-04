
"""
TODO: add a docstring.

"""

class Complex(object):

    def header(self):
        return "Colors"

    def item(self):
        return [
            {'name': 'red', 'current': True, 'url': '#Red'},
            {'name': 'green', 'link': True, 'url': '#Green'},
            {'name': 'blue', 'link': True, 'url': '#Blue'},
        ]

    def list(self):
        return not self.empty()

    def empty(self):
        return len(self.item()) == 0

    def empty_list(self):
        return [];
