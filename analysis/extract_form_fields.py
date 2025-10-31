#!/usr/bin/env python3
"""
Extract form fields from Energy Trust of Oregon PDFs
Creates a comprehensive CSV with field names, document references, and context
"""

import os
import re
import csv
from pathlib import Path
import PyPDF2

def extract_form_number(filename):
    """Extract form number from filename (e.g., '350CC' from '043_Customer Consent Form–Form 350CC (PDF).pdf')"""
    match = re.search(r'Form\s+(\d+[A-Z-]+)', filename, re.IGNORECASE)
    if match:
        return match.group(1)
    
    # Try alternative pattern
    match = re.search(r'(\d{3}[A-Z-]+)', filename)
    if match:
        return match.group(1)
    
    return "Unknown"

def clean_field_name(text):
    """Clean and normalize field names"""
    if not text:
        return ""
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text.strip())
    
    # Remove special characters but keep meaningful ones
    text = re.sub(r'[★⭐]', '', text)
    
    return text

def extract_fields_from_text(text, form_number, filename):
    """Extract form fields from PDF text content"""
    fields = []
    
    # Patterns to identify form fields
    patterns = [
        # Fields marked with asterisk (required fields)
        r'[★⭐]\s*([A-Z][A-Za-z\s/]+(?:name|address|signature|date|email|telephone|city|state|zip|model|manufacturer|OCCB|license|cost|qty|HSPF|AFUE|FE|serial|install|company))',
        
        # Checkbox fields
        r'☐\s*([A-Z][A-Za-z\s,/\-()]+)(?:\s*\.{2,}|\s*\$)',
        
        # Fields with colons
        r'^([A-Z][A-Za-z\s/]+):\s*(?:_+|\s*$)',
        
        # Required field indicators
        r'Indicates required field',
    ]
    
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip headers and footers
        if any(skip in line.lower() for skip in ['page', 'form 3', 'energy trust', 'return completed', 'upgrade types']):
            continue
        
        # Look for signature fields
        if 'signature' in line.lower() and len(line) < 100:
            context = ' '.join(lines[max(0, i-2):min(len(lines), i+3)])
            fields.append({
                'field_type': 'Signature',
                'field_name': clean_field_name(line),
                'required': '★' in line or 'required' in line.lower(),
                'context': clean_field_name(context[:200])
            })
        
        # Look for text input fields (with underscores or colons)
        if ('___' in line or ': ' in line) and len(line) < 100:
            # Extract field label
            label = re.sub(r'[_:]+.*$', '', line).strip()
            if label and len(label) > 2:
                fields.append({
                    'field_type': 'Text Input',
                    'field_name': clean_field_name(label),
                    'required': '★' in line or '⭐' in line,
                    'context': clean_field_name(line[:200])
                })
        
        # Look for checkbox/radio options
        checkbox_match = re.search(r'☐\s*([A-Z][A-Za-z\s,/\-()]+?)(?:\s*☐|\s*$)', line)
        if checkbox_match:
            fields.append({
                'field_type': 'Checkbox',
                'field_name': clean_field_name(checkbox_match.group(1)),
                'required': False,
                'context': clean_field_name(line[:200])
            })
    
    # Add document reference and filename to each field
    for field in fields:
        field['form_number'] = form_number
        field['document'] = filename
    
    return fields

def extract_all_forms(pdf_dir):
    """Process all PDFs in the directory"""
    all_fields = []
    pdf_files = list(Path(pdf_dir).glob('*.pdf'))
    
    print(f"Found {len(pdf_files)} PDF files to process...")
    
    for pdf_path in sorted(pdf_files):
        print(f"Processing: {pdf_path.name}")
        
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                # Extract text from all pages
                full_text = ""
                for page in pdf_reader.pages:
                    full_text += page.extract_text() + "\n"
                
                # Get form number
                form_number = extract_form_number(pdf_path.name)
                
                # Extract fields
                fields = extract_fields_from_text(full_text, form_number, pdf_path.name)
                all_fields.extend(fields)
                
                print(f"  Found {len(fields)} fields in {pdf_path.name}")
                
        except Exception as e:
            print(f"  Error processing {pdf_path.name}: {e}")
    
    return all_fields

def deduplicate_fields(fields):
    """Remove duplicate fields while preserving context"""
    seen = {}
    unique_fields = []
    
    for field in fields:
        key = (field['form_number'], field['field_name'], field['field_type'])
        
        if key not in seen:
            seen[key] = True
            unique_fields.append(field)
    
    return unique_fields

def main(pdf_dir=None):
    if pdf_dir is None:
        pdf_dir = os.getcwd()
    output_csv = os.path.join(pdf_dir, 'form_fields_comprehensive.csv')
    
    print("="*60)
    print("Energy Trust of Oregon - Form Field Extractor")
    print("="*60)
    
    # Extract fields from all PDFs
    all_fields = extract_all_forms(pdf_dir)
    
    # Deduplicate
    unique_fields = deduplicate_fields(all_fields)
    
    print(f"\nTotal fields extracted: {len(all_fields)}")
    print(f"Unique fields: {len(unique_fields)}")
    
    # Write to CSV
    if unique_fields:
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['form_number', 'document', 'field_name', 'field_type', 'required', 'context']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for field in sorted(unique_fields, key=lambda x: (x['form_number'], x['field_name'])):
                writer.writerow(field)
        
        print(f"\n✓ CSV created successfully: {output_csv}")
        print(f"  Total rows: {len(unique_fields)}")
    else:
        print("\n⚠ No fields found to write to CSV")

if __name__ == "__main__":
    import sys
    # Allow specifying directory as argument
    if len(sys.argv) > 1:
        pdf_dir = sys.argv[1]
    else:
        pdf_dir = os.getcwd()
    
    main(pdf_dir)
