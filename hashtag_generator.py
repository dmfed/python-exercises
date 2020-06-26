'''
This one is very simple. We need to generate a hashtag
of maximum 140 symbols from the input string.
'''

def generate_hashtag(s):
    if len(s) == 0:
        return False
    result = "".join (["#"] + [item.title() for item in s.strip().split()])
    return result if len(result) <= 140 else False

print(generate_hashtag('Do We have A Hashtag'))
