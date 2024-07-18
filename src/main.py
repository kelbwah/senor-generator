from textnode import TextNode

def main():
    text = "This is a text node"
    text_type = "bold"
    url = "https://www.boot.dev"

    textNode = TextNode(text, text_type, url) 
    print(textNode) 

if __name__ == "__main__":
    main() 
