"""
Module provides a simple make method to import function and class definitions using config file. The class definitions so
imported can be used to create corresponding instances if they can be initialized using the config file.

Following config file demostrates usage:

example_config.cfg
-----------------------------------------------------------------------------------------------------------------------

[section]
entrypoint = path.to.class:Class
param1 = a
param2 = b

[section]
entrypoint: path.to.method:Method

"""

import importlib

def get(config, section):

    """
    Get module attribute. Ex. class or function

    Args:
        config: ConfigParser object of the config file
        section: section name in the config file

    Returns:
        Module attribute

    """

    return _get_attr(config, section)


def make(config, section):

    """
    Make instance of class using config

    Args:
        config: ConfigParser object of the config file
        section: section name in the config file

    Returns:
        Instance of class

    """

    attr = _get_attr(config, section)

    return attr(config, section)


def _get_attr(config, section):

    """
    parse config section, import module and return attr

    Args:
        config: ConfigParser object of the config file
        section: section name in the config file

    Returns:
        Module attribute

    """
    entrypoint = config.get(section_name, 'entrypoint')
    module, name = entrypoint.split(':')
    module = importlib.import_module(module)
    attr = getattr(module, name)

    return attr
