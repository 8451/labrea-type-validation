from . import _startup
from ._runtime import enable, enabled
from ._version import __version__


# If environment variable LABREA_TYPE_VALIDATION_ENABLED is set, enable type checking
_startup.run()


__all__ = ["enable", "enabled", "__version__"]
