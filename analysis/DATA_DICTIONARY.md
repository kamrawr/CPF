# CPF Program - Form Fields Data Dictionary

## Overview
This document provides a comprehensive data dictionary for all form fields extracted from the Energy Trust of Oregon Community Partner Fund (CPF) program documents.

**Source File:** `form_fields_enhanced.csv`  
**Total Fields:** 543  
**Unique Forms:** 19  
**Languages:** English (405 fields), Spanish (138 fields)

---

## Table of Contents
1. [Field Schema](#field-schema)
2. [Field Categories](#field-categories)
3. [Data Types](#data-types)
4. [Form Mapping](#form-mapping)
5. [Common Fields](#common-fields)
6. [Validation Rules](#validation-rules)

---

## Field Schema

Each field in `form_fields_enhanced.csv` contains the following attributes:

| Column | Description | Example |
|--------|-------------|---------|
| `field_id` | Unique identifier for the field | `AUTH_CUST_9c7a5f_customer_signature` |
| `form_id` | Standardized form identifier | `CPF-350-CUSTOMER-CONSENT` |
| `form_number` | Original form number from PDF | `350CC` |
| `field_category` | Logical grouping | `customer_authorization` |
| `field_name` | Original field label | `Customer Name and Signature` |
| `normalized_name` | Programmatic field name | `customer_signature` |
| `data_type` | Data type for validation | `signature` |
| `field_type` | UI component type | `Signature` |
| `required` | Whether field is required | `True` or `False` |
| `validation_rules` | Validation rules (pipe-separated) | `required\|signature_required` |
| `language` | Language of the field | `en` or `es` |
| `context` | Additional context from PDF | Explanatory text |
| `document_source` | Source PDF filename | `043_Customer Consent Form...pdf` |

---

## Field Categories

### Distribution by Category

| Category | Count | Description |
|----------|-------|-------------|
| **other** | 293 | Uncategorized fields (needs review) |
| **financial_information** | 45 | Costs, incentives, payments |
| **terms_and_conditions** | 43 | Legal terms, eligibility |
| **equipment_information** | 37 | HVAC, insulation, appliances |
| **customer_authorization** | 26 | Customer signatures |
| **customer_information** | 20 | Customer personal data |
| **contractor_authorization** | 19 | Contractor signatures |
| **technical_specifications** | 19 | Equipment specs (HSPF, AFUE, etc.) |
| **contractor_information** | 16 | Contractor details |
| **utility_information** | 12 | Electric/gas providers |
| **process_instructions** | 9 | Form completion steps |
| **site_information** | 4 | Property details |

### Category Definitions

#### 1. Customer Information (`customer_information`)
- Customer name, email, phone
- Customer type (homeowner, renter, property owner)
- Mailing address

**Common Fields:**
- Customer Name
- Customer Email
- Customer Phone
- Customer Type

#### 2. Customer Authorization (`customer_authorization`)
- Customer signatures
- Authorization agreements
- Consent forms

**Data Types:** Primarily `signature`

#### 3. Contractor Information (`contractor_information`)
- Contractor company name
- OCCB# / Washington License #
- Contractor contact details

**Common Fields:**
- Contractor Company
- OCCB# or Washington License #
- Contractor Full Name

#### 4. Contractor Authorization (`contractor_authorization`)
- Contractor signatures
- Contractor certifications
- Instant incentive agreements

**Data Types:** Primarily `signature`

#### 5. Site Information (`site_information`)
- Site address
- City, State, ZIP
- Year built
- Square footage
- Foundation type
- Number of stories

**Common Fields:**
- Site Address
- City
- State
- ZIP
- Year Built
- Square Feet
- Foundation/Basement

#### 6. Equipment Information (`equipment_information`)
- Ductless Heat Pump
- Ducted Heat Pump
- Gas Furnace
- Water Heater
- Insulation (Attic, Floor, Wall)
- Windows
- Smart Thermostat
- Fireplace
- Air Conditioner

**Data Types:** `text`, `percentage`, `number`

#### 7. Technical Specifications (`technical_specifications`)
- HSPF2 (Heating Seasonal Performance Factor)
- SEER2 (Seasonal Energy Efficiency Ratio)
- EER2 (Energy Efficiency Ratio)
- AFUE (Annual Fuel Utilization Efficiency)
- BTU Capacity
- Model Number
- Manufacturer
- Serial Number

**Data Types:** `number`, `text`

**Validation Examples:**
- HSPF2: `range:7.0-10.0`
- AFUE: `range:70-100`
- SEER2: `range:13-25`

#### 8. Financial Information (`financial_information`)
- Incentive amounts
- Installed cost
- Invoice amounts
- Instant incentive indicators
- Household income
- Funding amounts

**Data Types:** `currency`, `text`

**Validation:** `positive_number`

#### 9. Utility Information (`utility_information`)
- Electric Provider (PGE, Pacific Power)
- Gas Provider (NW Natural, Cascade Natural Gas, Avista)
- Service area information

#### 10. Terms and Conditions (`terms_and_conditions`)
- Eligibility requirements
- Property rights statements
- Disclaimer text
- Authorization statements
- Payment terms
- Tax liability
- Safety codes

#### 11. Process Instructions (`process_instructions`)
- Step-by-step completion guides
- Form submission instructions
- Review requirements

#### 12. Demographic Information (`demographic_information`)
- Optional customer demographics
- Income qualification
- Language preferences
- Household size

---

## Data Types

### Data Type Distribution

| Data Type | Count | Validation | UI Component |
|-----------|-------|------------|--------------|
| `text` | 412 | Max length | Text input |
| `signature` | 75 | Signature required | Signature pad |
| `boolean` | 22 | True/False | Checkbox |
| `number` | 12 | Numeric only | Number input |
| `percentage` | 11 | 0-100 range | Number input with % |
| `currency` | 6 | Positive decimal | Currency input |
| `date` | 3 | Valid date | Date picker |
| `phone` | 1 | Phone format | Phone input |
| `email` | 1 | Email format | Email input |
| `address` | 0 | Multi-line | Address component |
| `zipcode` | 0 | 5 or 9 digits | Zipcode input |
| `state` | 0 | State code | Dropdown |

### Data Type Specifications

#### Text
- **Description:** Free-form text input
- **Validation:** Length limits, pattern matching
- **Examples:** Name, company, model number

#### Signature
- **Description:** Electronic signature capture
- **Validation:** Non-empty signature data
- **Required:** Usually yes
- **Examples:** Customer signature, Contractor signature

#### Boolean
- **Description:** Yes/No, True/False selections
- **UI:** Checkbox or radio button
- **Examples:** Instant incentive (yes/no), ECM present (yes/no)

#### Number
- **Description:** Numeric values without currency
- **Validation:** Range checks, positive values
- **Examples:** HSPF2, SEER2, quantity, square feet

#### Percentage
- **Description:** Percentage values
- **Validation:** Range 0-100
- **Examples:** AFUE, FE (Fireplace Efficiency)

#### Currency
- **Description:** Monetary amounts
- **Validation:** Positive decimal, 2 decimal places
- **Examples:** Installed cost, incentive amount

#### Date
- **Description:** Date fields
- **Validation:** Valid date, not future date (typically)
- **Examples:** Install date, signature date, date of birth

#### Phone
- **Description:** Phone numbers
- **Validation:** Format (###) ###-#### or ##########
- **Examples:** Customer telephone

#### Email
- **Description:** Email addresses
- **Validation:** Valid email format
- **Examples:** Customer email

---

## Form Mapping

### Primary Forms

| Form ID | Form Number | Fields | Primary Use | Required Signatures |
|---------|-------------|--------|-------------|---------------------|
| **CPF-350-CUSTOMER-CONSENT** | 350CC | 17 | Customer & contractor consent | Customer + Contractor |
| **CPF-320-HVAC-INCENTIVE** | 320C-HVAC | 41 | HVAC equipment incentives | Customer + Contractor |
| **CPF-320-WATER-HEATING-INCENTIVE** | 320C-WH | 23 | Water heating incentives | Customer + Contractor |
| **CPF-320-WEATHERIZATION-INCENTIVE** | 320C-WX | 27 | Weatherization incentives | Customer + Contractor |
| **CPF-320-EXTENDED-CAPACITY-HP** | 320ECHP | 29 | Extended capacity heat pumps | Customer + Contractor |
| **CPF-300-HOME-ASSESSMENT** | 300CPF | 92 | Home energy assessment | Customer + Organization |
| **CPF-320-PROJECT-DETAILS** | 320CPF | 54 | Project details | Varies |
| **CPF-300-HEAT-PUMP-QUESTIONNAIRE** | 300HPQ | 5 | Heat pump qualification | Staff |

### Form Dependencies

```
Customer Journey Flow:
1. CPF-300-HOME-ASSESSMENT → Initial assessment
2. CPF-350-CUSTOMER-CONSENT → Authorization
3. CPF-320-*-INCENTIVE → Equipment-specific application
   ├── CPF-320-HVAC-INCENTIVE (heating/cooling)
   ├── CPF-320-WATER-HEATING-INCENTIVE (water heaters)
   └── CPF-320-WEATHERIZATION-INCENTIVE (insulation/windows)
4. CPF-320-PROJECT-DETAILS → Project completion
```

---

## Common Fields (Cross-Form)

### Fields That Appear Across Multiple Forms

These fields should be auto-populated when a customer completes multiple forms:

#### Customer Fields
- Customer Name (`CUST_*_full_name`)
- Customer Email (`CUST_*_email_address`)
- Customer Phone (`CUST_*_phone_number`)
- Site Address (`SITE_*_site_address`)
- City (`SITE_*_city`)
- State (`SITE_*_state`)
- ZIP (`SITE_*_zip`)

#### Contractor Fields
- Contractor Company (`CNTR_*_contractor_company`)
- OCCB# / License # (`CNTR_*_license_number`)
- Contractor Name (`CNTR_*_full_name`)

#### Site/Property Fields
- Year Built (`SITE_*_year_built`)
- Square Feet (`SITE_*_square_feet`)
- Foundation Type (`SITE_*_foundation_basement`)
- Electric Provider (`UTIL_*_electric_provider`)
- Gas Provider (`UTIL_*_gas_provider`)

---

## Validation Rules

### Standard Validation Rules

| Rule | Description | Applies To |
|------|-------------|------------|
| `required` | Field must have a value | Various |
| `email_format` | Valid email format | Email fields |
| `phone_format` | Valid phone format | Phone fields |
| `zipcode_format` | 5 or 9 digit ZIP | ZIP fields |
| `valid_date` | Parseable date | Date fields |
| `positive_number` | Must be > 0 | Currency, quantities |
| `signature_required` | Signature data present | Signature fields |
| `range:X-Y` | Value between X and Y | Technical specs |

### Equipment-Specific Validations

#### HVAC Equipment
- **HSPF2:** 7.0 - 10.0 (Heating Seasonal Performance Factor 2)
- **SEER2:** 13 - 25 (Seasonal Energy Efficiency Ratio 2)
- **EER2:** 9 - 15 (Energy Efficiency Ratio 2)
- **AFUE:** 70 - 100% (Annual Fuel Utilization Efficiency)

#### Capacity/Size
- **BTU:** Positive integer (typically 6,000 - 60,000)
- **Gallons:** 30 - 100 (water heaters)
- **Square Feet:** Positive integer

### Cross-Field Validations

#### Business Rules
1. **Instant Incentive:** If "Yes", incentive amount must be > $0
2. **Rental Property:** If selected, customer cannot be "Owner Occupied"
3. **Electric Provider Required:** If heating fuel is electric
4. **Gas Provider Required:** If heating fuel is gas
5. **AHRI Certificate:** Required for certain heat pump types

---

## Integration Notes for App Development

### Database Schema Recommendations

```sql
-- Forms table
CREATE TABLE forms (
    form_id VARCHAR(50) PRIMARY KEY,
    form_number VARCHAR(20),
    form_name VARCHAR(200),
    form_version VARCHAR(20),
    language VARCHAR(2),
    active BOOLEAN DEFAULT TRUE
);

-- Field definitions table
CREATE TABLE field_definitions (
    field_id VARCHAR(100) PRIMARY KEY,
    form_id VARCHAR(50) REFERENCES forms(form_id),
    field_category VARCHAR(50),
    field_name VARCHAR(200),
    normalized_name VARCHAR(100),
    data_type VARCHAR(50),
    required BOOLEAN,
    validation_rules TEXT,
    display_order INT,
    language VARCHAR(2)
);

-- Application submissions
CREATE TABLE applications (
    application_id SERIAL PRIMARY KEY,
    form_id VARCHAR(50) REFERENCES forms(form_id),
    customer_id INT,
    contractor_id INT,
    submission_date TIMESTAMP,
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Field values
CREATE TABLE field_values (
    value_id SERIAL PRIMARY KEY,
    application_id INT REFERENCES applications(application_id),
    field_id VARCHAR(100) REFERENCES field_definitions(field_id),
    value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### API Endpoints Suggested

```
GET  /api/forms                     # List all forms
GET  /api/forms/:form_id            # Get form definition with fields
GET  /api/forms/:form_id/fields     # Get fields for a form
POST /api/applications              # Create new application
GET  /api/applications/:id          # Get application with values
PUT  /api/applications/:id          # Update application
POST /api/applications/:id/submit   # Submit for review
GET  /api/customers/:id/applications # Customer's applications
```

### Frontend Component Mapping

| Data Type | React Component | Props |
|-----------|-----------------|-------|
| text | `<TextInput>` | maxLength, pattern |
| signature | `<SignaturePad>` | required, clear |
| boolean | `<Checkbox>` | checked, onChange |
| number | `<NumberInput>` | min, max, step |
| percentage | `<PercentInput>` | min: 0, max: 100 |
| currency | `<CurrencyInput>` | min: 0, precision: 2 |
| date | `<DatePicker>` | minDate, maxDate |
| phone | `<PhoneInput>` | format |
| email | `<EmailInput>` | validation |

---

## Change Log

| Date | Version | Changes |
|------|---------|---------|
| 2025-10-30 | 1.0 | Initial data dictionary creation |

---

*For questions or updates, contact: Community Consulting Partners LLC - Isaiah Kamrar*
