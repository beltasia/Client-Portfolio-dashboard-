# 📊 Data Management Guide

Complete guide for managing your portfolio data in the dashboard.

## File Locations

All data files must be in the `data/` directory:

```
investment Consultant/
├── data/
│   ├── clients.csv              # Client master data
│   ├── engagements.csv          # Project/engagement tracking
│   ├── deliverables.csv         # Deliverable items
│   └── monthly_summaries.csv    # Monthly performance data
```

## Data File Specifications

### 1. clients.csv

**Purpose:** Master list of all clients

**Required Columns:**
| Column | Type | Format | Required | Notes |
|--------|------|--------|----------|-------|
| client_id | String | C001, C002, etc | Yes | Unique identifier |
| client_name | String | Text | Yes | Organization name |
| industry | String | Text | Yes | Business sector |
| status | String | Active\|Completed\|Paused | Yes | Current status |
| start_date | Date | YYYY-MM-DD | Yes | Engagement start |
| contract_value | Number | Integer | Yes | Total contract value (USD) |
| manager | String | Text | Yes | Account manager name |

**Example:**
```csv
client_id,client_name,industry,status,start_date,contract_value,manager
C001,Tech Innovations Inc,Technology,Active,2023-01-15,500000,John Smith
C002,Global Finance Corp,Financial Services,Active,2023-03-20,750000,Sarah Johnson
C003,Retail Plus LLC,Retail,Completed,2023-06-10,320000,Mike Chen
```

**Validation Rules:**
- client_id must be unique
- contract_value must be > 0
- date must be in YYYY-MM-DD format
- status must be one of: Active, Completed, Paused

---

### 2. engagements.csv

**Purpose:** Track projects/engagements for clients

**Required Columns:**
| Column | Type | Format | Required | Notes |
|--------|------|--------|----------|-------|
| engagement_id | String | E001, E002, etc | Yes | Unique identifier |
| client_id | String | C001, etc | Yes | Reference to client |
| engagement_name | String | Text | Yes | Project name |
| start_date | Date | YYYY-MM-DD | Yes | Project start |
| end_date | Date | YYYY-MM-DD | Yes | Project end |
| status | String | In Progress\|Completed\|On Hold\|Paused | Yes | Current status |
| progress | Number | 0-100 | Yes | % completion |
| budget_allocated | Number | Integer | Yes | Allocated budget (USD) |
| budget_spent | Number | Integer | Yes | Amount spent (USD) |

**Example:**
```csv
engagement_id,client_id,engagement_name,start_date,end_date,status,progress,budget_allocated,budget_spent
E001,C001,Digital Transformation,2023-01-15,2024-01-15,Completed,100,150000,148500
E002,C001,Cloud Migration,2024-02-01,2024-12-31,In Progress,75,200000,165000
E003,C002,Risk Assessment Framework,2023-03-20,2023-09-20,Completed,100,100000,99500
```

**Validation Rules:**
- engagement_id must be unique
- client_id must exist in clients.csv
- end_date must be >= start_date
- progress must be 0-100
- budget_spent must be <= budget_allocated (can be over if flagged as at-risk)
- status must match allowed values

**Budget Alerts:**
- 🟡 Yellow: 80-99% of budget used
- 🔴 Red: 100%+ of budget used

---

### 3. deliverables.csv

**Purpose:** Track individual deliverables within engagements

**Required Columns:**
| Column | Type | Format | Required | Notes |
|--------|------|--------|----------|-------|
| deliverable_id | String | D001, D002, etc | Yes | Unique identifier |
| engagement_id | String | E001, etc | Yes | Reference to engagement |
| deliverable_name | String | Text | Yes | Deliverable title |
| due_date | Date | YYYY-MM-DD | Yes | Target delivery date |
| completion_date | Date | YYYY-MM-DD | No | Actual completion date |
| status | String | Completed\|In Progress\|Pending\|On Hold | Yes | Current status |
| quality_score | Number | 0-100 | No | Quality rating (null if not completed) |

