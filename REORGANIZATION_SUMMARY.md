# CPF Project - Reorganization Complete

**Date:** October 30, 2025  
**Organization:** Community Consulting Partners LLC  
**Lead:** Isaiah Kamrar

---

## Summary

Successfully reorganized and processed all Energy Trust of Oregon program documents with separate analyses for CPF and Residential programs.

---

## Directory Structure

\`\`\`
/Users/isaiah/CPF/
├── analysis/                  # Combined analysis (543 total fields)
│   ├── form_fields_comprehensive.csv
│   ├── form_fields_enhanced.csv
│   ├── DATA_DICTIONARY.md
│   ├── PROCESSING_SUMMARY.md
│   ├── README_FORM_EXTRACTION.md
│   ├── extract_form_fields.py
│   └── enhance_form_fields.py
│
├── cpf-docs/                  # CPF Program (303 fields)
│   ├── 40 PDF documents
│   ├── form_fields_comprehensive.csv
│   ├── form_fields_enhanced.csv
│   └── README_CPF.md
│
└── residential-docs/          # Residential Program (242 fields)
    ├── 46 PDF documents
    ├── form_fields_comprehensive.csv
    ├── form_fields_enhanced.csv
    └── README_RESIDENTIAL.md
\`\`\`

---

## Analysis Results

### Combined Analysis (/analysis/)
- **Source:** All 86 PDFs
- **Total Fields:** 543
- **Unique Forms:** 19
- **Purpose:** Master database covering both programs

### CPF Program (/cpf-docs/)
- **Source:** 40 CPF-specific PDFs
- **Total Fields:** 303
- **Unique Forms:** 10
- **Key Forms:** 300CPF, 320CPF, 371CPF
- **Target:** Community-based organizations serving underserved populations

### Residential Program (/residential-docs/)
- **Source:** 46 residential program PDFs  
- **Total Fields:** 242
- **Unique Forms:** 10
- **Key Forms:** 320C-HVAC, 320C-WH, 320C-WX, 320ECHP, 350CC
- **Target:** General residential customers and contractors

---

## Documentation Created

### Program-Specific
1. **README_CPF.md** - Complete CPF program guide
2. **README_RESIDENTIAL.md** - Complete residential program guide

### Combined Analysis
3. **DATA_DICTIONARY.md** - Field specifications for all programs
4. **PROCESSING_SUMMARY.md** - Project completion summary
5. **README_FORM_EXTRACTION.md** - Technical methodology

### Root
6. **README.md** - Master directory guide
7. **REORGANIZATION_SUMMARY.md** - This file

---

## Key Differences: CPF vs Residential

| Aspect | CPF Program | Residential Program |
|--------|-------------|---------------------|
| **Documents** | 40 PDFs | 46 PDFs |
| **Fields** | 303 | 242 |
| **Forms** | 300CPF, 320CPF, 371CPF | 320C-*, 350CC |
| **Target** | Underserved communities via CBOs | General customers via contractors |
| **Incentives** | Enhanced (e.g., $1,800-$3,500 DHP) | Standard (e.g., $800 DHP) |
| **Workflow** | Flexible, adapted to partner | Standardized application |
| **Assessment** | Home Energy Assessment ($250) | Optional |
| **No-Cost** | Yes, for income-qualified | No |

---

## Usage

### For CPF Partners
\`\`\`bash
cd /Users/isaiah/CPF/cpf-docs
# Review README_CPF.md
# Use form_fields_enhanced.csv for app development
\`\`\`

### For Residential Contractors  
\`\`\`bash
cd /Users/isaiah/CPF/residential-docs
# Review README_RESIDENTIAL.md
# Use form_fields_enhanced.csv for app development
\`\`\`

### For Full Program Analysis
\`\`\`bash
cd /Users/isaiah/CPF/analysis
# Review DATA_DICTIONARY.md
# Use form_fields_enhanced.csv (all 543 fields)
\`\`\`

---

## Next Steps

1. **Review Program-Specific Data**
   - CPF partners: Focus on cpf-docs/
   - Contractors: Focus on residential-docs/
   
2. **Application Development**
   - Each program has its own field database
   - Separate workflows can be built
   - Common fields can be identified across programs

3. **Data Refinement**
   - Review "other" category fields (43-62% uncategorized)
   - Add program-specific validation rules
   - Map common fields between programs

---

## Contact

**Energy Trust of Oregon:**
- CPF Program: communitypartners@energytrust.org
- Residential: residentialforms@energytrust.org
- Phone: 1.866.311.1822

**Project Lead:**
- Community Consulting Partners LLC
- Isaiah Kamrar

---

*Reorganization completed: October 30, 2025 @ 23:50*
