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
    """Replace image src attributes and CSS background-image URLs with base64 data URIs."""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace each image reference
        for img_path, data_uri in image_mappings.items():
            if data_uri:
                # Extract just the filename from the full path for pattern matching
                img_filename = os.path.basename(img_path)
                
                # Replace src="../images/filename" with src="data:..." (for files in subdirectories)
                relative_pattern = f'src="../images/{img_filename}"'
                content = content.replace(relative_pattern, f'src="{data_uri}"')
                
                # Replace src="images/filename" with src="data:..." (for files in root)
                direct_pattern = f'src="images/{img_filename}"'
                content = content.replace(direct_pattern, f'src="{data_uri}"')
                
                # Replace CSS background-image: url('../images/filename')
                css_relative_pattern = f"url('../images/{img_filename}')"
                content = content.replace(css_relative_pattern, f"url('{data_uri}')")
                
                # Replace CSS background-image: url('images/filename')
                css_direct_pattern = f"url('images/{img_filename}')"
                content = content.replace(css_direct_pattern, f"url('{data_uri}')")
                
                # Also handle double quotes in CSS
                css_relative_pattern_dq = f'url("../images/{img_filename}")'
                content = content.replace(css_relative_pattern_dq, f"url('{data_uri}')")
                
                css_direct_pattern_dq = f'url("images/{img_filename}")'
                content = content.replace(css_direct_pattern_dq, f"url('{data_uri}')")
                
                # Handle CSS without quotes
                css_relative_pattern_nq = f"url(../images/{img_filename})"
                content = content.replace(css_relative_pattern_nq, f"url('{data_uri}')")
                
                css_direct_pattern_nq = f"url(images/{img_filename})"
                content = content.replace(css_direct_pattern_nq, f"url('{data_uri}')")
                
                print(f"Replaced {img_filename} references in {html_file}")
        
        # Write back to file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Successfully updated {html_file}")
        
    except Exception as e:
        print(f"Error processing {html_file}: {e}")

def main():
    # Define the images to convert
    target_images = [
        'images/campaign1.jpg',
        'images/campaign2.jpg',
        'images/campaign3.jpg',
        'images/campaign4.jpg',
        'images/campaign5.jpg',
        'images/campaign6.jpg',
        'images/toyo-tires.png',
        'images/CARE.png',
        'images/ETEN.png',
        'images/toyo-tires-white.png',
        'images/CARE-white.png',
        'images/ETEN-white.png',
        'images/ic_warranty_plus.png',
        'images/profile-placeholder.png',
        'images/image-event-1.png',
        'images/image-event-2.jpg',
        'images/image-speaker.png',
        'images/image-look.webp',
        'images/image-pointing.webp',
        'images/image-promo1.jpg',
        'images/image-promo2.jpg'
    ]
    
    # HTML files to update
    html_files = [
        'design-1/campaign.html',
        'design-1/home-main.html',
        'design-1/games.html',
        'design-1/appointments-claim.html',
        'design-1/membership-tier.html',
        'design-1/rewards.html',
        'design-1/service-centre-finder.html',
        'design-1/support.html',
        'design-1/warranty-claim.html',
        'design-1/warranty-registration.html',
        'design-2/claims.html',
        'design-2/credit-balance.html',
        'design-2/home-main.html',
        'design-2/manage-appointments.html',
        'design-2/order-history.html',
        'design-2/order-tires.html',
        'design-2/sales-forecast.html'
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