#!./venv/bin/python

from lib.database import init_database
from lib.parser import parse_args


def main(args):
    args = parse_args()

    init_database()

    match args.function:
        case "import":
            pass


if __name__ == "__main__":
    args = parse_args()
    main(args)
