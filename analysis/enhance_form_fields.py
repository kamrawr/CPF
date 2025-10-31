#!/usr/bin/env python3
"""
Enhance form fields CSV for dynamic form and reporting application
Adds: form_id, field_id, data_type, validation_rules, field_category
"""

import csv
import re
import hashlib
from collections import defaultdict

def normalize_field_name(field_name):
    """Create a normalized field name for matching across forms"""
    # Remove numbers, punctuation, convert to lowercase
    normalized = re.sub(r'^\d+\.\s*', '', field_name)  # Remove leading numbers
    normalized = re.sub(r'[★⭐☐]', '', normalized)  # Remove special chars
    normalized = normalized.lower().strip()
    
    # Standardize common variations
    replacements = {
        'customer name and signature': 'customer_signature',
        'contractor name and signature': 'contractor_signature',
        'customer signature': 'customer_signature',
        'contractor signature': 'contractor_signature',
        'full name': 'full_name',
        'email': 'email_address',
        'site address': 'site_address',
        'mailing address': 'mailing_address',
        'telephone': 'phone_number',
        'install date': 'installation_date',
        'date': 'date',
        'manufacturer': 'manufacturer',
        'model': 'model_number',
        'serial #': 'serial_number',
        'occb#': 'license_number',
    }
    
    for key, value in replacements.items():
        if key in normalized:
            return value
    
    # Create snake_case identifier
    normalized = re.sub(r'[^\w\s]', '', normalized)
    normalized = re.sub(r'\s+', '_', normalized)
    
    return normalized[:50]  # Limit length

def categorize_field(field_name, context):
    """Categorize field into logical groups"""
    name_lower = field_name.lower()
    context_lower = context.lower()
    
    # Customer Information - check signatures first
    if any(x in name_lower for x in ['customer signature', 'customer name and signature', 'firma del cliente']):
        return 'customer_authorization'
    
    # Contractor signatures
    if any(x in name_lower for x in ['contractor signature', 'contractor name and signature', 'firma del contratista']):
        return 'contractor_authorization'
    
    # Customer Information (non-signature)
    if any(x in name_lower for x in ['customer', 'homeowner', 'renter', 'cliente', 'propietario']):
        if 'type' in name_lower or 'tipo' in name_lower:
            return 'customer_information'
        return 'customer_information'
    
    # Contractor Information (non-signature)
    if any(x in name_lower for x in ['contractor', 'company', 'occb', 'license', 'contratista', 'empresa']):
        return 'contractor_information'
    
    # Site/Property Information
    if any(x in name_lower for x in ['site address', 'mailing address', 'dirección', 'city', 'state', 'zip',
                                      'ciudad', 'estado', 'year built', 'año', 'square feet', 'pies cuadrados',
                                      'foundation', 'basement', 'cimientos', 'sótano', 'stories', 'pisos']):
        return 'site_information'
    
    # Equipment/Upgrade Types
    if any(x in name_lower for x in ['heat pump', 'bomba de calor', 'furnace', 'horno', 'thermostat', 'termostato',
                                      'water heater', 'calentador de agua', 'insulation', 'aislamiento', 
                                      'windows', 'ventanas', 'fireplace', 'chiminea', 'air conditioner',
                                      'aire acondicionado', 'weatherization', 'impermeabilización']):
        return 'equipment_information'
    
    # Technical Specifications
    if any(x in name_lower for x in ['hspf', 'afue', 'seer', 'eer', 'btu', 'capacity', 'capacidad',
                                      'model', 'modelo', 'manufacturer', 'fabricante', 'serial']):
        return 'technical_specifications'
    
    # Financial/Incentive
    if any(x in name_lower for x in ['incentive', 'incentivo', 'cost', 'costo', 'price', 'precio', 
                                      'payment', 'pago', 'invoice', 'factura', 'funding', 'financiación',
                                      'instant', 'discount', 'descuento', 'income', 'ingreso']):
        return 'financial_information'
    
    # Program/Process Steps
    if name_lower.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
        if any(x in name_lower for x in ['review', 'complete', 'sign', 'submit']):
            return 'process_instructions'
        # Otherwise it's likely an equipment/upgrade recommendation
        return 'equipment_information'
    
    # Terms and Conditions
    if any(x in name_lower for x in ['terms', 'conditions', 'eligibility', 'elegibilidad',
                                      'authorization', 'autorización', 'disclaimer', 'exoneración',
                                      'liability', 'responsabilidad', 'property rights', 'derechos']):
        return 'terms_and_conditions'
    
    # Demographics (Optional)
    if any(x in name_lower for x in ['demographic', 'demográfico', 'gender', 'género', 'race', 'raza',
                                      'language', 'idioma', 'residents', 'residentes', 'household']):
        return 'demographic_information'
    
    # Utility/Energy Provider Info
    if any(x in name_lower for x in ['electric provider', 'gas provider', 'proveedor', 'utility', 'servicio']):
        return 'utility_information'
    
    return 'other'

