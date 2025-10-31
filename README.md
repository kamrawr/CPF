# Energy Trust of Oregon - CPF Project Directory

**Organization:** Community Consulting Partners LLC  
**Project Owner:** Isaiah Kamrar  
**Last Updated:** October 30, 2025

---

## 🌐 Interactive Web Pages

Explore the CPF program resources through these interactive pages:

- **[📚 Document Library](https://isaiahkamrar.github.io/CPF/)** - Browse all 70+ CPF and residential program documents
- **[📖 CPF Program Guide](https://isaiahkamrar.github.io/CPF/cpf-program-guide.html)** - Complete guide to the Community Partner Funding program
- **[🛠️ CPF Staff Portal](https://isaiahkamrar.github.io/CPF/cpf-staff-portal.html)** - Quick reference portal for staff and partners
- **[🤝 Contractor Opportunities](https://isaiahkamrar.github.io/CPF/contractor_cpf_opportunity.html)** - Partnership opportunities for contractors

---

## Directory Structure

```
CPF/
├── README.md (this file)
├── analysis/                    # Combined analysis (all programs)
│   ├── form_fields_comprehensive.csv    # All 543 fields (raw)
│   ├── form_fields_enhanced.csv         # All 543 fields (enhanced)
│   ├── DATA_DICTIONARY.md               # Complete specifications
│   ├── PROCESSING_SUMMARY.md            # Project summary
│   ├── README_FORM_EXTRACTION.md        # Technical details
│   ├── extract_form_fields.py           # Extraction script
│   └── enhance_form_fields.py           # Enhancement script
├── cpf-docs/                    # CPF program (303 fields)
│   ├── [40 PDFs]                # CPF forms & materials
│   ├── form_fields_enhanced.csv # ⭐ CPF-specific database
│   ├── form_fields_comprehensive.csv
│   └── README_CPF.md            # CPF documentation
└── residential-docs/            # Standard program (242 fields)
    ├── [46 PDFs]                # Residential forms & materials
    ├── form_fields_enhanced.csv # ⭐ Residential-specific database
    ├── form_fields_comprehensive.csv
    └── README_RESIDENTIAL.md    # Residential documentation
```

---

## What's What

### `/cpf-docs/` - Community Partner Funding Documents

**Purpose:** CPF-specific program materials for community-based organizations

**Key Documents:**
- `001_Program Information sheet_ PI0320CPF.pdf` - Main CPF program guide (Oregon)
- `002_...PI0320CPF-WA.pdf` - CPF program guide (Washington)
- `003_CPF-Overview-Document-1.pdf` - Program overview
- `004_CPF-Overview-Document_For-Contractors.pdf` - Contractor guide
- `007_CPF-Onboarding-PPT.pdf` - Onboarding presentation
- `008_CPF_Onboarding_Checklist.pdf` - Getting started checklist
- `011_HES_FM0300CPF.pdf` - Home Energy Assessment form
- `013_HES_FM0320CPF.pdf` - Project details form
- `018_CPF-Home-Energy-Assessment-Flyer-Template.pdf` - Marketing template
- `019_CPF-Incentive-Grid_INFOGR_0423-Customizable.pdf` - Incentive grid

**Includes:**
- Program information sheets
- Forms (300CPF, 320CPF, 371CPF series)
- Onboarding materials
- Assessment templates
- Incentive grids
- Enhanced windows program docs
- No-cost program guides
- Spanish language versions

**File Count:** 40 PDFs

---

### `/residential-docs/` - Standard Residential Program Documents

**Purpose:** Standard Energy Trust residential program forms and materials

**Key Documents:**

#### Application Forms:
- `034_Heating and Cooling, Contractor Installed–Form 320C-HVAC.pdf`
- `036_Water Heating, Contractor Installed–Form 320C-WH.pdf`
- `038_Weatherization, Contractor Installed_ Form 320C-WX.pdf`
- `042_Extended Capacity Heat Pump...Form 320ECHP.pdf`
- `043_Customer Consent Form–Form 350CC.pdf`

#### Specification Sheets:
- `001_...PI 320I.pdf` - Standard residential program info
- `005_2025 Specifications manual.pdf`
- `007_2025 Quality Management Policy.pdf`

#### Equipment Guides:
- Heat Pumps (ductless, ducted, extended capacity)
- Gas furnaces and fireplaces
- Water heaters (heat pump, gas tankless)
- Insulation (attic, floor, wall)
- Windows
- Smart thermostats
- Air conditioners

#### Community Outreach:
- `021_CBO-Roadmap_CLEAN.pdf` - CBO partnership roadmap
- `029_CBO-Low-Cost-No-Cost-Biligual-Flyer_CLEAN.pdf`
- `032_DHP-Engagement-Guide-English_CLEAN.pdf`

**File Count:** 46 PDFs + 6 analysis files

---

## Form Field Database

### Master Data File

**`form_fields_enhanced.csv`** (⭐ PRIMARY)
- **543 fields** from 86 PDFs across 19 form types
- Fully categorized and typed for app development
- Includes: field_id, form_id, data_type, validation_rules, language tags

### Documentation

1. **`DATA_DICTIONARY.md`** - Complete specifications
   - Field schemas and definitions
   - Category descriptions (12 categories)
   - Data types (9 types)
   - Validation rules
   - Database schemas
   - API endpoint suggestions
   - Frontend component mapping

2. **`PROCESSING_SUMMARY.md`** - Executive summary
   - Project statistics
   - Deliverables overview
   - Next steps
   - Development phases

3. **`README_FORM_EXTRACTION.md`** - Technical details
   - Extraction methodology
   - Tools used
   - Limitations
   - Form identification

---

## Program Overview

### Community Partner Funding (CPF)

**What:** Enhanced incentive program for underserved communities  
**Who:** Community-based organizations, housing authorities, nonprofits  
**Serves:** LMI households, communities of color, rural, veterans, people with disabilities

**Key Features:**
- Higher incentive amounts (e.g., $1,800-$3,500 vs $800 for ductless heat pumps)
- "No-Cost" options for income-qualified customers
- Flexible workflows adapted to partner organizations
- Home Energy Assessment support ($250/home)

### Standard Residential Program

**What:** Standard Energy Trust residential incentives  
**Who:** Any licensed contractor or homeowner  
**Serves:** All eligible utility customers

**Key Features:**
- Standard incentive amounts
- Trade Ally network
- Instant incentives available
- Self-serve online applications

---

## Quick Reference

### CPF Incentive Highlights (Oregon)

| Upgrade | CPF Incentive | Standard | Difference |
|---------|---------------|----------|------------|
| Ductless Heat Pump (Single-Family) | $1,800 | $800 | +$1,000 |
| Ductless Heat Pump (Manufactured) | $3,500 | $800 | +$2,700 |
| Ducted Heat Pump | $4,000 | $1,000 | +$3,000 |
| "No-Cost" Heat Pump | Variable (Full) | N/A | 100% coverage |
| High Efficiency Gas Furnace | $2,900 | $1,600 | +$1,300 |
| Heat Pump Water Heater | $240 + retail | $50-75 + retail | +~$165-190 |

### Eligible Improvements

**HVAC:**
- Ductless heat pumps
- Ducted heat pumps
- Extended capacity heat pumps
- Gas furnaces (95%+ AFUE)
- Heat pump controls
- Smart thermostats

**Water Heating:**
- Heat pump water heaters
- Gas tankless water heaters

**Weatherization:**
- Attic insulation
- Wall insulation
- Floor insulation
- Windows (standard & enhanced)
- Air sealing

**Other:**
- Home Energy Assessments
- Central air conditioners

---

## For Developers

### Using the Field Database

The `form_fields_enhanced.csv` is ready for:

1. **Database Import** - Field IDs, data types, validation rules included
2. **API Development** - Standardized form IDs and field categories
3. **Dynamic Forms** - Component mapping and validation specs
4. **Reporting** - Categorized fields with context

See `DATA_DICTIONARY.md` for:
- SQL schema recommendations
- API endpoint suggestions
- Frontend component mapping
- Validation rule specifications

---

## Contact

**Energy Trust of Oregon:**
- Residential Programs: 1.866.311.1822
- Email: residentialforms@energytrust.org
- CPF Inquiries: communitypartners@energytrust.org

**Project Lead:**
- Community Consulting Partners LLC
- Isaiah Kamrar

---

## Notes

- All CPF files downloaded: Oct 30, 2025 @ 16:09
- All residential files downloaded: Oct 30, 2025 @ 16:22-16:23
- Form field extraction completed: Oct 30, 2025 @ 16:36
- Directory reorganization: Oct 30, 2025 @ 16:43

**File Naming Convention:** `###_Document-Title.pdf` where ### indicates download order
