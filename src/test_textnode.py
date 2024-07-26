import unittest

from textnode import *

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

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        node = TextNode("This is regular text", text_type_text)

        expected = LeafNode(None, node.text)
        recieved = text_node_to_html_node(node)
        
        self.assertEqual(expected.tag, recieved.tag)
        self.assertEqual(expected.value, recieved.value)
        self.assertEqual(expected.props, recieved.props)

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is bold text", text_type_bold)

        expected = LeafNode("b", node.text)
        recieved = text_node_to_html_node(node)

        self.assertEqual(expected.tag, recieved.tag)
        self.assertEqual(expected.value, recieved.value)
        self.assertEqual(expected.props, recieved.props)

    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is italic text", text_type_italic)

        expected = LeafNode("i", node.text)
        recieved = text_node_to_html_node(node)

        self.assertEqual(expected.tag, recieved.tag)
        self.assertEqual(expected.value, recieved.value)
        self.assertEqual(expected.props, recieved.props)

    def test_text_node_to_html_node_code(self):
        node = TextNode("This is code", text_type_code)

        expected = LeafNode("code", node.text)
        recieved = text_node_to_html_node(node)

        self.assertEqual(expected.tag, recieved.tag)
        self.assertEqual(expected.value, recieved.value)
        self.assertEqual(expected.props, recieved.props)

    def test_text_node_to_html_node_link(self):
        link = "https://kelbya.dev"
        node = TextNode("This is a link", text_type_link, link)

        expected = LeafNode("a", node.text, {"href": link})
        recieved = text_node_to_html_node(node)

        self.assertEqual(expected.tag, recieved.tag)
        self.assertEqual(expected.value, recieved.value)
        self.assertEqual(expected.props, recieved.props)

    def test_text_node_to_html_node_image(self):
        image_link = "https://image.com"
        node = TextNode("This is an image", text_type_image, image_link)

        expected = LeafNode("img", "", {"src": image_link, "alt": node.text})
        recieved = text_node_to_html_node(node)

        self.assertEqual(expected.tag, recieved.tag)
        self.assertEqual(expected.value, recieved.value)
        self.assertEqual(expected.props, recieved.props)

    def test_text_node_to_html_node_invalid(self):
        node = TextNode("This is an invalid text_node", "invalid")

        with self.assertRaises(ValueError) as err:
            text_node_to_html_node(node)

        self.assertEqual(type(err.exception), ValueError)

if __name__ == "__main__":
    unittest.main()
