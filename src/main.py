from textnode import TextNode, TextType
import os
import shutil
from generate import generate_pages_recursive
def main():
    destination = "public"
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)    
    copy_content("static", destination)
    generate_pages_recursive('content', 'template.html', destination)


def copy_content(source, destination):
    if not os.path.exists(source):
       return 
    static_content = os.listdir(source)
    for name in static_content:
        source_path = os.path.join(source, name)
        destination_path = os.path.join(destination, name)
        if os.path.isfile(source_path):
            print(f"copying from: {source_path} to {destination}")
            shutil.copy(source_path, destination)
        else:
            print(f"creating folder: {destination}")
            os.mkdir(destination_path)
            copy_content(source_path,destination_path)
    
    

if __name__ == "__main__":
    main()