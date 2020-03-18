""" Extend configparser.ConfigParser with additional methods """

import configparser
import ast

class ConfigParser(configparser.ConfigParser):

    """ Extend configparser.ConfigParser with additional methods """

    def __init__(self):
        super().__init__()

    def save(self, path):

        """
        Save config to path

        Args:
            path: str

        Returns:
            None

        """

        with open(path, 'w') as f:
            self.write(f)

    def get_section(self, section, options):

        """
        Equivalent of get but for section

        Args:
            section(str): section name
            options(dict): dict of options and type

        Returns:
            dict of options with corresponding parsed values

        """
        assert self.has_section(section), 'section {} not found'.format(section)
        assert isinstance(options, dict), 'options must be a dict'

        sec = {}
        for opt, typ in options.items():
            if self.has_option(sec, opt):
                if typ == 'bool':
                    sec[opt] = self.getboolean(section, opt)
                elif typ == 'int':
                    sec[opt] = self.getint(section, opt)
                elif typ == 'float':
                    sec[opt] = self.getfloat(section, opt)
                elif typ == 'list':
                    sec[opt] = self.getlist(section, opt)
                elif typ == 'eval':
                    sec[opt] = eval(self.get(section, opt))
                elif typ == 'str':
                    sec[opt] = self.get(section, opt)
        return sec

    def dump_section(self, section, recursive=False, dump=None):

        """
        Get section and copy into dump, recurse if required

        Args:
            section: section name
            recursive: set True to copy recursively
            dump: (Optional) ConfigParser object to copy to

        """
        if dump is None:
            dump = ConfigParser()
        else:
            assert isinstance(dump, configparser.ConfigParser)

        if self.has_section(section):
            dump.add_section(section)
            for opt, val in self.items(section):
                dump.set(section, opt, val)
                if recursive:
                    dump = self.dump_section(val, recursive=recursive, dump=dump)
        else:
            return dump

    def rename_section(self, old, new):

        """ Renames section """

        if not self.has_section(old):
            raise ValueError("section {} does not exist".format(old))
        if self.has_section(new):
            raise ValueError("section {} already exists".format(new))

        self.add_section(new)
        for opt, val in self.items(old):
            self.set(new, opt, val)

        self.remove_section(old)

    def getlist(self, section, option):
        return ast.literal_eval(self.getlist(section, option))

    def getint(self, *args, **kwargs):
        return int(super().getfloat(*args, **kwargs))
