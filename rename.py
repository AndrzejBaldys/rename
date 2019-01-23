import argparse
import os
import sys
import re


parser = argparse.ArgumentParser(description='Rename files.')
parser.add_argument('--prefix',
                    type=str,
                    help='Prefix which will be used to create file name. Default is None.',
                    default='')
parser.add_argument('--suffix',
                    type=str,
                    help='Suffix which will be used to create file name. Default is None.',
                    default='')
parser.add_argument('--digits',
                    type=int,
                    help='Number of digits which will be used to distinguish files. Default is 4.',
                    default=4)
parser.add_argument('--path',
                    type=str,
                    help='Path to work directory.',
                    required=True)
parser.add_argument('--extension',
                    type=str,
                    help='All files with provided file extension will be renamed. Default is *.',
                    default='*')

arguments = parser.parse_args()


def msg(_string, _msg_type='INFO'):
    """
    Prints message with specified prefix.

    :param _string: Message to print
    :param _msg_type: Message qualifier
    :return: None
    """
    print('[{}] {}'.format(_msg_type, _string))


def check_content(_path, _digi):
    """
    Gets directory content and validates it.

    :param _path: Directory path
    :param _digi: Width of unique part of the file name
    :return: Listed files
    """
    _content = (os.listdir(_path))
    if len(_content) == 0:
        msg('Directory is empty. Nothing to do.')
        sys.exit(0)
    if len(_content) > (int('9' * _digi)):
        msg('Directory contains more elements of specified type then '
            'it can be renamed with provided argument --digits', 'ERROR')
        sys.exit(1)
    return _content

# Path: /home/python/Pictures/wallpapers


def main(args):
    """
    Gets directory content and renames it accordingly.

    :param args: Arguments which have been provided to script
    :return: None
    """
    msg('path:      {}'.format(args.path))
    msg('prefix:    {}'.format(args.prefix))
    msg('digits:    {}'.format(args.digits))
    msg('suffix:    {}'.format(args.suffix))
    msg('extension: {}'.format(args.extension.lower()))

    def rename(_file, _counter):
        """
        Renames file.

        :param _file: File to rename
        :param _counter: Unique file number
        :return: None
        """
        _ext = _file.lower().split('.')[-1]
        os.rename(os.path.join(args.path, _file),
                  os.path.join(args.path, '{}{:0{width}}{}.{}'.format(args.prefix, _counter,
                                                                      args.suffix, _ext, width=args.digits)))

    def match_file(_file):
        """
        Checks if file should be renamed.

        :param _file: File to check
        :return: Corresponding match object
        """
        if args.extension == '*':
            _pattern = r'\..*$'
        else:
            _pattern = r'\.{}$'.format(args.extension.lower())
        return re.search(_pattern, _file)

    def iterate_through_dir():
        """
        Iterates through directory content.

        :return: None
        """
        _directory_content = check_content(args.path, args.digits)
        _directory_content = sorted(_directory_content)
        _counter = 0
        for _file in _directory_content:
            if os.path.isfile(os.path.join(args.path, _file)) and match_file(_file):
                rename(_file, _counter)
            _counter += 1

    if not os.path.isdir(args.path):
        msg('Directory dose not exist: {}'.format(args.path), 'ERROR')
        sys.exit(1)

    if args.extension != '*':
        iterate_through_dir()
    else:
        iterate_through_dir()


if __name__ == "__main__":
    main(arguments)
