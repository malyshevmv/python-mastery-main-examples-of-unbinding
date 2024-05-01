
import sys
import inspect

class Structure:
    _fields = ()
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, arg in zip(self._fields, args):
            setattr(self, name, arg)
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}({', '.join(repr(getattr(self, name)) for name in self._fields)})'
    
    def __setattr__(self, name: str, value) -> None:
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'No attribute {name}')

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
    
    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple(sig.parameters)