def infer_data_type(field_name, field_type, context):
    """Infer the data type for the field"""
    name_lower = field_name.lower()
    
    if field_type == 'Signature':
        return 'signature'
    
    if field_type == 'Checkbox':
        return 'boolean'
    
    # Email
    if 'email' in name_lower or 'e-mail' in name_lower:
        return 'email'
    
    # Phone
    if any(x in name_lower for x in ['phone', 'telephone', 'tel', 'fax']):
        return 'phone'
    
    # Date
    if any(x in name_lower for x in ['date', 'year built', 'install date']):
        return 'date'
    
    # Currency/Money
    if any(x in name_lower for x in ['cost', 'price', 'incentive', 'payment', 'income', 'funding']):
        if '$' in context:
            return 'currency'
    
    # Numeric measurements
    if any(x in name_lower for x in ['hspf', 'afue', 'seer', 'eer', 'btu', 'capacity', 'qty', 
                                      'quantity', 'square feet', 'sq ft', 'temperature']):
        return 'number'
    
    # Percentage
    if '%' in name_lower or 'percent' in name_lower or 'fe' in name_lower:
        return 'percentage'
    
    # Address
    if 'address' in name_lower:
        return 'address'
    
    # Zip code
    if 'zip' in name_lower:
        return 'zipcode'
    
    # State
    if name_lower == 'state' or 'estado' in name_lower:
        return 'state'
    
    # Model/Serial numbers
    if any(x in name_lower for x in ['model', 'serial', 'license', 'occb', 'certificate']):
        return 'text'
    
    # Default to text
    return 'text'

def extract_validation_rules(field_name, data_type, required, context):
    """Extract validation rules based on field characteristics"""
    rules = []
    
    if required == 'True':
        rules.append('required')
    
    if data_type == 'email':
        rules.append('email_format')
    
    if data_type == 'phone':
        rules.append('phone_format')
    
    if data_type == 'zipcode':
        rules.append('zipcode_format')
    
    if data_type == 'date':
        rules.append('valid_date')
    
    if data_type == 'currency':
        rules.append('positive_number')
    
    if data_type == 'signature':
        rules.append('signature_required')
    
    # Extract ranges from context
    if 'hspf' in field_name.lower():
        rules.append('range:7.0-10.0')
    
    if 'afue' in field_name.lower():
        rules.append('range:70-100')
    
    if 'seer' in field_name.lower():
        rules.append('range:13-25')
    
    return '|'.join(rules) if rules else None

def create_form_id(form_number):
    """Create standardized form ID"""
    # Normalize form numbers
    form_map = {
        '300CPF': 'CPF-300-HOME-ASSESSMENT',
        '300HPQ': 'CPF-300-HEAT-PUMP-QUESTIONNAIRE',
        '320C-HVAC': 'CPF-320-HVAC-INCENTIVE',
        '320C-WH': 'CPF-320-WATER-HEATING-INCENTIVE',
        '320C-WX': 'CPF-320-WEATHERIZATION-INCENTIVE',
        '320ECHP': 'CPF-320-EXTENDED-CAPACITY-HP',
        '350CC': 'CPF-350-CUSTOMER-CONSENT',
        '320CPF': 'CPF-320-PROJECT-DETAILS',
        '371CPF': 'CPF-371-ENERGY-TRUST',
        '320I': 'CPF-320-PROGRAM-INFO',
    }
    
    # Handle Spanish versions
    if form_number in form_map:
        return form_map[form_number]
    elif form_number.endswith('-ES'):
        base_form = form_number.replace('-ES', '')
        if base_form in form_map:
            return form_map[base_form] + '-ES'
    
    return f'CPF-{form_number}'

