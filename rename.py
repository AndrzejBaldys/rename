import argparse
import os
import sys


def msg(string, msg_type='INFO'):
    print('[{}] {}'.format(msg_type, string))


def str2bool(value):
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    elif value.lower() in ('none', 'null', 'nil'):
        return None
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def check_content(path, digi):
    content = (os.listdir(path))
    msg(content, 'DEBUG')
    if len(content) == 0:
        msg('Directory is empty. Nothing to do.')
        sys.exit(0)
    if len(content) > (int('9' * digi)):
        msg('Directory contain more elements then it can be rename with provided argument --digits', 'ERROR')
        msg('Number of files in directory: {}'.format(len(content)))
        sys.exit(1)
    return content


parser = argparse.ArgumentParser(description='Rename files.')
parser.add_argument('--prefix',
                    type=str,
                    help='Prefix which will be used to create file name. Default is None.',
                    default=None)
parser.add_argument('--suffix',
                    type=str,
                    help='Suffix which will be used to create file name. Default is None.',
                    default=None)
parser.add_argument('--digits',
                    type=int,
                    help='Number of digits which will be used to distinguish files. Default is 4.',
                    default=4)
parser.add_argument('--all',
                    type=str2bool,
                    help='Rename all files with specified extension even if they fit the pattern '
                         '(prefix-digits-suffix). Default is true.',
                    default=True)
parser.add_argument('--path',
                    type=str,
                    help='Path to work directory.',
                    required=True)
parser.add_argument('--extension',
                    type=str,
                    help='All files with provided file extension will be renamed. Default is *.',
                    default='*')

arguments = parser.parse_args()

# Path: /home/python/Pictures/wallpapers


def main(args):
    msg(args.prefix)
    msg(args.suffix)
    msg(args.digits)
    msg(args.all)
    msg(args.path)
    msg(args.extension)

    msg(os.path.isdir(args.path))
    if not os.path.isdir(args.path):
        msg('Directory dose not exist: {}'.format(args.path), 'ERROR')
        sys.exit(1)

    directory_content = None

    if args.all and args.extension == '*':
        # rename all files
        directory_content = check_content(args.path, args.digits)
        directory_content = sorted(directory_content)
        for file in directory_content:
            if args.prefix is None:
                prefix = ''
            else:
                prefix = args.prefix
            if args.suffix is None:
                suffix = ''
            else:
                suffix = args.suffix
            ext = file.split('.')[-1]
            counter = 0
            os.rename(os.path.join(args.path, file),
                      os.path.join(args.path, '{}{:0{width}}{}.{}'.format(prefix, counter,
                                                                           suffix, ext, width=args.digits)))
            counter += 1
    elif args.all and args.extension != '*':
        # rename all files with specified extension
        pass
    elif not args.all and args.extension != '*':
        # rename files with specifies extension which don't fit the pattern
        pass
    elif not args.all and args.extension == '*':
        # rename files witch don't fit the pattern
        pass


if __name__ == "__main__":
    main(arguments)
