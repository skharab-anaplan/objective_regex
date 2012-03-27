# form .

from . import base, types

class If(base.RegexBase):

    type = types.Group()

    cond = ifTrue = ifFalse = None

    def __init__(self, cond, ifTrue, ifFalse=None):
        super(If, self).__init__()

        self.cond = cond
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse
        self.children = (cond, ifTrue, ifFalse)

    def _getRegex(self, ctx):

        _mask = "(?({}){})"
        _patterns = [self.ifTrue ]

        if self.ifFalse:
            _mask = "(?({}){}|{})"
            _patterns.append(self.ifFalse)

        return _mask.format(
            self.cond.getName(ctx),
            *(
                _el._asHiddenGroup()._getRegex(ctx)
                for _el in _patterns
            )
        )

# vim: set sts=4 sw=4
