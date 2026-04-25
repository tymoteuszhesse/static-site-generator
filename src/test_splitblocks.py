import unittest
from splitblocks import markdown_to_blocks, block_to_block_type, BlockType
class TestSplitBlocks(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
        
    def test_split_blocks_with_one_line(self):
        markdown = "# This is a heading"

        expected_result = ["# This is a heading"]
        
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected_result)
        
    def test_split_blocks_with_empty_string(self):
        markdown = ""

        expected_result = []
        
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected_result)
        
    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        expected_result = BlockType.HEADING
        
        result = block_to_block_type(block)
        self.assertEqual(result, expected_result)
        
    def test_block_to_block_type_code(self):
        block = """``` This is a code ```"""
        expected_result = BlockType.CODE
        
        result = block_to_block_type(block)
        self.assertEqual(result, expected_result)
        
    def test_block_to_block_type_quote(self):
        block = ">This is a quote"
        expected_result = BlockType.QUOTE
        
        result = block_to_block_type(block)
        self.assertEqual(result, expected_result)     
        
    def test_block_to_block_type_unordered_list(self):
        block = """
- This is a list
- This is a list
"""
        expected_result = BlockType.UNORDERED_LIST
        
        result = block_to_block_type(block)
        self.assertEqual(result, expected_result)        
        
    def test_block_to_block_type_ordered_list(self):
        block = """
1. This is a list
2. This is a list
"""
        expected_result = BlockType.ORDERED_LIST
        
        result = block_to_block_type(block)
        self.assertEqual(result, expected_result)                      
        
    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph"
        expected_result = BlockType.PARAGRAPH
        
        result = block_to_block_type(block)
        self.assertEqual(result, expected_result)