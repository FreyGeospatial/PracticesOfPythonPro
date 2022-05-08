import re

product_review = '''This is a fine milk, but the product line appears to be limited in available colors.
I could only find white.'''

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL) # matches full sentences ending with a period
matches = sentence_pattern.findall(product_review) # returns a list of tuples. Includes whitespaces, page breaks.
sentences = [match[0] for match in matches] # grabs the first item of each tuple