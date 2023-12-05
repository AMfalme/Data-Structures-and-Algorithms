# 
# Given a word (lower case letters only), and a set of
# tiles that can be used to make a word (also a string, 
# each tile is one lower case letter or underscore), determine 
# the point value possible for the word. The underscore represents
# a blank tile that can stand in for any letter but has a zero point
#  value.
# 
# 
# Points per tile are:
# 
# a: 1, b: 3, c: 3, d: 2, e: 1, f: 4, g: 2, h: 4, i: 1, j: 8,
# k: 5, l: 1, m: 3, n: 1, o: 1, p: 3, q: 10, r: 1, s: 1, t: 1,
# u: 1, v: 4, w: 4, x: 8, y: 4, z: 10, _: 0
# 
# 
# Example:
# --- word: cat
# --- tiles: tmoca
# --- results: 5 (3 + 1 + 1)
# 
# --- word: cat
# --- tiles: tmoa_
# --- results: 2 (1 + 1)
# --- 
# 
# 
# 
letterPointValues = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '_': 0
}

def calculatePoints(word, tiles):
    result = 0
    for letter in word:
        if letter in tiles:
            result += letterPointValues[letter]
            tiles.
    
    return result    
    
print(calculatePoints('cat', ['t', 'm', 'o', '_', 'a']))
print(calculatePoints('cat', 'tmoca'))