# Standard Residential Program - Form Fields

## Overview
**242 form fields** extracted from **46 residential program PDF documents**  
**10 unique forms** identified  
**Languages:** English & Spanish

---

## Files in this Directory

### PDF Documents (46 files)
- **Application Forms** - 320C series (HVAC, Water Heating, Weatherization)
- **Consent Forms** - 350CC Customer consent
- **Equipment Guides** - Heat pumps, furnaces, water heaters, insulation
- **Specification Sheets** - Technical requirements
- **Community Outreach** - CBO roadmaps, engagement guides
- **Accordion Files** - Quick reference materials
- **Spanish Versions** - Translated application forms

### Form Field Database

**`form_fields_enhanced.csv`** (⭐ PRIMARY)
- 242 residential program form fields
- Fully categorized and typed
- Ready for application development

**`form_fields_comprehensive.csv`**
- Raw extracted data

---

## Field Statistics

### By Category

| Category | Count | %  |
|----------|-------|-----|
| Other (needs review) | 104 | 43% |
| Financial Information | 30 | 12% |
| Terms & Conditions | 28 | 12% |
| Customer Authorization | 18 | 7% |
| Contractor Authorization | 15 | 6% |
| Technical Specifications | 12 | 5% |
| Contractor Information | 11 | 5% |
| Process Instructions | 9 | 4% |
| Customer Information | 7 | 3% |
| Utility Information | 5 | 2% |
| Equipment Information | 3 | 1% |

### By Data Type

| Data Type | Count |
|-----------|-------|
| Text | 182 |
| Signature | 40 |
| Number | 6 |
| Currency | 6 |
| Percentage | 6 |
| Date | 2 |

---

## Key Residential Forms

### Form 320C-HVAC - Heating and Cooling Incentives
- **46 fields**
- Application for contractor-installed HVAC equipment
- Ductless heat pumps, ducted heat pumps, gas furnaces
- Smart thermostats, heat pump controls
- Customer and contractor signatures required

### Form 320C-WH - Water Heating Incentives
- **23 fields**
- Heat pump water heaters
- Gas tankless water heaters
- Installation details and specifications

### Form 320C-WX - Weatherization Incentives
- **27 fields**
- Attic, wall, and floor insulation
- Air sealing measures
- Energy efficiency specifications

### Form 320ECHP - Extended Capacity Heat Pump
- **32 fields**
- Special heat pump category
- Can replace any heating system type
- Advanced specifications required

### Form 350CC - Customer Consent
- **17 fields**
- Required for all contractor-installed work
- Customer and contractor authorization
- Terms and conditions acceptance

---

## Standard Program Highlights

### Incentive Structure
- **Ductless Heat Pump:** $800
- **Ducted Heat Pump:** $1,000
- **Extended Capacity Heat Pump:** $2,000-$6,650
- **High Efficiency Gas Furnace:** $1,600
- **Heat Pump Water Heater:** $50-$240
- **Insulation:** Variable per sq ft
- **Windows:** $1.00-$1.50 per sq ft

### Eligibility
- Customers of PGE, Pacific Power, NW Natural, Cascade Natural Gas, or Avista
- Owner-occupied or rental properties
- Single-family, manufactured, and eligible multifamily
- Work by licensed contractors or Trade Allies

### Property Types
- Single-family homes
- Manufactured homes
- Duplexes, triplexes, fourplexes
- Townhomes (side-by-side, no units above/below)

---

## Eligible Improvements

**HVAC:**
- Ductless heat pumps (HSPF2 ≥8.10)
- Ducted heat pumps (HSPF2 ≥7.50)
- Extended capacity heat pumps
- Gas furnaces (95%+ AFUE)
- Heat pump controls ($250)
- Smart thermostats ($250 single-family, $100 multifamily)
- Central air conditioners

**Water Heating:**
- Heat pump water heaters (NEEA Tier 3)
- Gas tankless water heaters (Oregon only)

**Weatherization:**
- Attic insulation (R-38+)
- Wall insulation (R-11+)
- Floor insulation (R-30+)
- Windows (U-Value 0.22-0.27)

**Other:**
- Gas fireplaces (70%+ FE)

---

## Application Process

### Steps to Completion
1. **Review** - Customer & contractor review eligibility
2. **Customer Completes** - Customer information, site details
3. **Contractor Completes** - Equipment info, paid invoice
4. **Sign** - Both parties sign application
5. **Submit** - To Energy Trust within 60 days

### Required Documentation
- Completed application form
- Itemized contractor invoice (paid in full)
- Customer consent form (350CC)
- AHRI certificate (for certain equipment)
- Equipment specifications

### Processing Time
- 4-6 weeks after complete submission
- Incentive check issued to customer (or contractor for instant incentives)

---

## For Developers

### Database Schema
Fields are structured with:
- `field_id` - Unique identifier
- `form_id` - Standard form reference (CPF-320-*)
- `field_category` - Logical grouping
- `data_type` - Validation type
- `validation_rules` - Business rules
- `language` - en/es flag

### Forms Identified

| Form ID | Form Number | Fields | Primary Use |
|---------|-------------|--------|-------------|
| CPF-320-HVAC-INCENTIVE | 320C-HVAC | 46 | HVAC equipment |
| CPF-320-EXTENDED-CAPACITY-HP | 320ECHP | 32 | Extended capacity HP |
| CPF-320-WEATHERIZATION-INCENTIVE | 320C-WX | 27 | Insulation & air sealing |
| CPF-320-WATER-HEATING-INCENTIVE | 320C-WH | 23 | Water heaters |
| CPF-350-CUSTOMER-CONSENT | 350CC | 17 | Customer authorization |

---

## Technical Specifications

### HVAC Equipment Requirements
- **HSPF2:** 7.50-10.0 depending on equipment type
- **SEER2:** 13-25 for cooling
- **EER2:** 9-15 for efficiency
- **AFUE:** 70-100% for gas furnaces

### Insulation Requirements
- **Attic:** R-38 or greater
- **Walls:** R-11 or greater (existing R-4 or less)
- **Floor:** R-30 or greater (existing R-11 or less)
- **Manufactured Homes:** May have different R-values

### Windows Requirements
- **U-Value:** 0.22-0.30
- Must replace existing windows
- Single-pane or double-pane metal frame

---

## Contact

**Energy Trust Residential Programs:**
- Email: residentialforms@energytrust.org
- Phone: 1.866.311.1822
- Fax: 1.866.516.7592

**Trade Ally Support:**
- Website: www.energytrust.org
- Specifications Manual: www.energytrust.org/specmanual

**Project Lead:**
- Community Consulting Partners LLC
- Isaiah Kamrar

---

*Last Updated: October 30, 2025*
