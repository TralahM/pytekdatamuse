"""
The Datamuse API is a word-finding query engine for developers.

You can use it in your apps to find words that match a given set of constraints and that are likely in a given context.
You can specify a wide variety of constraints on meaning, spelling, sound, and vocabulary in your queries, in any combination.

The API gives you programmatic access to most of the functionality of Datamuse's websites, including OneLook, RhymeZone, Rimar.io, and WikSearch.

"""
from .api_client import (
    Datamuse,
    DOC_QUERY_PARAMETERS,
    yaml,
    requests,
)

__version__ = "0.0.4"

__author__ = "Tralah M Brian."

__all__ = [
    "Datamuse",
    "DOC_QUERY_PARAMETERS",
    "yaml",
    "requests",
]
