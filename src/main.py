import argparse
from plotter import generate_chart


def main():
    parser = argparse.ArgumentParser(description='Sorting algorithms comparison')

    parser.add_argument('INPUT_FILE',
                        help='Path to the file generated by `pytest --benchmark-json=PATH`')
    parser.add_argument('OUTPUT_FILE',
                        help='Output file path')
    parser.add_argument('-s', '--separate', action='store_true',
                        help='Generate separate chart for each algorithm')

    args = parser.parse_args()
    generate_chart(args.INPUT_FILE, args.OUTPUT_FILE, args.separate)


if __name__ == '__main__':
    main()
