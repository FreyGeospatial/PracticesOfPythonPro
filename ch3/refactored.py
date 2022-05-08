import re

def get_matches_for_pattern(pattern, string): # takes regular expression, string
    matches = pattern.findall(string)
    return [match[0] for match in matches]


parse_this = '''This is a fine milk, but the product line appears to be limited in available colors.
I could only find white.'''

pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL) # matches full sentences ending with a period
sentences = get_matches_for_pattern(
    pattern,
    parse_this
)

# parse sentences into words
word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    words = get_matches_for_pattern(
        word_pattern,
        sentence
    )
    print(words)