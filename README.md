# 📊 Client Portfolio Dashboard

A powerful, zero-database solution for visualizing and analyzing client portfolios using local CSV/JSON files. Perfect for internal visibility, stakeholder presentations, and weekly/monthly briefing summaries.

## ✨ Features

- **Executive Dashboard** - High-level portfolio metrics and KPIs
- **Portfolio Overview** - Industry distribution, budget analysis, and quality metrics
- **Client Details** - Deep dive into individual client information and engagements
- **Engagement Analysis** - Progress tracking, budget utilization, and performance metrics
- **Monthly Briefing** - Revenue trends, hours tracking, and satisfaction scores
- **At-Risk Items** - Quick identification of over-budget, paused, or overdue items
- **Reports** - Health scores, financial summaries, and satisfaction analysis
- **Real-time Data** - Automatic loading from CSV/JSON files in the `/data` directory

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone or download the project**
```bash
cd "investment Counstultant"
```

2. **Create a virtual environment (optional but recommended)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
investment Consultant/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── data/                       # Data files (CSV/JSON)
│   ├── clients.csv            # Client information
│   ├── engagements.csv        # Engagement details
│   ├── deliverables.csv       # Deliverable tracking
│   └── monthly_summaries.csv  # Monthly performance data
│
├── src/                        # Python modules
│   ├── data_loader.py         # CSV/JSON file loading
│   ├── analyzer.py            # Data analysis and calculations
│   └── charts.py              # Visualization components
│
└── reports/                    # Generated reports (optional)
```

## 📊 Data File Formats

### clients.csv
Essential client information and status tracking.

| Field | Type | Description |
|-------|------|-------------|
| client_id | String | Unique identifier |
| client_name | String | Client organization name |
| industry | String | Industry sector |
| status | String | Active, Completed, Paused |
| start_date | Date | Engagement start date (YYYY-MM-DD) |
| contract_value | Float | Total contract value in USD |
| manager | String | Account manager name |

**Example:**
```csv
client_id,client_name,industry,status,start_date,contract_value,manager
C001,Tech Innovations Inc,Technology,Active,2023-01-15,500000,John Smith
```

### engagements.csv
Project/engagement tracking and budget management.

| Field | Type | Description |
|-------|------|-------------|
| engagement_id | String | Unique engagement identifier |
| client_id | String | Associated client |
| engagement_name | String | Project name |
| start_date | Date | Project start date |
| end_date | Date | Project end date |
| status | String | In Progress, Completed, On Hold, Paused |
| progress | Integer | Completion percentage (0-100) |
| budget_allocated | Float | Budget allocated in USD |
| budget_spent | Float | Amount spent so far in USD |

**Example:**
```csv
engagement_id,client_id,engagement_name,start_date,end_date,status,progress,budget_allocated,budget_spent
E001,C001,Digital Transformation,2023-01-15,2024-01-15,Completed,100,150000,148500
```

### deliverables.csv
Track individual deliverables and their quality.

| Field | Type | Description |
|-------|------|-------------|
| deliverable_id | String | Unique identifier |
| engagement_id | String | Associated engagement |
| deliverable_name | String | Deliverable title |
| due_date | Date | Target delivery date |
| completion_date | Date | Actual completion date |
| status | String | Completed, In Progress, Pending, On Hold |
| quality_score | Integer | Quality rating (0-100) |

**Example:**
```csv
deliverable_id,engagement_id,deliverable_name,due_date,completion_date,status,quality_score
D001,E001,Technical Assessment,2023-02-28,2023-02-25,Completed,95
```

### monthly_summaries.csv
Monthly performance metrics and status updates.

| Field | Type | Description |
|-------|------|-------------|
| summary_id | String | Unique identifier |
| client_id | String | Associated client |
| month | Integer | Month (1-12) |
| year | Integer | Year (YYYY) |
| revenue_generated | Float | Revenue in USD |
| hours_spent | Integer | Billable hours |
| satisfaction_score | Float | Client satisfaction (0-5) |
| key_milestones | String | Notable achievements |
| risks | String | Identified risks |

**Example:**
```csv
summary_id,client_id,month,year,revenue_generated,hours_spent,satisfaction_score,key_milestones,risks
S001,C001,01,2024,45000,320,4.8,"Cloud planning started","None"
```

## 🎯 Dashboard Views

### 1. Executive Dashboard
High-level overview with:
- Total clients and active count
- Engagement metrics
- Portfolio contract value
- Client health scores
- Project progress status
- Deliverable completion rates

### 2. Portfolio Overview
Comprehensive analysis including:
- Industry distribution breakdown
- Budget utilization scatter plot
- Quality score distribution
- Performance metrics table

### 3. Client Details
Deep-dive into individual clients:
- Client information and status
- Contract and spending details
- Active engagements list
- Associated deliverables

### 4. Engagement Analysis
Project-level insights:
- Progress tracking
- Budget utilization
- Status filtering
- Performance details

### 5. Monthly Briefing
Trends and performance:
- Revenue trends
- Hours spent analysis
- Client satisfaction trends
- Monthly summary cards
- Key milestones and risks

### 6. At-Risk Items
Quick alerts for:
- Over-budget engagements
- Paused projects
- Overdue deliverables

### 7. Reports
Exportable reports:
- Health score analysis
- Financial summary
- Deliverable status
- Client satisfaction analysis

## 📈 Key Metrics

The dashboard automatically calculates:

### Client Health Score
Composite score based on:
- Project progress (50%)
- Budget efficiency (30%)
- Activity level (20%)

### Budget Utilization
- Percentage of allocated budget spent
- Remaining budget tracking
- Over-budget alerts

### Engagement Performance
- Progress percentage
- Quality score averaging
- Deliverable completion rates
- Timeline adherence

### Portfolio Health
- Total contract value
- Revenue generation
- Client satisfaction trends
- Resource utilization

## 🔄 Updating Data

Simply update the CSV files in the `/data` directory:

1. Edit the CSV files directly or use your favorite spreadsheet application
2. Save the changes
3. Click the "🔄 Refresh Data" button in the dashboard sidebar
4. The dashboard will reload with the latest data

**Note:** CSV files must follow the column structure exactly as shown above.

## 🛠️ Customization

### Adding New Data Fields

1. Add the column to your CSV file
2. Update the `DataLoader` class in `src/data_loader.py` if needed
3. Update the `DataAnalyzer` class to calculate metrics with the new field
4. Add visualizations in `src/charts.py`
5. Update the dashboard views in `app.py`

### Customizing Colors and Styling

Edit color schemes in `src/charts.py`:
```python
color_discrete_map={
    'In Progress': '#3498db',  # Change these hex colors
    'Completed': '#2ecc71',
    'On Hold': '#e74c3c'
}
```

### Adding New Dashboard Views

1. Add a new section in the sidebar navigation in `app.py`
2. Create the view with Streamlit components
3. Use `DashboardCharts` methods for consistency

## 📥 Exporting Data

The Reports page allows downloading:
- Health Score Report (CSV)
- Financial data
- Deliverable information
- Satisfaction metrics

## ⚡ Performance Tips

- The dashboard caches data for 1 hour by default
- Click refresh to immediately reload data
- For large datasets, consider indexing critical columns
- Monthly data is aggregated for better performance

## 🐛 Troubleshooting

### "File not found" Error
- Ensure CSV files are in the `/data` directory
- Check file names match exactly (case-sensitive on some systems)
- Verify CSV headers match the expected format

### Dashboard won't load
- Check all required packages are installed: `pip install -r requirements.txt`
- Ensure Python 3.8+ is installed
- Try clearing cache: Click refresh button or restart app

### Data not updating
- Click the "🔄 Refresh Data" button in the sidebar
- Check CSV file modifications are saved
- Verify date formats are correct (YYYY-MM-DD)

## 📊 Sample Data

The project includes sample data for all CSV files. To reset to sample data:
```bash
# Delete current data files and let the dashboard regenerate them
# Or download fresh sample files from the repository
```

## 🔐 Security Notes

- All data is stored locally - no cloud transmission
- Access the dashboard only on secure networks for sensitive data
- CSV files are plain text - consider encryption for sensitive information
- No user authentication by default - add with Streamlit Secrets if needed

## 📝 License

This project is provided as-is for internal use.

## 🤝 Support & Contributions

For issues, questions, or enhancements:
1. Check the data format matches the schema
2. Review the troubleshooting section
3. Ensure all dependencies are correctly installed

## 📚 Resources

- **Streamlit Docs:** https://docs.streamlit.io/
- **Plotly Charts:** https://plotly.com/python/
- **Pandas Documentation:** https://pandas.pydata.org/docs/

---

**Version:** 1.0.0  
**Last Updated:** February 2026
