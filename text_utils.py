import argparse
from sys import stdin, stdout


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=argparse.FileType('r'), default=stdin, help='Input')
    parser.add_argument('--output', type=argparse.FileType('w'), default=stdout, help='Output')
    parser.add_argument('--layer', type=int, required=True)

    # subparser = parser.add_subparsers(dest='subparser_name')
    # split = subparser.add_parser('split')

    return parser


if __name__ == '__main__':
    args = create_parser().parse_args()

    with args.input as f:
        lines = f.read().splitlines()

    K = 3
    i = 0
    while lines:
        i += 1
        with open('/u/tran/working_folder/test/layer-{}.block-{}'.format(args.layer, i), 'w') as out:
            k = 0
            while k < K and lines:
                line = lines.pop(0)
                if line == '':
                    k += 1
                out.write(line + '\n')


