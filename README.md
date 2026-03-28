# README TOC Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A zero-dependency CLI tool built in Python to automatically generate a Table of Contents for Markdown files, adhering to standard GitHub slug formats.

## Features
- **Smart parsing**: Ignores markdown headings inside code blocks.
- **Customizable Depth**: Set a maximum heading level to include.
- **Zero Dependencies**: Pure Python using just the standard library.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gbvk312/readme-toc-generator.git
   ```
2. Navigate into the directory:
   ```bash
   cd readme-toc-generator
   ```
3. Make the tool executable:
   ```bash
   chmod +x generate_toc.py
   ```

## Usage
Simply point the script to your markdown file:
```bash
./generate_toc.py README.md
```

To limit the TOC to only H1 and H2 headings:
```bash
./generate_toc.py README.md --max-level 2
```

The script will output the TOC to `stdout`, which you can neatly copy and paste into your Markdown file.
