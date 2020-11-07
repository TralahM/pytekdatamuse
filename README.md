[![Build Status](https://travis-ci.com/TralahM/pytekdatamuse.svg?branch=master)](https://travis-ci.com/TralahM/pytekdatamuse)
[![Build status](https://ci.appveyor.com/api/projects/status/yvvmq5hyf7hj743a/branch/master?svg=true)](https://ci.appveyor.com/project/TralahM/pytekdatamuse/branch/master)
[![Documentation Status](https://readthedocs.org/projects/pytekdatamuse/badge/?version=latest)](https://pytekdatamuse.readthedocs.io/en/latest/?badge=latest)
[![License: GPLv3](https://img.shields.io/badge/License-GPLV2-green.svg)](https://opensource.org/licenses/GPLV2)
[![Organization](https://img.shields.io/badge/Org-TralahTek-blue.svg)](https://github.com/TralahTek)
[![Views](http://hits.dwyl.io/TralahM/pytekdatamuse.svg)](http://dwyl.io/TralahM/pytekdatamuse)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square)](https://github.com/TralahM/pytekdatamuse/pull/)
[![GitHub pull-requests](https://img.shields.io/badge/Issues-pr-red.svg?style=flat-square)](https://github.com/TralahM/pytekdatamuse/pull/)
[![Language](https://img.shields.io/badge/Language-python-3572A5.svg)](https://github.com/TralahM)
<img title="Watching" src="https://img.shields.io/github/watchers/TralahM/pytekdatamuse?label=Watchers&color=blue&style=flat-square">
<img title="Stars" src="https://img.shields.io/github/stars/TralahM/pytekdatamuse?color=red&style=flat-square">
<img title="Forks" src="https://img.shields.io/github/forks/TralahM/pytekdatamuse?color=green&style=flat-square">

# pytekdatamuse.


[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-black.svg?style=for-the-badge&logo=github)](https://github.com/TralahTek)
[![TralahM](https://img.shields.io/badge/Engineer-TralahM-blue.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)

# Documentation

[![Documentation](https://img.shields.io/badge/Docs-pytekdatamuse-blue.svg?style=for-the-badge)](https://github.com/TralahM/pytekdatamuse)

Look at the [Datamuse API Docs](http://www.datamuse.com/api/) for a detailed
description.

## How to Install
```bash
# In terminal do:
$ pip install pytekdatamuse
```
## Usage
You can use the cli script

```console
$ tekdatamuse define hypotheses
hypotheses
N 	 a tentative theory about the natural world; a concept that is not yet verified but that if true would explain certain facts or phenomena
N 	 a proposal intended to explain certain facts or observations
N 	 a message expressing an opinion based on incomplete evidence
```

### From python scripts

```python

import tekdatamuse
api=tekdatamuse.Datamuse()
# words
words=api.words(sp="early",md="d")

# get synonyms
syns=api.synonyms("look")

# get antonyms
antonyms=api.antonyms("look")

# get holonyms
holonyms=api.holonyms("look")

# get hypernyms
hypernyms=api.hypernyms("look")

# get hyponyms
hyponyms=api.hyponyms("look")

# get meronyms
meronyms=api.meronyms("look")

# get homophones
homophones=api.homophones("look")

# get rhymes
rhymes=api.rhymes("look")

# get approximate rhymes
approx_rhymes=api.approx_rhymes("look")

# get popular adjectives modifying a noun
noun_modifiers=api.noun_modifiers("look")

# get popular nouns modified by the  adjective
adj_modifiers=api.adj_modifiers("look")

# get word definition
define=api.define("hypotheses")

# autocomplete
completions=api.autocomplete("boo",max=20)

# followers
followers=api.followers("early")

# predecessors
predecessors=api.predecessors("early")

# right_context
right_context=api.right_context("early")

# left_context
left_context=api.left_context("early")

# triggers
triggers=api.triggers("early")

# means_like
means_like=api.means_like("early")

# sounds_like
sounds_like=api.sounds_like("early")

# spelled_like
spelled_like=api.spelled_like("early")

```

## Building from Source for Developers

```console
$ git clone https://github.com/TralahM/pytekdatamuse.git
$ cd pytekdatamuse
```

# Contributing
[See the Contributing File](CONTRIBUTING.rst)


[See the Pull Request File](PULL_REQUEST_TEMPLATE.md)


# Support

# LICENCE

[Read the license here](LICENSE)


# Self-Promotion

[![](https://img.shields.io/badge/Github-TralahM-green?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![](https://img.shields.io/badge/Twitter-%40tralahtek-red?style=for-the-badge&logo=twitter)](https://twitter.com/TralahM)
[![TralahM](https://img.shields.io/badge/Kaggle-TralahM-purple.svg?style=for-the-badge&logo=kaggle)](https://kaggle.com/TralahM)
[![TralahM](https://img.shields.io/badge/LinkedIn-TralahM-red.svg?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/TralahM)


[![Blog](https://img.shields.io/badge/Blog-tralahm.tralahtek.com-blue.svg?style=for-the-badge&logo=rss)](https://tralahm.tralahtek.com)

[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-cyan.svg?style=for-the-badge)](https://org.tralahtek.com)


