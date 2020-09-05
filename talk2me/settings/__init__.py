from .base import *
from decouple import config

if config('DEBUG'):
    from .local import *
else:
    from .prod import *