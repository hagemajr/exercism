def word_count(msg):
    word_list = msg.strip().replace('\t', ' ').replace('\n', ' ').replace('_', ' ').replace(',',' ').split(" ")
    word_counts = {}
    for word in word_list:
        word = "".join([x for x in word.lower().strip("'").strip('.') if x.isalnum() or x == "'"])
        
        if len(word) > 0:
            if word in word_counts.keys():
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts

print(word_count(' multiple   whitespaces'))
#testing coda workflow