# 🚀 Deployment Guide - Program Management Center

This guide will help you deploy the Program Management Center to GitHub Pages.

## Quick Deployment Steps

### 1. Commit the New Files

```bash
cd /Users/isaiah/CPF

# Stage the new files
git add program-management-center.html
git add PMC-README.md
git add DEPLOYMENT.md

# Commit
git commit -m "Add Program Management Center - unified hub for all projects"

# Push to GitHub
git push origin main
```

### 2. Enable GitHub Pages

1. Go to your CPF repository on GitHub
2. Click **Settings** (gear icon)
3. Scroll down to **Pages** section in the left sidebar
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**

### 3. Access Your Site

After a few minutes, your site will be live at:
```
https://kamrawr.github.io/CPF/program-management-center.html
```

### 4. Set as Homepage (Optional)

To make the Program Management Center your repository homepage:

**Option A: Rename File**
```bash
# Backup current index
mv index.html cpf-document-library.html

# Make PMC the new index
cp program-management-center.html index.html

# Update links in PMC
sed -i '' 's/index.html/cpf-document-library.html/g' index.html

git add .
git commit -m "Set Program Management Center as homepage"
git push origin main
```

**Option B: Update Repository Settings**
1. Go to repository Settings
2. Under **Pages**, once deployed, you'll see the URL
3. Copy this URL
4. Go back to main repository page
5. Click the gear icon next to "About"
6. Paste the URL with `/program-management-center.html`
7. Save changes

## Verify Deployment

Check these items after deployment:

- [ ] Main hub page loads correctly
- [ ] All internal links work (CPF docs, program guide, etc.)
- [ ] External links to other GitHub Pages work
- [ ] Filtering functionality works
- [ ] Mobile responsive design displays correctly
- [ ] Stats dashboard is visible

## Update External Projects

For each external project repository, update the README to include a link back to the Program Management Center:

### Example Addition to External READMEs

```markdown
## 🏛️ Part of Program Management Center

This project is part of the [Program Management Center](https://kamrawr.github.io/CPF/program-management-center.html), a comprehensive hub for energy efficiency program tools, research, and data analytics.

**Other Projects:**
- [Research Synthesis Lab](https://kamrawr.github.io/research-synthesis-lab/)
- [Oregon Housing Analysis](https://kamrawr.github.io/oregon-housing-analysis/)
- [Oregon Energy Assessment Tools](https://kamrawr.github.io/oregon-energy-assessment-advanced/)
- [Oregon Income Calculator](https://kamrawr.github.io/oregon-income-calculator/)
- [CPF Document Library](https://kamrawr.github.io/CPF/)
```

## Troubleshooting

### Links Not Working

If internal links (to index.html, cpf-program-guide.html, etc.) don't work:

1. Verify the files exist in your repository
2. Check that file names match exactly (case-sensitive)
3. Ensure all files are committed and pushed

### External Links 404

If links to other GitHub Pages repos show 404:

1. Verify each external repo has GitHub Pages enabled
2. Check that the URLs in `program-management-center.html` are correct
3. Ensure external repos are public

### Styling Issues

If the page doesn't look right:

1. Check browser console for errors
2. Verify all CSS is embedded in the HTML (no external stylesheets needed)
3. Test in different browsers

### Mobile Display Issues

1. Test responsive design at different breakpoints
2. Check viewport meta tag is present
3. Verify media queries are working

## Custom Domain (Optional)

To use a custom domain:

1. Purchase domain from registrar
2. Add CNAME file to repository root:
   ```bash
   echo "your-domain.com" > CNAME
   git add CNAME
   git commit -m "Add custom domain"
   git push origin main
   ```
3. Configure DNS at your registrar:
   - Add A records pointing to GitHub's IPs:
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153
   - Or add CNAME record pointing to `kamrawr.github.io`

4. Wait for DNS propagation (can take 24-48 hours)

## Maintenance

### Adding New Projects

1. Open `program-management-center.html`
2. Find the `<div class="project-grid">` section
3. Copy an existing project card
4. Modify the content:
   - Update icon, title, description
   - Change `data-category` attribute
   - Update links and metadata
   - Adjust project type badge
5. Update stats if needed
6. Commit and push changes

### Updating Project Info

When a project gets updated:

1. Edit the relevant project card in `program-management-center.html`
2. Update descriptions, links, or stats
3. Keep PMC-README.md in sync with major changes
4. Commit and push

### Regular Maintenance Tasks

- [ ] Quarterly: Review all links and verify they work
- [ ] Quarterly: Update statistics (document counts, study counts, etc.)
- [ ] Annually: Review project descriptions for accuracy
- [ ] Annually: Update data source versions (AMI data, etc.)
- [ ] As needed: Add new projects or tools

## Analytics (Optional)

To track page views, add Google Analytics or similar:

1. Sign up for Google Analytics
2. Get your tracking ID
3. Add tracking code before `</head>` in `program-management-center.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

4. Commit and push changes

## Backup Strategy

Recommended backup approach:

1. **Git History:** All changes are tracked in git
2. **GitHub:** Acts as remote backup
3. **Local Copies:** Keep local repository updated
4. **Export:** Periodically export key HTML files to separate backup location

```bash
# Create backup
mkdir -p ~/Backups/CPF-$(date +%Y%m%d)
cp program-management-center.html ~/Backups/CPF-$(date +%Y%m%d)/
cp PMC-README.md ~/Backups/CPF-$(date +%Y%m%d)/
```

## Support

If you encounter issues:

1. Check this deployment guide
2. Review GitHub Pages documentation
3. Check GitHub status page for outages
4. Review git history for recent changes
5. Test locally by opening HTML file directly

## Next Steps

After successful deployment:

- [ ] Share the Program Management Center URL with stakeholders
- [ ] Add link to your professional profiles (LinkedIn, resume, etc.)
- [ ] Update each external project README to reference the PMC
- [ ] Consider creating social media posts announcing the launch
- [ ] Add the PMC link to your email signature
- [ ] Create a blog post or case study about the integrated platform

---

**Questions or Issues?**  
Review the PMC-README.md for more details about the project structure and features.

**Last Updated:** October 2025
