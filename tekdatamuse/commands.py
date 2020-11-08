#!/usr/bin/env python
"""TekDatamuse Entry Points."""
import tekdatamuse
import argparse


def antonyms(args):
    """Get antonymns subcommand."""
    defs = tekdatamuse.Datamuse().antonyms(args.word)
    for d in defs:
        print(d.get("word"))
    return


def synonyms(args):
    """Get synonyms subcommand."""
    defs = tekdatamuse.Datamuse().synonyms(args.word)
    for d in defs:
        print(d.get("word"))
    return


def means_like(args):
    """Get means like subcommand."""
    defs = tekdatamuse.Datamuse().means_like(args.word)
    for d in defs:
        print(d.get("word"))
    return


def sounds_like(args):
    """Get sounds like subcommand."""
    defs = tekdatamuse.Datamuse().sounds_like(args.word)
    for d in defs:
        print(d.get("word"))
    return


def spelled_like(args):
    """Get spelled like subcommand."""
    defs = tekdatamuse.Datamuse().spelled_like(args.word)
    for d in defs:
        print(d.get("word"))
    return


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


def build_subparsers(subparsers, subcommands):
    """Build subparsers."""
    for subc, fun in subcommands.items():
        p = subparsers.add_parser(
            subc,
            aliases=[
                fun[1],
            ],
            help=fun[2],
        )
        p.add_argument(
            "word",
            metavar="WORD",
        )
        p.set_defaults(func=fun[0])
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
        "define",
        help="Get definition of word",
        aliases=[
            "def",
        ],
    )
    def_subparser.add_argument("word")
    def_subparser.set_defaults(func=define)
    subcommands = {
        "sounds_like": [sounds_like, "sl", "get words sounding like word"],
        "means_like": [means_like, "ml", "get words meaning like phrase"],
        "antonyms": [antonyms, "ant", "get words antonyms of word"],
        "synonyms": [synonyms, "syn", "get words synonyms of word"],
        "spelled_like": [spelled_like, "sp", "get words spelled like pattern"],
    }
    build_subparsers(subparsers, subcommands)
    args = parser.parse_args()
    args.func(args)
    return
