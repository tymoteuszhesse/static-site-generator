from extract_markdown import markdown_to_html_node
from extract_markdown import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as template_file:
        template_content = template_file.read()
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as destination:
        destination.write(template_content)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        return
    for content in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, content)
        destination_path = os.path.join(dest_dir_path, content)
        if os.path.isfile(source_path) and content.endswith(".md"):
            destination_path = destination_path.replace(".md", ".html",-1)
            with open(source_path) as f:
                markdown = f.read()
            with open(template_path) as template_file:
                template_content = template_file.read()   
            node = markdown_to_html_node(markdown)
            html = node.to_html()
            title = extract_title(markdown)
            template_content = template_content.replace("{{ Title }}", title)
            template_content = template_content.replace("{{ Content }}", html)
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            with open(destination_path, 'w') as destination:
                destination.write(template_content)
        elif not os.path.isfile(source_path):
            generate_pages_recursive(source_path, template_path, destination_path)                  
            