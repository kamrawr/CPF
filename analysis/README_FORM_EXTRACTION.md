# Energy Trust of Oregon - Form Field Extraction

## Overview
This document describes the automated extraction of form fields from Energy Trust of Oregon Community Partner Fund (CPF) program PDFs.

## Output File
**Location:** `/Users/isaiah/CPF/pdf_downloads/form_fields_comprehensive.csv`

## Extraction Results

### Summary Statistics
- **Total PDFs Processed:** 86 documents
- **Total Fields Extracted:** 543 unique form fields
- **Unique Forms Identified:** 19 different form types

### CSV Structure
The output CSV contains the following columns:

| Column | Description |
|--------|-------------|
| `form_number` | Form identifier (e.g., 350CC, 320C-HVAC) |
| `document` | Source PDF filename |
| `field_name` | Name/label of the form field |
| `field_type` | Type of field (Text Input, Signature, Checkbox, etc.) |
| `required` | Whether the field is required (True/False) |
| `context` | Surrounding text providing additional context |

### Forms Identified

| Form Number | Fields | Documents | Description |
|-------------|--------|-----------|-------------|
| 300CPF | 92 | 2 | Customer Authorization Form and Home Energy Assessment |
| 320C-HVAC | 41 | 1 | Heating and Cooling Incentives, Contractor Install |
| 320C-WH | 23 | 1 | Water Heating, Contractor Installed |
| 320C-WX | 27 | 1 | Weatherization, Contractor Installed |
| 320ECHP | 29 | 1 | Extended Capacity Heat Pump |
| 350CC | 17 | 1 | Customer Consent and Authorization Form |
| 320C-HVAC-ES | 27 | 1 | Spanish version of HVAC form |
| 320C-WH-ES | 18 | 1 | Spanish version of Water Heating form |
| 320C-WX-ES | 18 | 1 | Spanish version of Weatherization form |
| 350CC-ES | 15 | 1 | Spanish version of Consent form |
| 371CPF | 16 | 1 | Energy Trust form |
| 320CPF | 54 | 3 | CPF Project Details Form |
| 300HPQ | 5 | 1 | Heat Pump Questionnaire |
| 371CPF-A | 3 | 1 | Energy Trust form variant |
| 320I | 1 | 1 | Program Information |
| 320I-HP | 1 | 1 | Heat Pump Program Information |
| 523-C | 1 | 1 | Additional form |
| Unknown | 151 | 22 | Various supporting documents and guides |

## Field Types Extracted

1. **Text Input Fields** - Customer/contractor data entry fields
2. **Signature Fields** - Authorization signatures
3. **Checkbox Fields** - Multiple choice selections
4. **Date Fields** - Installation dates, signature dates
5. **Numeric Fields** - Equipment specifications, costs, quantities

## Key Forms Detail

### Form 350CC - Customer Consent and Authorization
- **Purpose:** Customer and contractor signatures for authorization
- **Key Fields:**
  - Customer Name and Signature
  - Customer email address
  - Site Address
  - Mailing Address
  - Contractor Name and Signature
  - Contractor company
  - OCCB# or Washington License #
  - Install date
  - Instant incentive project indicator

### Form 320C-HVAC - Heating and Cooling Incentives
- **Purpose:** Contractor-installed HVAC equipment incentive application
- **Key Sections:**
  - Customer Information
  - Site Information
  - Equipment Information (Ductless Heat Pump, Ducted Heat Pump, etc.)
  - Contractor Information
  - Instant Incentives
  - Optional demographic information

### Form 320C-WH - Water Heating Incentives
- **Purpose:** Water heating equipment incentive applications
- **Equipment Types:**
  - Heat Pump Water Heaters
  - Gas Tankless Water Heaters
  - Related equipment

### Form 320C-WX - Weatherization Incentives
- **Purpose:** Insulation and weatherization incentive applications
- **Measure Types:**
  - Attic Insulation
  - Floor Insulation
  - Wall Insulation
  - Air Sealing

## Usage

### Opening the CSV
```bash
# View in terminal
cat /Users/isaiah/CPF/pdf_downloads/form_fields_comprehensive.csv

# Open in Excel/Numbers
open /Users/isaiah/CPF/pdf_downloads/form_fields_comprehensive.csv
```

### Filtering by Form Type
```python
import pandas as pd
df = pd.read_csv('form_fields_comprehensive.csv')

# Get all fields for a specific form
hvac_fields = df[df['form_number'] == '320C-HVAC']
print(hvac_fields)
```

### Finding Required Fields
```python
required_fields = df[df['required'] == True]
print(required_fields[['form_number', 'field_name']])
```

## Technical Details

### Extraction Method
- **Tool:** Python with PyPDF2 and PyCryptodome libraries
- **Script:** `extract_form_fields.py`
- **Process:**
  1. Scanned all PDFs in pdf_downloads directory
  2. Extracted text content from each page
  3. Identified form fields using pattern matching
  4. Classified fields by type (signature, text input, checkbox)
  5. Deduplicated fields across documents
  6. Generated comprehensive CSV output

### Limitations
- Some PDFs contain graphical forms that may not be fully captured
- Field validation rules and dependencies are not captured
- Dropdown menu options may not be fully enumerated
- Spanish language forms are included but not specifically tagged

## Next Steps

### Recommended Actions
1. **Validation** - Review CSV against original forms for accuracy
2. **Database Design** - Use field list to design application database schema
3. **Form Digitization** - Create digital versions of paper forms
4. **Data Integration** - Map fields to existing systems
5. **Documentation** - Create field-by-field documentation for staff

### Potential Use Cases
- Digital form creation
- Database schema design
- API endpoint planning
- Data validation rule development
- Staff training materials
- Application workflow design

## Contact
For questions about this extraction:
- **Business:** Community Consulting Partners LLC
- **Contact:** Isaiah Kamrar

---
*Generated: October 30, 2025*
*Source: Energy Trust of Oregon CPF Program Documents*
