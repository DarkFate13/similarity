from BeautifulSoup import BeautifulSoup
import re

def HTML_stripper(inStr):
    htmlStripped =  BeautifulSoup(inStr).text
    bracketStripped = re.sub(r'\([^)]*\)', '', htmlStripped)
    return bracketStripped[2:]
    
if __name__ == '__main__':
    print HTML_stripper('<B>2 (a)</B>What is an Algorithm? Write an algorithm to find largest of 3 numbers.')