# Community Partner Funding (CPF) Program - Form Fields

## Overview
**303 form fields** extracted from **40 CPF program PDF documents**  
**10 unique forms** identified  
**Languages:** English & Spanish

---

## Files in this Directory

### PDF Documents (40 files)
- **Program Information Sheets** - PI0320CPF (Oregon & Washington)
- **Forms** - 300CPF, 320CPF, 371CPF series
- **Onboarding Materials** - Presentations, checklists
- **Assessment Templates** - Home Energy Assessment forms
- **Incentive Grids** - Customizable incentive summaries
- **Specifications Manual** - 2025 Technical specifications
- **Spanish Versions** - Translated forms and materials

### Form Field Database

**`form_fields_enhanced.csv`** (⭐ PRIMARY)
- 303 CPF-specific form fields
- Fully categorized and typed
- Ready for application development

**`form_fields_comprehensive.csv`**
- Raw extracted data

---

## Field Statistics

### By Category

| Category | Count | %  |
|----------|-------|-----|
| Other (needs review) | 189 | 62% |
| Equipment Information | 34 | 11% |
| Financial Information | 15 | 5% |
| Terms & Conditions | 15 | 5% |
| Customer Information | 13 | 4% |
| Customer Authorization | 8 | 3% |
| Utility Information | 7 | 2% |
| Technical Specifications | 7 | 2% |
| Contractor Information | 6 | 2% |
| Contractor Authorization | 5 | 2% |
| Site Information | 4 | 1% |

### By Data Type

| Data Type | Count |
|-----------|-------|
| Text | 230 |
| Signature | 37 |
| Boolean | 22 |
| Number | 6 |
| Percentage | 5 |
| Phone | 1 |
| Date | 1 |
| Email | 1 |

---

## Key CPF Forms

### Form 300CPF - Home Energy Assessment
- Customer authorization
- Site information
- Assessment findings
- Equipment recommendations
- Bilingual (English/Spanish)

### Form 320CPF - Project Details
- Project information
- Measures installed
- Contractor details
- Funding breakdown

### Form 371CPF - Participation Agreement
- One-time partnership agreement
- Terms and conditions
- Organization information

---

## CPF Program Highlights

### Enhanced Incentives
- **Ductless Heat Pump (Single-Family):** $1,800 (vs $800 standard)
- **Ductless Heat Pump (Manufactured):** $3,500 (vs $800 standard)
- **Ducted Heat Pump:** $4,000 (vs $1,000 standard)
- **"No-Cost" Options:** Variable (100% coverage for income-qualified)

### Target Communities
- Low-to-moderate income (LMI) households
- Communities of color
- Indigenous communities
- Rural communities
- Veterans
- People with disabilities

### Eligible Property Types
- Detached single-family homes
- Manufactured homes
- Small multifamily (duplexes, triplexes, fourplexes, townhomes)

---

## Eligible Improvements

**HVAC:**
- Ductless heat pumps
- Ducted heat pumps
- Extended capacity heat pumps
- Gas furnaces (95%+ AFUE)
- Heat pump controls
- Smart thermostats

**Water Heating:**
- Heat pump water heaters (including no-cost)
- Gas tankless water heaters

**Weatherization:**
- Attic insulation (R-38+)
- Wall insulation (R-11+)
- Floor insulation (R-30+)
- Windows (standard & enhanced)

**Assessment:**
- Home Energy Assessment - $250/home

---

## For Developers

### Database Schema
Fields are structured with:
- `field_id` - Unique identifier
- `form_id` - CPF-specific form reference
- `field_category` - Logical grouping
- `data_type` - Validation type
- `validation_rules` - Business rules
- `language` - en/es flag

### Forms Identified

| Form ID | Form Number | Fields | Primary Use |
|---------|-------------|--------|-------------|
| CPF-300-HOME-ASSESSMENT | 300CPF | 92 | Home energy assessment |
| CPF-320-PROJECT-DETAILS | 320CPF | 54 | Project completion |
| CPF-371-ENERGY-TRUST | 371CPF | 16 | Partnership agreement |
| CPF-300-HEAT-PUMP-QUESTIONNAIRE | 300HPQ | 5 | Heat pump qualification |

---

## Contact

**Energy Trust CPF Program:**
- Email: communitypartners@energytrust.org
- Phone: 1.866.311.1822

**Project Lead:**
- Community Consulting Partners LLC
- Isaiah Kamrar

---

*Last Updated: October 30, 2025*
