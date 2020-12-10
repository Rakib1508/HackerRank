from html.parser import HTMLParser as Parser

class ParseTool(Parser):
    def handle_starttag(self, tag, attributes):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attributes]
        
html = '\n'.join([input() for _ in range(int(input()))])
scanner = ParseTool()
scanner.feed(html)
scanner.close()