**Example:**
```csv
deliverable_id,engagement_id,deliverable_name,due_date,completion_date,status,quality_score
D001,E001,Technical Assessment Report,2023-02-28,2023-02-25,Completed,95
D002,E001,Architecture Design,2023-04-15,2023-04-18,Completed,92
D005,E002,Migration Strategy,2024-05-15,,In Progress,
D010,E006,Inventory Analysis,2024-04-15,,In Progress,
```

**Validation Rules:**
- deliverable_id must be unique
- engagement_id must exist in engagements.csv
- completion_date can be null (for incomplete items)
- quality_score should only be set if status is "Completed"
- completion_date should be <= due_date for on-time delivery

**Status Meanings:**
- **Completed**: Delivered and accepted
- **In Progress**: Currently being worked on
- **Pending**: Not yet started
- **On Hold**: Blocked or paused

---

### 4. monthly_summaries.csv

**Purpose:** Monthly performance summaries per client

**Required Columns:**
| Column | Type | Format | Required | Notes |
|--------|------|--------|----------|-------|
| summary_id | String | S001, S002, etc | Yes | Unique identifier |
| client_id | String | C001, etc | Yes | Reference to client |
| month | Number | 1-12 | Yes | Month number |
| year | Number | YYYY | Yes | Year |
| revenue_generated | Number | Integer | Yes | Revenue in USD |
| hours_spent | Number | Integer | Yes | Billable hours |
| satisfaction_score | Number | 0-5 | Yes | Client satisfaction (decimals allowed) |
| key_milestones | String | Text | Yes | Notable achievements |
| risks | String | Text | Yes | Identified risks |

**Example:**
```csv
summary_id,client_id,month,year,revenue_generated,hours_spent,satisfaction_score,key_milestones,risks
S001,C001,01,2024,45000,320,4.8,"Cloud planning started","None"
S002,C001,02,2024,52000,380,4.7,"Architecture finalized","Schedule delay risk"
S003,C002,01,2024,35000,240,4.9,"Compliance audit completed","None"
```

**Validation Rules:**
- summary_id must be unique
- client_id must exist in clients.csv
- month must be 1-12
- year must be valid (e.g., 2024)
- revenue_generated must be >= 0
- hours_spent must be >= 0
- satisfaction_score must be 0-5
- One entry per client per month

---

## Common Data Updates

### Weekly Updates

Update progress on active engagements:

```csv
engagement_id,client_id,engagement_name,start_date,end_date,status,progress,budget_allocated,budget_spent
E002,C001,Cloud Migration,2024-02-01,2024-12-31,In Progress,80,200000,175000
```

Update deliverable progress:

```csv
deliverable_id,engagement_id,deliverable_name,due_date,completion_date,status,quality_score
D005,E002,Migration Strategy,2024-05-15,2024-05-14,Completed,94
```

### Monthly Updates

Add end-of-month summary:

```csv
summary_id,client_id,month,year,revenue_generated,hours_spent,satisfaction_score,key_milestones,risks
S004,C001,03,2024,48000,360,4.8,"Migration 75% complete","Resource constraints"
```

### Quarterly Updates

Review and update client status:

```csv
client_id,client_name,industry,status,start_date,contract_value,manager
C001,Tech Innovations Inc,Technology,Active,2023-01-15,500000,John Smith
```

### New Client Onboarding

1. Add client row to clients.csv
2. Create engagement entry in engagements.csv
3. Initialize deliverables in deliverables.csv
4. Add first monthly summary
5. Click refresh in dashboard

---

## Data Quality Checks

### Before Submitting Data

✅ **Dates**
- All dates in YYYY-MM-DD format
- End dates >= start dates
- Completion dates <= due dates

✅ **Numbers**
- Budget values are positive integers
- Progress is 0-100
- Satisfaction is 0-5
- Quality scores are 0-100 (or blank)

✅ **References**
- All client_ids exist in clients.csv
- All engagement_ids exist in engagements.csv
- All deliverable engagement_ids exist
- All summary client_ids exist

✅ **Status Values**
- Clients: Active, Completed, Paused
- Engagements: In Progress, Completed, On Hold, Paused
- Deliverables: Completed, In Progress, Pending, On Hold

✅ **Completeness**
- No required columns are empty
- Quality scores only when Completed
- Completion dates only when Completed

---

## Data Entry Tools

