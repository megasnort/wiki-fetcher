import sys
import json
from urllib.request import urlopen
from urllib.parse import quote_plus


def fetch_wiki_entry_for(term, language):
    url = 'https://' + language + '.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=' + quote_plus(term) + '&redirects=1'
    print('Fetching "' + term + '" in "' + language + '"')
    response = urlopen(url)
    content = response.read()
    json_content = json.loads(content)

    for page in json_content['query']['pages']:
        try:
            return json_content['query']['pages'][page]['extract']
        except KeyError:
            pass


def parse_line(term, language, cleanup):
    if cleanup:
        brace_pos = term.find('(')
        if brace_pos != -1:
            term = term[0:brace_pos]

    return term.strip()

try:
    language = sys.argv[1]
    input_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    cleanup = (len(sys.argv) == 5 and sys.argv[4] == '--clean')

    with open(input_file_path, 'r') as input_file:
        lines = input_file.read().splitlines()

    with open(output_file_path, 'w') as output_file:
        for term in lines:
            cleaned_term = parse_line(term, language, cleanup)

            if cleaned_term:
                entry = fetch_wiki_entry_for(cleaned_term, language)

                if entry is None:
                    entry = fetch_wiki_entry_for(cleaned_term, 'en')

                if entry is None:
                    entry = 'Nothing found!'

                output_file.write(term + '\n\n' + entry + '\n\n==========================\n\n')

        print('Output file written: ' + output_file_path)

except IndexError:
    print('Supply a valid language, input and output file like so:')
    print('python wiki_fetcher.py nl input_file.txt output_file.txt')
    exit(1)
