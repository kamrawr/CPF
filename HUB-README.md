# ⚡ Energy Trust CPF Resource Hub

**Focused, intuitive hub for CPF program management and energy assessments**

**Live Site:** [View Resource Hub](https://kamrawr.github.io/CPF/hub.html)

---

## 🎯 Overview

The CPF Resource Hub is a clean, focused interface that brings together essential resources for Energy Trust of Oregon's Community Partner Funding program. It integrates existing CPF documentation pages with practical assessment tools—all in one intuitive, mobile-friendly interface.

## 📋 What's Included

### CPF Program Resources & Staff Tools (6 Items)
Pages within this repository and external staff resources:

1. **Document Library** (`index.html`)
   - 70+ CPF and residential program documents
   - Application forms, program guides, marketing materials
   - Equipment specifications
   - Bilingual English/Spanish support
   - Smart search and filtering

2. **CPF Program Guide** (`cpf-program-guide.html`)
   - Interactive program guide
   - Eligibility criteria
   - Application processes
   - Incentive structures
   - Equipment specifications

3. **Staff Portal** (`cpf-staff-portal.html`)
   - Quick reference for staff and partners
   - Easy access to forms
   - Program information
   - Onboarding materials
   - Frequently used resources

4. **Contractor Opportunities** (`contractor_cpf_opportunity.html`)
   - Partnership information
   - Enhanced incentives
   - Requirements and getting started
   - Contractor resources

5. **Oregon Housing Analysis** (External)
   - Comprehensive analysis of housing and affordability
   - All 36 Oregon counties
   - Interactive D3.js visualizations
   - County comparison tools
   - HUD AMI data for program targeting
   - Link: [View Analysis](https://kamrawr.github.io/oregon-housing-analysis/)
   - Repository: [GitHub](https://github.com/kamrawr/oregon-housing-analysis)

6. **Research Synthesis Lab** (External)
   - 12 literature reviews and research syntheses
   - Energy equity and community resilience research
   - Workforce development insights
   - Housing infrastructure studies
   - Evidence-based program design support
   - Link: [Explore Research](https://kamrawr.github.io/research-synthesis-lab/)
   - Repository: [GitHub](https://github.com/kamrawr/research-synthesis-lab)

### Assessment & Eligibility Tools (3 External Tools)

1. **Oregon Comprehensive Energy Assessment**
   - Professional-grade assessment tool
   - Detailed sizing calculations
   - Dynamic form fields
   - Precise Energy Trust incentive calculations
   - HVAC load analysis
   - Comprehensive reporting capabilities
   - Link: [Open Tool](https://kamrawr.github.io/oregon-comprehensive-energy-app/)
   - Repository: [GitHub](https://github.com/kamrawr/oregon-comprehensive-energy-app)

2. **Energy Assessment (Simple)**
   - Lightweight, offline-capable
   - Zero dependencies (works without internet)
   - Quick home energy evaluations
   - Instant recommendations
   - ~28KB single-file HTML
   - Link: [Open Tool](https://kamrawr.github.io/dynamic-energy-assessment-tool/standalone_assessment.html)
   - Repository: [GitHub](https://github.com/kamrawr/dynamic-energy-assessment-tool)

3. **Income Eligibility Calculator**
   - 2025 HUD rates for Oregon
   - Multiple income frequencies (annual, monthly, weekly, hourly)
   - Tax status options
   - Visual charts
   - Real-time updates
   - Link: [Open Calculator](https://kamrawr.github.io/oregon-income-calculator/)
   - Repository: [GitHub](https://github.com/kamrawr/oregon-income-calculator)

---

## 🎨 Design Features

### Intuitive Layout
- Clear context section explaining the hub's purpose
- Two organized sections: Resources and Tools
- Clean visual hierarchy with icons and badges
- Color-coded badges (green for resources, orange for tools)

### Responsive Design
- Auto-fit grid: 280px minimum card width
- Mobile-first approach
- Single column on small screens
- Smooth transitions and hover effects

### Compact Cards
- Smaller, more scannable than previous version
- Icon, badge, title, description, and action button
- Secondary "GitHub" links for external tools
- Consistent spacing and typography

### Professional UI/UX
- Modern gradient header
- Subtle shadows and borders
- Smooth hover animations (slight lift effect)
- Energy Trust color scheme (blue primary, green accent)
- Fast load time (~11KB)

---

## 🚀 Quick Deployment

### 1. Review the Page
```bash
# Already opened in your browser
# Test on mobile by resizing browser or using device toolbar
```

### 2. Commit Changes
```bash
cd /Users/isaiah/CPF

# Stage files
git add hub.html HUB-README.md README.md

# Commit
git commit -m "Add CPF Resource Hub - focused, mobile-friendly interface"

# Push
git push origin main
```

### 3. Access Live
After GitHub Pages builds (2-3 minutes):
```
https://kamrawr.github.io/CPF/hub.html
```

### 4. Update Links (Optional)
Consider updating other pages to reference the hub:
- Add link to hub in Document Library header
- Add link to hub in CPF Program Guide
- Add link to hub in Staff Portal

---

## 📊 Technical Details

### File Size
- **hub.html**: ~11KB (self-contained)
- No external CSS/JS dependencies
- Fast load time on any connection

### Browser Support
- All modern browsers (Chrome, Safari, Firefox, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- Responsive breakpoint at 768px

### Accessibility
- Semantic HTML structure
- Clear heading hierarchy (h1 → h2 → h3)
- Sufficient color contrast
- Keyboard navigable
- Screen reader friendly

### Performance
- No external requests (except when clicking links)
- CSS Grid for efficient layout
- Minimal JavaScript (none required)
- Optimized for Core Web Vitals

---

## 🎯 Use Cases

### For Program Staff
- Quick access to all program documentation
- Easy navigation to assessment tools
- Share single link with partners
- Mobile access in the field

### For Community Partners
- Find forms and guides quickly
- Access assessment tools
- Calculate income eligibility
- View contractor opportunities

### For Contractors
- Learn about CPF opportunities
- Access technical specifications
- Download marketing materials
- Use assessment tools with customers

### For Developers
- Clean, maintainable code
- Easy to customize
- Self-contained HTML
- GitHub-ready

---

## 🔧 Customization

### Update Links
All links are in the HTML:
- Internal links: relative paths (e.g., `index.html`)
- External links: absolute URLs with `target="_blank"`

### Change Colors
Modify CSS variables in `:root`:
```css
:root {
    --primary: #0066cc;      /* Primary blue */
    --primary-dark: #004a99; /* Darker blue for hover */
    --accent: #00a651;       /* Green accent */
    --gray-50: #f8f9fa;      /* Background */
}
```

### Add New Cards
Copy existing card structure:
```html
<div class="card">
    <div class="card-icon">🎯</div>
    <span class="badge resource">Resource</span>
    <h3>New Resource</h3>
    <p>Description here</p>
    <a href="link.html" class="card-link">Open →</a>
</div>
```

### Modify Layout
Change grid behavior:
```css
.grid {
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    /* Adjust 280px for different card widths */
}
```

---

## 📱 Mobile Testing

### Recommended Tests
1. Open in mobile Safari/Chrome
2. Test portrait and landscape
3. Verify card grid adjusts
4. Check button sizes (easy to tap)
5. Ensure text is readable

### Responsive Breakpoint
At 768px and below:
- Grid becomes single column
- Header font size reduces
- Section margins adjust

---

## 🔗 Integration Points

### Link from Document Library
Add to `index.html` header:
```html
<a href="hub.html" class="quick-link">
    <span class="quick-link-icon">⚡</span>
    <span class="quick-link-text">Resource Hub</span>
</a>
```

### Link from Other Pages
Add to navigation or footer:
```html
<a href="hub.html">← Back to Resource Hub</a>
```

### Share Link
Primary URL to share with stakeholders:
```
https://kamrawr.github.io/CPF/hub.html
```

---

## 📝 Maintenance

### Regular Updates
- [ ] Verify all links work quarterly
- [ ] Update tool descriptions as features change
- [ ] Add new resources as they're created
- [ ] Keep GitHub repository links current

### When Adding New Pages
1. Create new card in appropriate section
2. Add icon, badge, title, and description
3. Link to the new page
4. Test on mobile
5. Commit and deploy

---

## ✅ Comparison to Previous Version

### Improvements
✅ Focused scope (9 well-organized items)
✅ Better context with intro section
✅ Smaller, more scannable cards
✅ Better mobile experience
✅ Clearer visual hierarchy
✅ More intuitive categorization
✅ Professional Energy Trust branding
✅ Faster load time

### What Changed
- **Added**: Oregon Housing Analysis and Research Synthesis Lab as staff resources
- **Organized**: Clear separation between program resources (6) and assessment tools (3)
- **Improved**: Card size, layout, mobile responsiveness
- **Enhanced**: Contextual intro section, badge system
- **Refined**: Typography, spacing, color scheme
- **Updated**: Oregon Comprehensive Energy App as primary assessment tool

---

## 📄 Files Created

1. **hub.html** (11KB)
   - Main resource hub page
   - Self-contained HTML/CSS
   - No external dependencies

2. **HUB-README.md** (this file)
   - Complete documentation
   - Deployment guide
   - Customization instructions

3. **Updated README.md**
   - Added Resource Hub section
   - Listed all tools and pages
   - Clear navigation structure

---

## 🆘 Support

### Issues?
1. Check that all internal links point to existing files
2. Verify external links are correct
3. Test in different browsers
4. Check mobile responsiveness

### Need Help?
- Review this documentation
- Check the main README.md
- Visit individual tool GitHub repositories

---

## 🏷️ Tags

`energy-efficiency` `cpf-program` `resource-hub` `assessment-tools` `energy-trust` `oregon` `mobile-responsive` `program-management`

---

**Built for Community Consulting Partners LLC**  
Isaiah Kamrar  
[GitHub Profile](https://github.com/kamrawr)

**Last Updated:** October 2025  
**Version:** 2.0 (Refined & Focused)
