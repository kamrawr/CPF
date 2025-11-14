# 🏛️ Program Management Center

**Comprehensive hub for energy efficiency program tools, research, and data analytics**

**Live Site:** [View Program Management Center](program-management-center.html)

**Organization:** Community Consulting Partners LLC  
**Author:** Isaiah Kamrar

---

## 🎯 Overview

The Program Management Center is a unified platform that integrates multiple projects and tools developed for energy efficiency program management, research synthesis, and community engagement. This mega GitHub page combines 8 major projects spanning research, interactive tools, data analytics, and operational resources.

## 📊 Integrated Projects

### 🧠 Research & Analysis

#### 1. **Research Synthesis Lab**
Interactive exploration of 12 literature reviews and research syntheses covering:
- Higher education & workforce development
- Labor market dynamics & automation
- Energy equity & community infrastructure
- Machine learning & predictive modeling
- COVID-19 economic impacts

**Stats:** 12 projects • 500+ studies reviewed • D3.js visualizations  
**Links:** [Live Site](https://kamrawr.github.io/research-synthesis-lab/) | [GitHub](https://github.com/kamrawr/research-synthesis-lab)

#### 2. **Community Resilience Initiative**
Research-backed framework connecting workforce development, housing infrastructure, and energy efficiency to build community resilience.

**Link:** [View Initiative](community-resilience-initiative.html)

---

### ⚡ Assessment Tools

#### 3. **CPF Assessment Tool**
Comprehensive home energy assessment and incentive calculator:
- Complete 5-step assessment workflow
- Property intake and eligibility check (2025 HUD income limits)
- Home energy assessment (heating, cooling, insulation, windows)
- Personalized equipment recommendations
- Financial summary with incentive calculations
- 4 incentive tiers: Standard, CPF Enhanced, CERTA Premium, No-Cost
- PII-protected (all processing in browser)
- Print-friendly reports

**Features:** 5-step workflow • 4 incentive tiers • PII-protected  
**Links:** [Open Tool](https://kamrawr.github.io/CPF/cpf-assessment-tool.html) | [GitHub](https://github.com/kamrawr/CPF)

#### 4. **Oregon Income Eligibility Calculator**
Calculate income eligibility for Oregon programs:
- 2025 HUD rates
- Multiple income frequencies (annual, monthly, weekly, hourly)
- Tax status options (pre-tax/after-tax)
- Visual charts with Chart.js
- Real-time updates

**Features:** 2025 rates • Interactive charts • Mobile friendly  
**Links:** [Open Calculator](https://kamrawr.github.io/oregon-income-calculator/) | [GitHub](https://github.com/kamrawr/oregon-income-calculator)

---

### 📈 Data & Analytics

#### 6. **Oregon Housing Analysis**
Comprehensive housing, income, and affordability analysis:
- All 36 Oregon counties
- Investor-Owned Utility (IOU) service territories
- Interactive D3.js visualizations
- County comparison tools
- AMI disparities and housing supply gaps

**Data:** 36 counties • 134K+ multifamily units • HUD AMI 2025  
**Links:** [View Analysis](https://kamrawr.github.io/oregon-housing-analysis/) | [GitHub](https://github.com/kamrawr/oregon-housing-analysis)

---

### 📚 Operations & Resources

#### 7. **CPF Document Library**
Comprehensive collection of Energy Trust CPF program documents:
- 70+ documents across 13 categories
- Application forms (300CPF, 320CPF, 371CPF, etc.)
- Program guides & specifications
- Marketing materials & customer resources
- Equipment specification sheets
- Bilingual support (English/Spanish)
- Smart search & filtering

**Content:** 70+ documents • 13 categories • Bilingual  
**Links:** [Browse Library](index.html) | [Staff Portal](cpf-staff-portal.html)

#### 8. **CPF Program Guide**
Interactive guide to Energy Trust's Community Partner Fund:
- Program overview & eligibility
- Application process walkthrough
- Incentive structures & calculations
- Equipment specifications
- Contractor resources
- Customer communication templates

**Links:** [View Guide](cpf-program-guide.html) | [Contractor Info](contractor_cpf_opportunity.html)

---

## 🏗️ Project Architecture

```
Program Management Center
├── Research & Analysis
│   ├── Research Synthesis Lab (12 projects)
│   └── Community Resilience Initiative
├── Assessment Tools
│   ├── CPF Assessment Tool
│   └── Oregon Income Eligibility Calculator
├── Data & Analytics
│   └── Oregon Housing Analysis
└── Operations & Resources
    ├── CPF Document Library
    └── CPF Program Guide
```

## 💻 Tech Stack

### Frontend
- **HTML5, CSS3, JavaScript (ES6+)** - Core technologies
- **D3.js v7** - Data visualizations
- **Chart.js** - Interactive charts
- **PicoCSS** - Minimal CSS framework
- **Marked.js** - Markdown rendering

### Design Philosophy
- Mobile-first responsive design
- Minimal dependencies
- Offline-capable where possible
- Accessibility focused
- Fast load times

### Deployment
- **GitHub Pages** - Static site hosting
- **Git** - Version control
- **CDN-hosted libraries** - No build process required

## 🚀 Quick Start

### View the Program Management Center

**Option 1: Open Locally**
```bash
# Navigate to CPF directory
cd /Users/isaiah/CPF

# Open in browser
open program-management-center.html
```

**Option 2: Deploy to GitHub Pages**
```bash
# From CPF directory
git add program-management-center.html PMC-README.md
git commit -m "Add Program Management Center"
git push origin main

# Enable GitHub Pages in repo settings
# Set source to main branch, root directory
```

Then access at: `https://[username].github.io/CPF/program-management-center.html`

## 📊 Key Features

### Filtering & Navigation
- Filter by category: Research, Tools, Data, Operations
- Dynamic project count updates
- Direct links to all projects and GitHub repos
- Responsive grid layout

### Stats Dashboard
- 6 active projects
- 12 research syntheses
- 70+ documents
- 36 Oregon counties covered

### Project Cards
Each project includes:
- Visual icon & category badge
- Project description & key features
- Important metrics & statistics
- Direct links to live sites & repositories

## 🎯 Use Cases

### For Energy Efficiency Programs
- Assess homes with standardized tools
- Calculate income eligibility
- Access program documents & forms
- Analyze county-level housing data

### For Researchers
- Explore literature syntheses
- Access interactive visualizations
- Review methodology & findings
- Connect research to practice

### For Program Managers
- Centralized resource hub
- Quick access to all tools
- Contractor onboarding materials
- Marketing & outreach templates

### For Community Partners
- Educational resources
- Bilingual materials
- Program eligibility tools
- Community resilience frameworks

## 📁 Repository Structure

```
CPF/
├── program-management-center.html    # Main hub page
├── PMC-README.md                      # This file
├── index.html                         # CPF Document Library
├── cpf-program-guide.html            # CPF Program Guide
├── cpf-staff-portal.html             # Staff Portal
├── contractor_cpf_opportunity.html   # Contractor Info
├── community-resilience-initiative.html
├── cpf-docs/                         # CPF documents
├── residential-docs/                 # Residential docs
└── analysis/                         # Form field analysis
```

## 🔗 External Projects

These projects are hosted in separate repositories:
- [research-synthesis-lab](https://github.com/kamrawr/research-synthesis-lab)
- [oregon-housing-analysis](https://github.com/kamrawr/oregon-housing-analysis)
- [oregon-income-calculator](https://github.com/kamrawr/oregon-income-calculator)

## 🛠️ Maintenance & Updates

### Adding New Projects
1. Open `program-management-center.html`
2. Add new project card in the `<div class="project-grid">` section
3. Follow existing card structure
4. Assign appropriate `data-category` attribute
5. Update stats in the stats bar if needed

### Updating Project Information
- Edit project descriptions in the HTML
- Update links to point to new locations
- Modify stats and metrics as projects evolve
- Keep GitHub repository links current

## 📝 Data Sources

- **HUD Area Median Income:** 2025 FY data for Oregon counties
- **Energy Trust of Oregon:** Program data, incentive structures, documents
- **College Scorecard:** Institutional & earnings data for research projects
- **O*NET:** Occupational task content for labor market analysis
- **Portland Maps:** Property assessor database
- **U.S. Census Bureau:** Population estimates

## 🤝 Contributing

This is a portfolio of projects developed by Community Consulting Partners LLC. For specific project contributions, please visit the individual GitHub repositories.

## 📄 License

- **Code:** MIT License
- **Data:** Public domain / government sources / Energy Trust materials
- **Documentation:** Creative Commons Attribution 4.0

## 🆘 Support

For questions or issues with specific projects, please:
1. Check the individual project README
2. Visit the GitHub repository
3. Create an issue in the appropriate repo

## 🏷️ Tags

`energy-efficiency` `program-management` `research-synthesis` `data-visualization` `assessment-tools` `oregon` `housing-analysis` `workforce-development` `community-resilience` `d3js` `interactive-tools`

---

**Built with ❤️ for energy efficiency and community resilience**

*Making program management accessible through open tools and research*

**Community Consulting Partners LLC**  
Isaiah Kamrar  
[GitHub Profile](https://github.com/kamrawr)

**Last Updated:** October 2025  
**Version:** 1.0
