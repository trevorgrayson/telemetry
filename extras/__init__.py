"""
  python package "extras" module

  *Attempt* to import a library, without knowing if it's installed.
  May optionally throw an error

  
"""
import inspect
import logging

logger = logging.getLogger(__name__)

MODULES={}


def __getitem__(module_name):
    """ hash interface with extras, throw error if 
    module doesn't exist.
    """
    module = MODULES.get(module_name)

    if module:
        return module

    module = __import__(module_name)  
    MODULES[module_name] = module

    return module


def get(module_name):
    """ return package if package exists, None if fails.
        should cache imported modules
    """

    try:
        return __getitem__(module_name)

    except ImportError as err:
        logger.info("Excluding `%s` because it's not installed."%module_name)


def not_important(module_name):
    """ `import` directly to the class binding.
    reference the class just like you used `import`.
    `module_name is None` checks for existance.
    """
    stack = inspect.stack()
    klass = stack[1][0].f_locals[module_name] = get(module_name)

optional = not_important
