import os

env = os.getenv('ENVIRONMENT', 'dev')

if env == 'dev':
    try:
        from .local import *  # noqa
    except ImportError:
        from .dev import *  # noqa
else:
    raise ValueError('Unknown settings')
