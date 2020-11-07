"""Api Client for Interacting with the Datamuse API."""
import requests
import yaml

DOC_QUERY_PARAMETERS = {
    "ml": "Means like",
    "sl": "Sounds like",
    "sp": "Spelled like",
    "rel_jja": "Related popular nouns modified by the given adjective.",
    "rel_jjb": "Related popular adjectives used to modify the given noun.",
    "rel_syn": "Related Synonyms",
    "rel_trg": "Related Triggers(words statistically associated with the word.)",
    "rel_ant": "Related Antonyms",
    "rel_spc": "Related Hypernyms (Kind of)",
    "rel_gen": "Related Hyponyms (More General than)",
    "rel_com": "Related Holonyms (Comprises)",
    "rel_par": "Related Meronyms (Part of)",
    "rel_bga": "Related Frequent Followers",
    "rel_bgb": "Related Frequent Predecessors",
    "rel_rhy": "Related Perfect Rhymes",
    "rel_nry": "Related Approximate Rhymes",
    "rel_hom": "Related Homophones (Sound-alike words)",
    "rel_cns": "Related Consonant Match",
    "v": "vocabulary identifier to use, es for spanish. default english",
    "topics": "optional hint of the theme of the document being written.",
    "lc": "left context words appearing before word",
    "rc": "right context words appearing after word",
    "max": "maximum number of results to return",
    "md": [
        "p",
        "d",
        "s",
        "r",
        "f",
        {
            "md": "metadata",
            "p": "parts of speech",
            "d": "definition",
            "s": "sylable count",
            "r": "pronounciation",
            "f": "word frequency",
        },
    ],
    "qe": "query echo, prepend a result to the output that describes a query string from some other parameter",
    "s": "for Sup endpoint prefix hint string typically the characters the user has entered so far.",
}


class Datamuse:
    """Datamuse class."""

    WORD_PARAMS = [
        "ml",
        "sl",
        "sp",
        "rel_jja",
        "rel_jjb",
        "rel_syn",
        "rel_trg",
        "rel_ant",
        "rel_spc",
        "rel_gen",
        "rel_com",
        "rel_par",
        "rel_bga",
        "rel_bgb",
        "rel_rhy",
        "rel_nry",
        "rel_hom",
        "rel_cns",
        "v",
        "topics",
        "lc",
        "rc",
        "max",
        "md",
        "qe",
    ]

    SUGGEST_PARAMS = ["s", "max", "v"]

    def __init__(self):
        """Initialize API Client."""
        self.words_endpoint = "https://api.datamuse.com/words"
        self.suggestions_endpoint = "https://api.datamuse.com/sug"

    def _validate_max(self, max_results):
        """Validate Max."""
        if not (0 < max_results <= 1000):
            raise ValueError(
                "Datamuse only supports values of max in (0, 1000]")
        return

    def _validate_args(self, args, param_set):
        """Validate Args."""
        for arg in args:
            if arg not in param_set:
                raise ValueError(
                    "{0} is not a valid parameter for this endpoint.".format(
                        arg)
                )
            if arg == "max":
                self._validate_max(args[arg])
        return

    def words(self, **kwargs):
        """Get words API."""
        self._validate_args(kwargs, self.WORD_PARAMS)
        response = requests.get(self.words_endpoint, kwargs)
        return response.json()

    def suggestions(self, **kwargs):
        """Get suggestions API."""
        self._validate_args(kwargs, self.SUGGEST_PARAMS)
        response = requests.get(self.suggestions_endpoint, kwargs)
        return response.json()

    def autocomplete(self, word, **kwargs):
        """Get completion suggestions of word."""
        return self.suggestions(s=word, **kwargs)

    def means_like(self, word, max=20, **kwargs):
        """Get Related Means Like words."""
        return self.words(ml=word, max=max, **kwargs)

    def sounds_like(self, word, max=20, **kwargs):
        """Get Related Sounds Like words."""
        return self.words(sl=word, max=max, **kwargs)

    def spelled_like(self, word, max=20, **kwargs):
        """Get Related Spelled Like words."""
        return self.words(sp=word, max=max, **kwargs)

    def left_context(self, word, max=20, **kwargs):
        """Get Left Context words appearing before word."""
        return self.words(lc=word, max=max, **kwargs)

    def right_context(self, word, max=20, **kwargs):
        """Get Right Context words appearing after word."""
        return self.words(rc=word, max=max, **kwargs)

    def rhymes(self, word, max=20, **kwargs):
        """Get Perfect Rhymes."""
        return self.words(rel_rhy=word, max=max, **kwargs)

    def approx_rhymes(self, word, max=20, **kwargs):
        """Get Approximate Rhymes."""
        return self.words(rel_nry=word, max=max, **kwargs)

    def synonyms(self, word, **kwargs):
        """Get synonyms."""
        return self.words(rel_syn=word, **kwargs)

    def antonyms(self, word, **kwargs):
        """Get antonyms."""
        return self.words(rel_ant=word, **kwargs)

    def homophones(self, word, **kwargs):
        """Get homophones sound alike words."""
        return self.words(rel_hom=word, **kwargs)

    def holonyms(self, word, **kwargs):
        """Get Related Holonyms (Comprises)."""
        return self.words(rel_com=word, **kwargs)

    def hyponyms(self, word, **kwargs):
        """Get Related Hyponyms (More General Than)."""
        return self.words(rel_gen=word, **kwargs)

    def hypernyms(self, word, **kwargs):
        """Get Related Hypernyms (Kind of)."""
        return self.words(rel_spc=word, **kwargs)

    def meronyms(self, word, **kwargs):
        """Get Related Meronyms (Part of)."""
        return self.words(rel_par=word, **kwargs)

    def consonant_match(self, word, **kwargs):
        """Get Related Consonant Match."""
        return self.words(rel_cns=word, **kwargs)

    def followers(self, word, **kwargs):
        """Get Related Frequent Followers."""
        return self.words(rel_bga=word, **kwargs)

    def predecessors(self, word, **kwargs):
        """Get Related Frequent Predecessors."""
        return self.words(rel_bgb=word, **kwargs)

    def triggers(self, word, **kwargs):
        """Get Related Popular triggers words statistically associated with the word. ."""
        return self.words(rel_trg=word, **kwargs)

    def noun_modifiers(self, noun, **kwargs):
        """Get Related Popular Adjectives modifying the noun."""
        return self.words(rel_jjb=noun, **kwargs)

    def adj_modifiers(self, adj, **kwargs):
        """Get Related Popular Nouns modified by the adjective."""
        return self.words(rel_jja=adj, **kwargs)

    def define(self, word, max=1, **kwargs):
        """Get Definitions of a Word."""
        return self.words(sp=word, max=max, md="d", **kwargs)

    def __str__(self):
        """Represent obj."""
        return """Datamuse API(https://api.datamuse.com/)\nSupported Query
        Params:\n""" + yaml.dump(
            DOC_QUERY_PARAMETERS
        )

    def __repr__(self):
        """Represent obj."""
        return """Datamuse API(https://api.datamuse.com/)\nSupported Query
        Params:\n""" + yaml.dump(
            DOC_QUERY_PARAMETERS
        )
