import unittest
from htmlnode import HTMLNode, LeafNode

props = {
    "href": "https://kelbya.dev",
    "target": "_blank"
}

class TestHTMLNode(unittest.TestCase):
    def test_init_a_tag(self):
        pNode = HTMLNode("p", "This is a test p tag")

        tag = "a"
        value = "This is a test link"
        children = [pNode]

        aNode = HTMLNode(tag, value, children, props) 
        
        self.assertEqual(aNode.tag, tag)
        self.assertEqual(aNode.value, value)
        self.assertEqual(aNode.children, children)
        self.assertEqual(aNode.props, props)

    def test_init_p_tag(self):
        tag = "p"
        value = "This is a test link"

        pNode = HTMLNode(tag, value)

        self.assertEqual(pNode.tag, tag)
        self.assertEqual(pNode.value, value)

    def test_props_to_html_valid(self):
        pNode = HTMLNode("p", "This is a test p tag")
        tag = "a"
        value = "This is a test link"
        children = [pNode]
        aNode = HTMLNode(tag, value, children, props) 

        expected = f' href="{props["href"]}" target="{props["target"]}"'
        recieved = aNode.props_to_html()

        self.assertEqual(expected, recieved)

    def test_props_to_html_invalid(self):
        pNode = HTMLNode("a", "This is a test p tag")
        tag = "p"
        value = "This is a test link"
        children = [pNode]
        aNode = HTMLNode(tag, value, children, props) 

        expected = f' href:"{props["href"]}" target:"{props["target"]}"'
        recieved = aNode.props_to_html()

        self.assertNotEqual(expected, recieved)
    
    def test_repr_all_fields_valid(self):
        pNode = HTMLNode("p", "This is a test p tag")
        tag = "p"
        value = "This is a test link"
        children = [pNode]
        aNode = HTMLNode(tag, value, children, props) 

        expected = f"HTMLNode({tag}, {value}, {children}, {props})" 
        recieved = aNode.__repr__()
        self.assertEqual(expected, recieved)
        
    def test_repr_some_fields_none(self):
        tag = "p"
        value = "This is a test link"
        pNode = HTMLNode(tag, value)

        expected = f"HTMLNode({tag}, {value}, None, None)" 
        recieved = pNode.__repr__()
        self.assertEqual(expected, recieved)

class TestLeafNode(unittest.TestCase):
    def test_init_a_tag(self):
        tag = "a"
        value = "This is a test a value"

        aNode = LeafNode(tag, value, props)

        self.assertEqual(aNode.tag, tag)
        self.assertEqual(aNode.value, value)
        self.assertEqual(aNode.children, None)
        self.assertEqual(aNode.props, props)

    def test_init_p_tag(self):
        tag = "p"
        value = "This is a test p value"

        aNode = LeafNode(tag, value, None)

        self.assertEqual(aNode.tag, tag)
        self.assertEqual(aNode.value, value)
        self.assertEqual(aNode.children, None)
        self.assertEqual(aNode.props, None)

    def test_to_html_valid(self):
        tag = "a"
        value = "This is a test p value"
        aNode = LeafNode(tag, value, None)

        expected = f'<{tag}{aNode.props_to_html()}>{value}</{tag}>'
        result = aNode.to_html()
        
        self.assertEqual(expected, result)

    def test_to_html_invalid_value(self):
        aNode = LeafNode("a", None, None)

        with self.assertRaises(ValueError) as err:
            aNode.to_html()

        self.assertEqual(type(err.exception), ValueError)

    def test_to_html_empty_tag(self):
        aNode = LeafNode(None, "This is a test value", None)
        
        self.assertEqual(aNode.to_html(), "This is a test value")

    def test_repr_valid_fields(self):
        tag = "a"
        value = "This is a test value"
        aNode = LeafNode(tag, value, props)

        expected = f"LeafNode({tag}, {value}, {props})"
        result = aNode.__repr__()

        self.assertEqual(expected, result)
        
    def test_repr_some_fields_none(self):
        invalidNode = LeafNode(None, None, props)

        expected = f"LeafNode(None, None, {props})"
        result = invalidNode.__repr__()

        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
