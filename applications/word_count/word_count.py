import string

def word_count(s):
    
    words = {}
    
    s.translate(None, string.punctuation) 
    
    for word in s.split():
        word = word.lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    
    items = dict(words.items())
    print(items)

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))