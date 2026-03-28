#!/usr/bin/env python3
"""
README TOC Generator

Parses a markdown file and displays a generated Table of Contents based on its headers.
"""
import argparse
import re
import sys
import os

def create_slug(title: str) -> str:
    """Generate a GitHub-compatible markdown slug from a heading title."""
    slug = title.lower()
    # Remove characters that aren't alphanumeric, space, or hyphen
    slug = re.sub(r'[^\w\s-]', '', slug)
    # Replace spaces with hyphens
    slug = re.sub(r'\s+', '-', slug)
    return slug

def generate_toc_from_lines(lines, max_level=3):
    """Generates the Markdown TOC list from a list of strings."""
    toc = []
    # Match standard ATX headings (e.g. "## Heading")
    heading_pattern = re.compile(r'^(#{1,6})\s+(.+?)\s*$')
    
    in_code_block = False
    
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
            
        if in_code_block:
            continue
            
        match = heading_pattern.match(line)
        if match:
            level = len(match.group(1))
            if level > max_level:
                continue
                
            title = match.group(2)
            slug = create_slug(title)
            
            # Use 2 spaces per indentation level. Shift level - 1 since H1 is top level.
            indent = "  " * (level - 1)
            toc.append(f"{indent}- [{title}](#{slug})")
            
    return toc

def main():
    parser = argparse.ArgumentParser(description="Generate a Table of Contents for Markdown files.")
    parser.add_argument("file", help="Path to the markdown file.")
    parser.add_argument("--max-level", type=int, default=3, help="Maximum heading level to include (default: 3).")
    
    args = parser.parse_args()
    
    if not os.path.isfile(args.file):
        print(f"Error: File '{args.file}' not found.", file=sys.stderr)
        sys.exit(1)
        
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        toc = generate_toc_from_lines(lines, max_level=args.max_level)
        
        if toc:
            print("## Table of Contents")
            print('\n'.join(toc))
        else:
            print("No headings found.")
            
    except Exception as e:
        print(f"Error generating TOC: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
