from ..parsers import parse_cmd_args
from gendiff.differ import generate_diff


def main():
    args = parse_cmd_args()

    first_file = args.first_file
    second_file = args.second_file

    print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
