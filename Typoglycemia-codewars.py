'''
Background
There is a message that is circulating via public media that claims a 
reader can easily read a message where the inner letters of each words 
is scrambled, as long as the first and last letters remain the same and 
the word contains all the letters.

Another example shows that it is quite difficult to read the text where 
all the letters are reversed rather than scrambled.

In this kata we will make a generator that generates text in a similar 
pattern, but instead of scrambled or reversed, ours will be sorted 
alphabetically

Requirement
return a string where:

1) the first and last characters remain in original place for each word
2) characters between the first and last characters must be sorted 
alphabetically
3) punctuation should remain at the same place as it started, for 
example: shan't -> sahn't

Assumptions

1) words are seperated by single spaces
2) only spaces separate words, special characters do not, for example: 
tik-tak -> tai-ktk
3) special characters do not take the position of the non special 
characters, for example: -dcba -> -dbca
4) for this kata puctuation is limited to 4 characters: hyphen(-), 
apostrophe('), comma(,) and period(.)
5) ignore capitalisation
''' 

def scramble_words(words):
    words = words.split(" ")
    out = []
    for word in words:
        letters = [l for l in word if l.isalpha()]
        srtd_letters = letters[:1] + sorted(letters[1:-1]) + letters[-1:]
        result = [l if not l.isalpha() else srtd_letters.pop(0) for l in word]
        out.append("".join(result))
    return " ".join(out)
