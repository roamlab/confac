""" Extend configparser.ConfigParser with additional methods """

import configparser
import ast

class ConfigParser(configparser.ConfigParser):

    """ Extend configparser.ConfigParser with additional methods """

    def __init__(self):
        super().__init__()

    def save(self, path: str):

        """
        Save config to path

        Args:
            path: str

        Returns:
            None

        """

        with open(path, 'w') as f:
            self.write(f)

    def get_section(self, section: str, recursive=False, dump=None):

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
                    dump = self.get_section(val, recursive=recursive, dump=dump)
        else:
            return dump

    def rename_section(self, old: str, new: str):

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
