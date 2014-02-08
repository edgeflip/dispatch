import os
import subprocess
import textwrap

import pypandoc


def main(cmd, infile, outfile, save=False, force=False):
    assert force or not os.path.exists(outfile), "%s exists" % outfile

    output = pypandoc.convert(infile, 'rst')
    with open(outfile, 'w') as fh:
        fh.write(output)

    try:
        subprocess.check_call(['python', 'setup.py'] + cmd)
    finally:
        if not save:
            os.remove(outfile)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=textwrap.dedent("""\
        Convert the project README, in Markdown, to reStructuredText, and
        and run the given setup.py command"""))
    parser.add_argument('cmd',
        help='The setup.py command to run, with optional arguments, '
             'e.g. sdist upload',
        nargs='+')
    parser.add_argument('-i', '--infile',
        help="Input README (Markdown)",
        default='README.md')
    parser.add_argument('-o', '--outfile',
        help="Output README (ReST)",
        default='README.txt')
    parser.add_argument('--save',
        help="Whether to save output file",
        action='store_true')
    parser.add_argument('--force',
        help="Whether to overwrite existing output file",
        action='store_true')
    args = parser.parse_args()
    main(**vars(args))