def create_field_id(normalized_name, form_id, category):
    """Create unique field ID based on semantic meaning"""
    # Create a short hash for uniqueness
    hash_obj = hashlib.md5(f"{normalized_name}_{category}".encode())
    short_hash = hash_obj.hexdigest()[:6]
    
    # Combine category prefix with normalized name
    category_prefixes = {
        'customer_information': 'CUST',
        'customer_authorization': 'AUTH_CUST',
        'contractor_information': 'CNTR',
        'contractor_authorization': 'AUTH_CNTR',
        'site_information': 'SITE',
        'equipment_information': 'EQUIP',
        'technical_specifications': 'SPEC',
        'financial_information': 'FIN',
        'terms_and_conditions': 'TERMS',
        'demographic_information': 'DEMO',
        'utility_information': 'UTIL',
        'process_instructions': 'PROC',
        'other': 'MISC'
    }
    
    prefix = category_prefixes.get(category, 'MISC')
    return f"{prefix}_{short_hash}_{normalized_name[:20]}"

def enhance_csv(input_file, output_file):
    """Main function to enhance the CSV"""
    
    print("Reading and enhancing form fields...")
    
    enhanced_rows = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            form_number = row['form_number']
            field_name = row['field_name']
            field_type = row['field_type']
            required = row['required']
            context = row['context']
            document = row['document']
            
            # Create enhanced fields
            form_id = create_form_id(form_number)
            normalized_name = normalize_field_name(field_name)
            category = categorize_field(field_name, context)
            data_type = infer_data_type(field_name, field_type, context)
            validation_rules = extract_validation_rules(field_name, data_type, required, context)
            field_id = create_field_id(normalized_name, form_id, category)
            
            # Determine language - check both document name and field content
            is_spanish = (any(x in document.lower() for x in ['-es', 'espanol', 'spanish', '_es.pdf']) or
                         any(x in field_name.lower() for x in ['cliente', 'contratista', 'bomba de calor', 
                                                                 'calentador', 'aislamiento', 'ventanas',
                                                                 'firma', 'dirección', 'nombre', 'fecha',
                                                                 'costo', 'instalado', 'incentivo', 'año',
                                                                 'empresa', 'elegibilidad', 'autorización',
                                                                 'proveedor', 'sótano', 'pies cuadrados',
                                                                 'termostato', 'calefacción', 'vivienda']))
            language = 'es' if is_spanish else 'en'
            
            enhanced_row = {
                'field_id': field_id,
                'form_id': form_id,
                'form_number': form_number,
                'field_category': category,
                'field_name': field_name,
                'normalized_name': normalized_name,
                'data_type': data_type,
                'field_type': field_type,
                'required': required,
                'validation_rules': validation_rules or '',
                'language': language,
                'context': context,
                'document_source': document
            }
            
            enhanced_rows.append(enhanced_row)
    
    # Write enhanced CSV
    fieldnames = [
        'field_id',
        'form_id', 
        'form_number',
        'field_category',
        'field_name',
        'normalized_name',
        'data_type',
        'field_type',
        'required',
        'validation_rules',
        'language',
        'context',
        'document_source'
    ]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(enhanced_rows)
    
    print(f"✓ Enhanced CSV created: {output_file}")
    print(f"  Total fields: {len(enhanced_rows)}")
    
    # Print statistics
    categories = defaultdict(int)
    data_types = defaultdict(int)
    forms = defaultdict(int)
    
    for row in enhanced_rows:
        categories[row['field_category']] += 1
        data_types[row['data_type']] += 1
        forms[row['form_id']] += 1
    
    print("\nCategories:")
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count}")
    
    print("\nData Types:")
    for dtype, count in sorted(data_types.items(), key=lambda x: x[1], reverse=True):
        print(f"  {dtype}: {count}")
    
    print(f"\nUnique Forms: {len(forms)}")

if __name__ == "__main__":
    import sys
    import os
    # Allow specifying directory as argument
    if len(sys.argv) > 1:
        work_dir = sys.argv[1]
    else:
        work_dir = os.getcwd()
    
    input_csv = os.path.join(work_dir, 'form_fields_comprehensive.csv')
    output_csv = os.path.join(work_dir, 'form_fields_enhanced.csv')
    
    enhance_csv(input_csv, output_csv)
