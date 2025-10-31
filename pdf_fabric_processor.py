#!/usr/bin/env python3
"""
PDF Fabric Processor - Iteratively extract and process PDF content with fabric patterns
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import List, Optional

try:
    import pypdf
except ImportError:
    print("Error: pypdf is required. Install with: pip install pypdf", file=sys.stderr)
    sys.exit(1)


def extract_pdf_text(pdf_path: Path) -> List[str]:
    """Extract text from PDF, returning a list of pages."""
    try:
        reader = pypdf.PdfReader(pdf_path)
        pages = []
        for page_num, page in enumerate(reader.pages, 1):
            text = page.extract_text()
            if text.strip():
                pages.append(text)
        return pages
    except Exception as e:
        print(f"Error reading PDF: {e}", file=sys.stderr)
        sys.exit(1)


def run_fabric_pattern(text: str, pattern: str) -> str:
    """Run a fabric pattern on the given text."""
    try:
        result = subprocess.run(
            ["fabric", "--pattern", pattern],
            input=text,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running fabric pattern '{pattern}': {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'fabric' command not found. Make sure fabric is installed.", file=sys.stderr)
        sys.exit(1)


def process_pdf_with_fabric(
    pdf_path: Path,
    pattern: str,
    chunk_size: int = 1,
    verbose: bool = False
) -> str:
    """
    Process a PDF with a fabric pattern iteratively.
    
    Args:
        pdf_path: Path to PDF file
        pattern: Fabric pattern name to apply
        chunk_size: Number of pages to process at once
        verbose: Print progress information
    
    Returns:
        Final aggregated output
    """
    if verbose:
        print(f"Extracting text from {pdf_path}...", file=sys.stderr)
    
    pages = extract_pdf_text(pdf_path)
    
    if not pages:
        print("Error: No text extracted from PDF", file=sys.stderr)
        sys.exit(1)
    
    if verbose:
        print(f"Extracted {len(pages)} pages", file=sys.stderr)
    
    # Process pages in chunks
    chunk_results = []
    total_chunks = (len(pages) + chunk_size - 1) // chunk_size
    
    for i in range(0, len(pages), chunk_size):
        chunk = pages[i:i + chunk_size]
        chunk_num = (i // chunk_size) + 1
        
        if verbose:
            print(f"Processing chunk {chunk_num}/{total_chunks} (pages {i+1}-{i+len(chunk)})...", file=sys.stderr)
        
        # Combine pages in chunk
        combined_text = "\n\n".join(chunk)
        
        # Run fabric pattern on chunk
        result = run_fabric_pattern(combined_text, pattern)
        chunk_results.append(result)
    
    if verbose:
        print(f"Aggregating {len(chunk_results)} results...", file=sys.stderr)
    
    # Aggregate all chunk results
    aggregated_text = "\n\n---\n\n".join(chunk_results)
    final_result = run_fabric_pattern(aggregated_text, pattern)
    
    return final_result


def main():
    parser = argparse.ArgumentParser(
        description="Process PDF with fabric patterns iteratively",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s document.pdf -p summarize
  %(prog)s report.pdf -p extract_wisdom -c 5 -v
  %(prog)s paper.pdf -p analyze_claims --chunk-size 3 -o output.txt
        """
    )
    
    parser.add_argument(
        "pdf_path",
        type=Path,
        help="Path to PDF file"
    )
    
    parser.add_argument(
        "-p", "--pattern",
        required=True,
        help="Fabric pattern to apply"
    )
    
    parser.add_argument(
        "-c", "--chunk-size",
        type=int,
        default=1,
        help="Number of pages to process together (default: 1)"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output file (default: stdout)"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print progress information"
    )
    
    args = parser.parse_args()
    
    if not args.pdf_path.exists():
        print(f"Error: File not found: {args.pdf_path}", file=sys.stderr)
        sys.exit(1)
    
    if not args.pdf_path.suffix.lower() == '.pdf':
        print(f"Error: File is not a PDF: {args.pdf_path}", file=sys.stderr)
        sys.exit(1)
    
    # Process the PDF
    result = process_pdf_with_fabric(
        args.pdf_path,
        args.pattern,
        args.chunk_size,
        args.verbose
    )
    
    # Output result
    if args.output:
        args.output.write_text(result)
        if args.verbose:
            print(f"Output written to {args.output}", file=sys.stderr)
    else:
        print(result)


if __name__ == "__main__":
    main()
