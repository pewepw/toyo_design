#!/usr/bin/env python3
"""
Convert image files to base64 data URIs in HTML files.
This ensures images are embedded directly in the HTML for better compatibility with html.to.design plugin.
"""

import os
import base64
import re
from typing import Dict

def get_mime_type(filename: str) -> str:
    """Get MIME type based on file extension."""
    ext = filename.lower().split('.')[-1]
    mime_types = {
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'gif': 'image/gif',
        'svg': 'image/svg+xml',
        'webp': 'image/webp'
    }
    return mime_types.get(ext, 'image/png')

def image_to_base64(image_path: str) -> str:
    """Convert image file to base64 data URI."""
    try:
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
            b64_data = base64.b64encode(img_data).decode('utf-8')
            mime_type = get_mime_type(image_path)
            return f"data:{mime_type};base64,{b64_data}"
    except Exception as e:
        print(f"Error converting {image_path}: {e}")
        return None

def replace_images_in_html(html_file: str, image_mappings: Dict[str, str]) -> None:
    """Replace image src attributes with base64 data URIs."""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace each image reference
        for img_filename, data_uri in image_mappings.items():
            if data_uri:
                # Replace src="filename" with src="data:..."
                pattern = f'src="{img_filename}"'
                replacement = f'src="{data_uri}"'
                content = content.replace(pattern, replacement)
                print(f"Replaced {img_filename} in {html_file}")
        
        # Write back to file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Successfully updated {html_file}")
        
    except Exception as e:
        print(f"Error processing {html_file}: {e}")

def main():
    # Define the images to convert
    target_images = [
        'screenshots/campaign1.jpg',
        'screenshots/campaign2.jpg',
        'screenshots/campaign3.jpg',
        'screenshots/campaign4.jpg',
        'screenshots/campaign5.jpg',
        'screenshots/campaign6.jpg',
        'toyo-tires.png',
        'CARE.png',
        'ic_warranty_plus.png',
        'profile-placeholder.png',
        'screenshots/image-event-1.png',
        'screenshots/image-event-2.jpg',
        'screenshots/image-speaker.png'
    ]
    
    # HTML files to update
    html_files = [
        'campaign.html',
        'home-main.html',
        'games.html'
    ]
    
    print("Converting images to base64 data URIs...")
    
    # Convert images to base64
    image_mappings = {}
    for img_file in target_images:
        if os.path.exists(img_file):
            print(f"Converting {img_file}...")
            data_uri = image_to_base64(img_file)
            if data_uri:
                image_mappings[img_file] = data_uri
                print(f"✓ {img_file} converted successfully")
            else:
                print(f"✗ Failed to convert {img_file}")
        else:
            print(f"✗ {img_file} not found")
    
    # Update HTML files
    print("\nUpdating HTML files...")
    for html_file in html_files:
        if os.path.exists(html_file):
            replace_images_in_html(html_file, image_mappings)
        else:
            print(f"✗ {html_file} not found")
    
    print("\nDone! Your HTML files now have embedded images.")
    print("This should work better with the html.to.design plugin.")

if __name__ == "__main__":
    main()