import unittest

from textnode import ( 
    TextNode,
    text_type_bold, 
    text_type_code
)

class TestTextNode(unittest.TestCase):
    def test_init(self):
        text = "This is a text node"
        node = TextNode(text, text_type_bold) 

        self.assertEqual(node.text, text)
        self.assertEqual(node.text_type, text_type_bold)
        self.assertEqual(node.url, None)

    def test_init_with_url(self):
        text = "This is a text node"
        url = "https://kelbya.dev"
        node = TextNode(text, text_type_bold, url) 

        self.assertEqual(node.text, text)
        self.assertEqual(node.text_type, text_type_bold)
        self.assertEqual(node.url, url)

    def test_eq_true(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)

        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_code)

        self.assertNotEqual(node, node2)

    def test_repr_no_url(self):
        expected = "TextNode(This is a text node, bold, None)"
        node = TextNode("This is a text node", text_type_bold)

        self.assertEqual(node.__repr__(), expected)


    def test_repr_with_url(self):
        expected = "TextNode(This is a text node, bold, https://kelbya.dev)"
        node = TextNode("This is a text node", text_type_bold, "https://kelbya.dev")

        self.assertEqual(node.__repr__(), expected)

if __name__ == "__main__":
    unittest.main()

