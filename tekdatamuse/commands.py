#!/usr/bin/env python
"""TekDatamuse Entry Points."""
import tekdatamuse
import argparse


def define(args):
    """Define subcommand."""
    defs = tekdatamuse.Datamuse().define(args.word)
    for df in defs:
        print(df.get("word"))
        st = df.get("defs")
        if st:
            for s in st:
                print(s[0].upper(), "\t", s.split("\t")[-1])
    return


def usage(args):
    """Get usage."""
    return


def main():
    """Run main entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version",
        action="version",
        version=f"tekdatamuse {tekdatamuse.__version__}",
    )
    parser.set_defaults(func=usage)
    subparsers = parser.add_subparsers()
    def_subparser = subparsers.add_parser(
        "define", help="Get definition of word")
    def_subparser.add_argument("word")
    def_subparser.set_defaults(func=define)
    args = parser.parse_args()
    args.func(args)
    return
