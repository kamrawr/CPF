#!/usr/bin/env python3
"""
Extract form fields from CPF program PDFs
Creates CPF-specific form field database
"""

import os
import sys
sys.path.append('../analysis')

# Import the extraction functions from the main script
from pathlib import Path
import csv
import PyPDF2
import re
import hashlib
from collections import defaultdict

# Use the same extraction functions as before
exec(open('../analysis/extract_form_fields.py').read().replace('if __name__ == "__main__":', 'if False:'))
exec(open('../analysis/enhance_form_fields.py').read().replace('if __name__ == "__main__":', 'if False:'))

def main():
    pdf_dir = os.path.dirname(os.path.abspath(__file__))
    output_csv_raw = os.path.join(pdf_dir, 'cpf_form_fields_raw.csv')
    output_csv_enhanced = os.path.join(pdf_dir, 'cpf_form_fields_enhanced.csv')
    
    print("="*60)
    print("CPF Program - Form Field Extractor")
    print("="*60)
    
    # Extract fields from CPF PDFs
    all_fields = extract_all_forms(pdf_dir)
    
    # Deduplicate
    unique_fields = deduplicate_fields(all_fields)
    
    print(f"\nTotal fields extracted: {len(all_fields)}")
    print(f"Unique fields: {len(unique_fields)}")
    
    # Write raw CSV
    if unique_fields:
        with open(output_csv_raw, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['form_number', 'document', 'field_name', 'field_type', 'required', 'context']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(unique_fields)
        
        print(f"\n✓ Raw CSV created: {output_csv_raw}")
        
        # Enhance the CSV
        enhance_csv(output_csv_raw, output_csv_enhanced)
    else:
        print("\n⚠ No fields found to write to CSV")

if __name__ == "__main__":
    main()
