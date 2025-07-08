#!/usr/bin/env python3
"""
Script to remove background-image: url('') properties from HTML files using regex.
This script will replace background-image declarations with empty strings.
"""

import re
import os
import shutil
from datetime import datetime

def remove_background_images(file_path, backup=True):
    """
    Remove background-image: url('...') properties from an HTML file.
    
    Args:
        file_path (str): Path to the HTML file to process
        backup (bool): Whether to create a backup of the original file
    
    Returns:
        tuple: (success: bool, message: str, changes_count: int)
    """
    
    if not os.path.exists(file_path):
        return False, f"File not found: {file_path}", 0
    
    try:
        # Create backup if requested
        if backup:
            backup_path = f"{file_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            shutil.copy2(file_path, backup_path)
            print(f"Backup created: {backup_path}")
        
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        original_content = content
        
        # Regex patterns to match background-image properties
        patterns = [
            # Match: background-image: url(''); or background-image: url("");
            r'background-image:\s*url\([\'"]?\s*[\'"]?\);?',
            
            # Match: background-image: url('data:...'); (for data URLs)
            r'background-image:\s*url\([\'"]?data:[^)]*[\'"]?\);?',
            
            # Match: background-image: url('path/to/image.ext'); (for file paths)
            r'background-image:\s*url\([\'"]?[^)]*\.(jpg|jpeg|png|gif|svg|webp)[\'"]?\);?',
            
            # Match any other background-image: url(...); pattern
            r'background-image:\s*url\([^)]*\);?'
        ]
        
        changes_count = 0
        
        # Apply each pattern
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                content = re.sub(pattern, '', content, flags=re.IGNORECASE)
                changes_count += len(matches)
        
        # Clean up any remaining empty style attributes or extra spaces
        # Remove empty style="" attributes
        content = re.sub(r'\s*style\s*=\s*[\'"][\'"]', '', content)
        
        # Clean up multiple spaces in style attributes
        content = re.sub(r'style\s*=\s*[\'"]([^\'\"]*)\s*;\s*([^\'\"]*)[\'"]', 
                        lambda m: f'style="{m.group(1).strip()}; {m.group(2).strip()}"' if m.group(2).strip() else f'style="{m.group(1).strip()}"', 
                        content)
        
        # Remove style attributes that only contain semicolons and spaces
        content = re.sub(r'\s*style\s*=\s*[\'"][;\s]*[\'"]', '', content)
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        if content != original_content:
            return True, f"Successfully processed {file_path}. Removed {changes_count} background-image properties.", changes_count
        else:
            return True, f"No background-image properties found in {file_path}.", 0
            
    except Exception as e:
        return False, f"Error processing {file_path}: {str(e)}", 0

def main():
    """Main function to process campaign.html file."""
    
    # Target file
    campaign_file = "design-1/campaign.html"
    
    print("Background Image Remover")
    print("=" * 40)
    print(f"Processing: {campaign_file}")
    
    # Process the file
    success, message, changes = remove_background_images(campaign_file, backup=True)
    
    if success:
        print(f"✅ {message}")
        if changes > 0:
            print(f"📝 Total changes made: {changes}")
    else:
        print(f"❌ {message}")
    
    print("\nDone!")

if __name__ == "__main__":
    main() 