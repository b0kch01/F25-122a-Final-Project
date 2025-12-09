#!./venv/bin/python

from lib.commands import import_data

from lib.database import init_database
from lib.parser import parse_args


def main(args):
    args = parse_args()
    db = init_database()

    match args.function:
        case "import":
            import_data.run(db, args)


if __name__ == "__main__":
    args = parse_args()
    main(args)
