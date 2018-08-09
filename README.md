# README

Simple python script to fetch the basic wikipedia info in a given language for a list of words. Except Python 3 it does not have any requirements.

## Usage

```bash
$ python3 wiki_fetcher.py nl input_file.txt output_file.txt
```

Where `input_file.txt` contains a *return separated* list of words, like so:

```python
lol
omg
braas
glaar
vier
hunkydrol
```

There is an optional fourth argument `--clean` with strips a pending string in the form of `(123)`. E.g. `hunkydrol (123` becomes `hunkydrol`. This was necessary for the specific project that this tool was developed for. Note that for some entries like `Beirut (band)` this is a problem.

If for the given language no entry is found, English is used as a fallback. 