### Option 1: Direct CSV Editing
- Use Excel, Google Sheets, or any text editor
- Maintain CSV format (comma-separated)
- Save as CSV (not XLSX)

### Option 2: Google Sheets
1. Create sheet with same structure
2. Export as CSV
3. Save in `/data` folder
4. Click refresh

### Option 3: Excel
1. Create workbook
2. Format columns as required
3. Save as CSV (File > Save As > CSV)
4. Save in `/data` folder

### Option 4: Python Script
```python
import pandas as pd

# Create data
data = {
    'client_id': ['C001', 'C002'],
    'client_name': ['Client A', 'Client B'],
    # ... more columns
}

# Save
df = pd.DataFrame(data)
df.to_csv('data/clients.csv', index=False)
```

---

## Data Backup & Recovery

### Backup Strategy

1. **Weekly Backup**
   - Copy entire `/data` folder
   - Store in backup location
   - Keep last 4 weeks

2. **Monthly Archive**
   - Export to external drive
   - Store with month/year label
   - Keep for 12+ months

### Backup Script (Windows)
```batch
@echo off
set backupdir=backups\%date:~-4,4%%date:~-10,2%%date:~-7,2%
mkdir %backupdir%
xcopy data %backupdir%\data /E /I /Y
echo Backup completed to %backupdir%
```

### Recovery

1. Stop dashboard (Ctrl+C)
2. Restore CSV files from backup
3. Click refresh button
4. Verify data is restored

---

## CSV Formatting Tips

### Proper Format
```csv
client_id,client_name,industry,status,start_date,contract_value,manager
C001,Tech Innovations Inc,Technology,Active,2023-01-15,500000,John Smith
```

### Text with Commas (Use Quotes)
```csv
client_id,client_name,industry,status,start_date,contract_value,manager
C001,"Smith, Johnson & Co",Technology,Active,2023-01-15,500000,John Smith
```

### Dates in Text Fields
```csv
client_id,client_name,notes
C001,Tech Corp,"Started 2023-01-15, ended 2024-01-15"
```

### Empty Fields
```csv
deliverable_id,engagement_id,deliverable_name,due_date,completion_date,status,quality_score
D001,E001,Report,2024-03-15,,In Progress,
```

---

## Performance Optimization

### For Large Datasets

1. **Archive Old Data**
   - Keep current year + 1 previous
   - Archive older data separately

2. **Reduce Columns**
   - Only include necessary fields
   - Remove notes if very large

3. **Optimize Updates**
   - Batch updates weekly
   - Avoid real-time updates

4. **File Size**
   - Keep files under 10MB
   - 1000+ rows may slow performance

---

## Data Privacy & Security

### Sensitive Information
- Remove actual names (use generic)
- Round numbers for examples
- Don't share dashboard link with sensitive data

### File Protection
- Store in secure location
- Restrict access to authorized users
- Consider encryption for local files

### Shared Drives
- Use read-only mode when sharing
- Export specific reports instead
- Restrict to dashboar link only

---

## Troubleshooting Data Issues

### "File not found" Error
✓ Check file is in `/data` folder
✓ Check exact filename spelling
✓ Ensure .csv extension

### "Invalid data format" Error
✓ Check date format (YYYY-MM-DD)
✓ Check status values exactly match
✓ Verify numbers (no $ or commas)

### Data not updating in dashboard
✓ Click refresh button
✓ Check file was saved
✓ Restart streamlit if needed

### Calculations look wrong
✓ Verify all reference IDs exist
✓ Check for duplicate IDs
✓ Validate numeric values

---

## Import/Export Guide

### Export from Dashboard
1. Go to Reports page
2. Select report type
3. Click "Download as CSV"
4. File downloads to Downloads folder

### Import from Excel
1. Open Excel file
2. Select all data
3. Save As → CSV Format
4. Place in `/data` folder
5. Click refresh

### Bulk Updates
1. Download current CSV
2. Update in Excel
3. Save as CSV
4. Replace original
5. Click refresh

---

## Support & Questions

For data format questions:
- Check schema in README.md
- Review EXAMPLES.md for samples
- Examine existing CSV files
- Ensure all validation rules pass

---

**Last Updated:** February 2024  
**Version:** 1.0.0
