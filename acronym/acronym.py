def abbreviate(phrase):
    return ''.join([x for x in phrase.title() if x.upper() == x and x.isalpha()])
    
#print(abbreviate('Portable Network Graphics'))
#print(abbreviate('Ruby on Rails'))
#print(abbreviate('First In, First Out'))
#print(abbreviate('GNU Image Manipulation Program'))
#print(abbreviate('Complementary metal-oxide semiconductor'))


