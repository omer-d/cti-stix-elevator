import os
import sys

from stix2elevator import elevate_file
from stix2elevator.cli import _get_arg_parser
from stix2elevator.options import initialize_options, set_option_value


def main():
    elevator_parser = _get_arg_parser(False)

    elevator_parser.add_argument(
        "dir_",
        help="A directory contaning STIX 1.x documents to be elevated.",
        metavar="dir"
    )

    elevator_parser.add_argument(
        "--output-directory",
        help="output logs",
        dest="output_directory",
        action="store",
        default=None
    )
    elevator_args = elevator_parser.parse_args()
    initialize_options(elevator_args)

    for filename in os.listdir(elevator_args.dir_):
        path = os.path.join(elevator_args.dir_, filename)

        if path.endswith(".xml"):
            sys.stdout.write(path + "\n")
            file_and_ext = filename.split(".")
            set_option_value("file_", file_and_ext[0])
            result = elevate_file(path)

            if elevator_args.output_directory:
                destination = os.path.join(elevator_args.output_directory, file_and_ext[0] + ".json")
                destination = os.path.abspath(destination)
                output_file = open(destination, "w")
                output_file.write(result)
                output_file.close()
            else:
                print(result + "\n")


if __name__ == '__main__':
    main()
