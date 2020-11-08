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


def rhymes(args):
    """Get rhymes subcommand."""
    defs = tekdatamuse.Datamuse().rhymes(args.word)
    for d in defs:
        print(d.get("word"))
    return


def approx_rhymes(args):
    """Get approx_rhymes subcommand."""
    defs = tekdatamuse.Datamuse().approx_rhymes(args.word)
    for d in defs:
        print(d.get("word"))
    return


def noun_modifiers(args):
    """Get noun_modifiers subcommand."""
    defs = tekdatamuse.Datamuse().noun_modifiers(args.word)
    for d in defs:
        print(d.get("word"))
    return


def adj_modifiers(args):
    """Get adj_modifiers subcommand."""
    defs = tekdatamuse.Datamuse().adj_modifiers(args.word)
    for d in defs:
        print(d.get("word"))
    return


def triggers(args):
    """Get triggers subcommand."""
    defs = tekdatamuse.Datamuse().triggers(args.word)
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
        "sounds_like": [
            sounds_like,
            "sl",
            "get words sounding like word",
        ],
        "means_like": [
            means_like,
            "ml",
            "get words meaning like phrase",
        ],
        "antonyms": [
            antonyms,
            "ant",
            "get words antonyms of word",
        ],
        "synonyms": [
            synonyms,
            "syn",
            "get words synonyms of word",
        ],
        "spelled_like": [
            spelled_like,
            "sp",
            "get words spelled like pattern",
        ],
        "rhymes": [
            rhymes,
            "rh",
            "get words rhymes for word.",
        ],
        "approx_rhymes": [
            approx_rhymes,
            "arh",
            "get words approximate rhymes for word.",
        ],
        "noun_modifiers": [
            noun_modifiers,
            "nm",
            "get popular adjectives modifying the  noun.",
        ],
        "adj_modifiers": [
            adj_modifiers,
            "am",
            "get popular nouns modified by the adjective.",
        ],
        "triggers": [
            triggers,
            "tg",
            "get trigger words statistically occuring with the word.",
        ],
    }
    build_subparsers(subparsers, subcommands)
    args = parser.parse_args()
    args.func(args)
    return
