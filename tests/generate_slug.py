import argparse
import os
import sys
import time

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_PATH not in sys.path:
    sys.path.append(PROJECT_PATH)

from coolname import generate_slug


def main(argv):
    parser = argparse.ArgumentParser(description='Generate slug in stdout')
    parser.add_argument('--word', help='With particular substring')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    args = parser.parse_args(argv)
    generate_slug()  # for more precise timing
    if args.word:
        slug = None
        max_slugs = 100000
        for i in range(0, max_slugs):
            start_time = time.perf_counter()
            s = generate_slug()
            elapsed_time = time.perf_counter() - start_time
            if args.word in s:
                slug = s
                break
        if slug is None:
            print('Failed to generate in {} attempts'.format(max_slugs))
            return 1
    else:
        start_time = time.perf_counter()
        slug = generate_slug()
        elapsed_time = time.perf_counter() - start_time
    print(slug)
    if args.verbose:
        sys.stderr.write('Generated in {:0.06f} seconds\n'.format(elapsed_time))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
