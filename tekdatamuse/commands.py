#!/usr/bin/env python
"""TekDatamuse Entry Points."""
import tekdatamuse
import argparse


def homophones(args):
    """Get homophoness subcommand."""
    defs = tekdatamuse.Datamuse().homophones(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def holonyms(args):
    """Get holonymss subcommand."""
    defs = tekdatamuse.Datamuse().holonyms(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def hypernyms(args):
    """Get hypernymss subcommand."""
    defs = tekdatamuse.Datamuse().hypernyms(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def hyponyms(args):
    """Get hyponymss subcommand."""
    defs = tekdatamuse.Datamuse().hyponyms(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def meronyms(args):
    """Get meronymss subcommand."""
    defs = tekdatamuse.Datamuse().meronyms(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def followers(args):
    """Get followerss subcommand."""
    defs = tekdatamuse.Datamuse().followers(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def predecessors(args):
    """Get predecessorss subcommand."""
    defs = tekdatamuse.Datamuse().predecessors(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def left_context(args):
    """Get left_contexts subcommand."""
    defs = tekdatamuse.Datamuse().left_context(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def right_context(args):
    """Get right_contexts subcommand."""
    defs = tekdatamuse.Datamuse().right_context(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def consonant_match(args):
    """Get consonant_matchs subcommand."""
    defs = tekdatamuse.Datamuse().consonant_match(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def autocomplete(args):
    """Get autocompletes subcommand."""
    defs = tekdatamuse.Datamuse().autocomplete(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def antonyms(args):
    """Get antonymns subcommand."""
    defs = tekdatamuse.Datamuse().antonyms(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def synonyms(args):
    """Get synonyms subcommand."""
    defs = tekdatamuse.Datamuse().synonyms(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def means_like(args):
    """Get means like subcommand."""
    defs = tekdatamuse.Datamuse().means_like(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def sounds_like(args):
    """Get sounds like subcommand."""
    defs = tekdatamuse.Datamuse().sounds_like(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def spelled_like(args):
    """Get spelled like subcommand."""
    defs = tekdatamuse.Datamuse().spelled_like(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def rhymes(args):
    """Get rhymes subcommand."""
    defs = tekdatamuse.Datamuse().rhymes(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def approx_rhymes(args):
    """Get approx_rhymes subcommand."""
    defs = tekdatamuse.Datamuse().approx_rhymes(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def noun_modifiers(args):
    """Get noun_modifiers subcommand."""
    defs = tekdatamuse.Datamuse().noun_modifiers(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def adj_modifiers(args):
    """Get adj_modifiers subcommand."""
    defs = tekdatamuse.Datamuse().adj_modifiers(args.word, max=args.max)
    for d in defs:
        print(d.get("word"))
    return


def triggers(args):
    """Get triggers subcommand."""
    defs = tekdatamuse.Datamuse().triggers(args.word, max=args.max)
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
        )
        p.add_argument(
            "word",
            metavar="WORD",
            help=fun[2],
        )
        p.add_argument(
            "-m",
            "--max",
            action="store",
            dest="max",
            default=10,
            type=int,
            help="maximum number of records to return default 10 upto 1000",
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
        "autocomplete": [
            autocomplete,
            "ac",
            "get words autocomplete of word",
        ],
        "consonant_match": [
            consonant_match,
            "cm",
            "get words consonant_match of word",
        ],
        "right_context": [
            right_context,
            "rc",
            "get words right_context of word",
        ],
        "left_context": [
            left_context,
            "lc",
            "get words left_context of word",
        ],
        "predecessors": [
            predecessors,
            "pre",
            "get words predecessors of word",
        ],
        "followers": [
            followers,
            "fol",
            "get words followers of word",
        ],
        "meronyms": [
            meronyms,
            "mer",
            "get words meronyms of word",
        ],
        "hyponyms": [
            hyponyms,
            "hypo",
            "get words hyponyms of word",
        ],
        "hypernyms": [
            hypernyms,
            "hyper",
            "get words hypernyms of word",
        ],
        "holonyms": [
            holonyms,
            "hol",
            "get words holonyms of word",
        ],
        "homophones": [
            homophones,
            "hom",
            "get words homophones of word",
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
        "define": [
            define,
            "def",
            "get definition of word.",
        ],
    }
    build_subparsers(subparsers, subcommands)
    args = parser.parse_args()
    args.func(args)
    return
