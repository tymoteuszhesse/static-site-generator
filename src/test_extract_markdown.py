import unittest
from extract_markdown import markdown_to_html_node, extract_title
from text_to_textnode import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(result, expected)
    def test_extract_markdown_images_with_single_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(result, expected)
 
    def test_extract_markdown_images_with_no_image(self):
        text = "This is text with no image"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)     

    def test_extract_markdown_images_with_invalid_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan] corrupted"
        result = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(result, expected)           

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expected)

    def test_extract_markdown_links_with_single_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        result = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(result, expected)
 
    def test_extract_markdown_links_with_no_link(self):
        text = "This is text with no link"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)     

    def test_extract_markdown_links_with_invalid_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube]("
        result = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev")]
        self.assertEqual(result, expected) 
        
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_extract_title(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts

- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)

## Reasons I like Tolkien

- You can spend years studying the legendarium and still not understand its depths
- It can be enjoyed by children and adults alike
- Disney _didn't ruin it_ (okay, but Amazon might have)
- It created an entirely new genre of fantasy

## My favorite characters (in order)        
        """
        result = extract_title(md)
        self.assertEqual(result, "Tolkien Fan Club")
        

if __name__ == "__main__":
    unittest.main()