#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "ariannagbasha, collabs: Sondos and Shanquel plus Tracy "


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument('text',
                        help='text to be manipulated')
    parser.add_argument('-u', '--upper',
                        help="convert text to uppercase", action='store_true')
    parser.add_argument('-l', '--lower',
                        help="convert text to lowercase", action='store_true')
    parser.add_argument('-t', '--title',
                        help="convert text to titlecase", action='store_true')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    # NAMESPACE called "ns"
    ns = parser.parse_args(args)
    # option flag
    if not ns:
        parser.print_usage()
        sys.exit(1)
        return
    text = ns.text
    final_text_trans = text
    # print(str(text))
    if ns.upper:
        final_text_trans = text.upper()
    if ns.lower:
        final_text_trans = text.lower()
    if ns.title:
        final_text_trans = text.title()
    print(final_text_trans)


if __name__ == '__main__':
    main(sys.argv[1:])
