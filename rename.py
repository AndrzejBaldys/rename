import argparse


def msg(string, msg_type='INFO'):
    print('[{}] {}'.format(msg_type, string))


def str2bool(value):
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


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
                    help='Number of digits which will be used distinguish files. Default is 4.',
                    default=4)
parser.add_argument('--all',
                    type=str2bool,
                    help='Rename all files even if they fit the pattern (prefix-digits-suffix). Default is true.',
                    default=True)

arguments = parser.parse_args()


def main(args):
    msg(args.prefix)
    msg(args.suffix)
    msg(args.digits)
    msg(args.all)


if __name__ == "__main__":
    main(arguments)
