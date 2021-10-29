class Callback:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def run(self, **kwargs):
        self.func(*self.args, **kwargs)
    