import argparse
from urllib.request import urlopen

def fetch_words(url):
    story = urlopen(url)
    storyWords = []
    for line in story:
        lineWords = line.decode('utf8').split()
        for word in lineWords:
            storyWords.append(word)
    story.close()
    return storyWords
def print_items(items):    
    for item in items:
        print(item)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url")
    args = parser.parse_args()
    url = args.url #When running the file itself, 
    #Sample url:
    #url = 'https://simple.wikipedia.org/wiki/Subatomic_particle'
    words = fetch_words(url)
    print_items(words)
if __name__ == '__main__':
    main()
