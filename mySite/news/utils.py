
class MyMixin(object):
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, smth):
        if isinstance(smth, str):
            return smth.upper()
        else:
            return smth.title.upper()
