# Dashboard Screenshots

Visual previews of the Client Portfolio Dashboard pages.

## Capturing Screenshots

Follow these steps to capture and add dashboard screenshots:

### Quick Screenshot Guide

1. **Open the dashboard** at `http://localhost:8501` (if not already open)
2. **For each page**, take a screenshot:
   - Press `Windows + Shift + S` to take a screenshot (Windows 10/11)
   - Or use `Print Screen` and paste into an image editor
   - Or use Streamlit's share button (top-right menu)

### Pages to Screenshot

Capture each of these pages and save with the filenames below:

1. **01_executive_dashboard.png**
   - Main overview with 5 key metrics
   - 4 charts (health, progress, deliverables, status)

2. **02_portfolio_overview.png**
   - Industry distribution pie chart
   - Budget utilization scatter plot
   - Quality metrics histogram
   - Engagement performance table

3. **03_client_details.png**
   - Client selector dropdown
   - Client metrics (status, industry, manager, contract value)
   - Active engagements table
   - Deliverables table

4. **04_engagement_analysis.png**
   - Engagement progress chart
   - Budget utilization chart
   - Status filter multiselect
   - Progress slider
   - Filtered engagements table

5. **05_monthly_briefing.png**
   - Monthly revenue chart
   - Hours spent chart
   - Satisfaction trend chart
   - Monthly summary expandable cards
   - Monthly metrics table

6. **06_at_risk_items.png**
   - Over budget engagements section
   - Paused engagements section
   - Overdue deliverables section

7. **07_reports.png**
   - Reports dropdown selector
   - Sample of one report view (e.g., Health Score Report)

## Screenshot Format

- **Format:** PNG or JPEG
- **Resolution:** 1024x768 or higher
- **Include:** Full dashboard view with navigation sidebar
- **Naming:** Use the `XX_page_name.png` format above

## Using Git to Add Screenshots

After capturing screenshots, save them to this folder and commit:

```bash
git add screenshots/
git commit -m "Add dashboard screenshots"
git push
```

## Display in README

Once added, reference screenshots in the main `README.md`:

```markdown
## Dashboard Screenshots

### Executive Dashboard
![Executive Dashboard](screenshots/01_executive_dashboard.png)

### Portfolio Overview
![Portfolio Overview](screenshots/02_portfolio_overview.png)

[...continue for all pages...]
```

