# 🚀 Quick Start Guide

## Installation (5 minutes)

### Windows

1. **Open Command Prompt** in your project folder
2. **Create virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard**:
   ```bash
   streamlit run app.py
   ```

### macOS/Linux

1. **Open Terminal** in your project folder
2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard**:
   ```bash
   streamlit run app.py
   ```

## First Steps

1. **Open the dashboard** - Navigate to `http://localhost:8501` in your browser
2. **Explore the data** - Sample data is already loaded
3. **Update with your data** - Replace CSV files in `/data` folder with your own data
4. **Refresh** - Click the refresh button to reload

## Common Tasks

### Adding a New Client

1. Open `data/clients.csv`
2. Add a new row:
   ```csv
   C007,Your Client Name,Industry,Active,2024-02-22,500000,Manager Name
   ```
3. Click refresh on dashboard

### Creating a New Engagement

1. Open `data/engagements.csv`
2. Add engagement (reference client_id and engagement_id):
   ```csv
   E011,C007,New Project,2024-02-22,2024-12-22,In Progress,25,250000,50000
   ```
3. Click refresh

### Tracking Deliverables

1. Open `data/deliverables.csv`
2. Add deliverable entry:
   ```csv
   D015,E011,Project Plan,2024-03-15,,In Progress,
   ```
3. Update when completed

### Monthly Updates

1. Open `data/monthly_summaries.csv`
2. Add monthly summary:
   ```csv
   S009,C007,02,2024,75000,400,4.9,"Project kickoff","None"
   ```

## Tips & Tricks

### Speed Up Loading
- Reduce number of rows in CSV files
- Use the refresh button instead of restarting

### Export Reports
- Go to Reports page
- Select report type
- Click download button

### Track Metrics
- Health Score combines progress, budget, and activity
- Quality scores track deliverable quality (0-100)
- Satisfaction scores show client happiness (0-5)

### Identify Issues
- Check "At-Risk Items" page regularly
- Look for red flags: over-budget, paused, overdue

## Dashboard Navigation

| Page | Purpose |
|------|---------|
| Executive Dashboard | High-level overview |
| Portfolio Overview | Detailed analytics |
| Client Details | Single client deep-dive |
| Engagement Analysis | Project-level metrics |
| Monthly Briefing | Trends and summaries |
| At-Risk Items | Problem identification |
| Reports | Exportable reports |

## Keyboard Shortcuts

- `R` - Refresh data
- `C` - Open command palette (Streamlit)
- `K` - Open keyboard shortcuts

## Troubleshooting

**Dashboard won't open?**
- Check you're using the correct URL: `http://localhost:8501`
- Try restarting: Ctrl+C and run `streamlit run app.py` again

**Data not showing?**
- Verify CSV files are in `/data` folder
- Check column headers match the schema
- Use proper date format: YYYY-MM-DD

**Getting errors?**
- Run `pip install -r requirements.txt` again
- Check Python version: `python --version` (needs 3.8+)

## Next Steps

1. ✅ Install and run dashboard
2. ✅ Explore sample data
3. ✅ Add your client data
4. ✅ Create engagements
5. ✅ Track deliverables
6. ✅ Review reports weekly

## Need Help?

- Check the main README.md for detailed documentation
- Review data file format specifications
- Examine sample CSV files for structure
- Streamlit docs: https://docs.streamlit.io

---

**Happy Dashboarding! 📊**
