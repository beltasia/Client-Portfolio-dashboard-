# 🚀 Deployment & Sharing Guide

Guide for running the dashboard locally and sharing it with stakeholders.

## Local Deployment

### Option 1: Direct Installation (Recommended)

#### Windows
```bash
# 1. Open Command Prompt in project folder
# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run dashboard
streamlit run app.py
```

#### macOS/Linux
```bash
# 1. Open Terminal in project folder
# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run dashboard
streamlit run app.py
```

### Option 2: Using Launch Scripts

#### Windows
```bash
# Simply double-click or run:
run_dashboard.bat
```

#### macOS/Linux
```bash
# Make executable and run:
chmod +x run_dashboard.sh
./run_dashboard.sh
```

### Option 3: One-Command Setup
```bash
# Windows
python setup.py

# Then run:
streamlit run app.py
```

---

## Dashboard Access

### Local Access
- Open browser to: `http://localhost:8501`
- Only accessible from your computer
- No external access

### Network Access
To access from other computers on your network:

1. **Find your IP address:**
   - Windows: `ipconfig` (look for IPv4 Address)
   - macOS/Linux: `ifconfig` (look for inet)

2. **Share URL with team members:**
   ```
   http://<YOUR_IP>:8501
   ```

3. **Example:**
   ```
   http://192.168.1.100:8501
   ```

⚠️ **Note:** Others can only access while dashboard is running

---

## Cloud Deployment

### Option 1: Streamlit Cloud (Free)

**Recommended for sharing dashboards widely**

#### Setup Steps:

1. **Create GitHub account** (if needed)
   - Go to github.com
   - Sign up

2. **Upload project to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

3. **Deploy to Streamlit Cloud**
   - Go to share.streamlit.io
   - Sign in with GitHub
   - Connect your repository
   - Choose main file: `app.py`
   - Click "Deploy"

4. **Access dashboard**
   - URL: `https://yourusername-portfoliodashboard.streamlit.app`
   - Shared with anyone with link
   - 24/7 availability

#### Limitations:
- Free tier has resource limits
- Data must be in repository
- Public or private (with auth)

---

### Option 2: Heroku Deployment

#### Requirements:
- Heroku account (free tier available)
- Git installed

#### Deployment Process:

1. **Create Procfile** in project root:
   ```
   web: streamlit run app.py --server.port=$PORT
   ```

2. **Create requirements.txt** (already exists)

3. **Deploy:**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   heroku open
   ```

4. **Access:**
   - URL: `https://your-app-name.herokuapp.com`
   - Available 24/7

#### Costs:
- Free tier: Limited hours
- Paid tier: $5-50/month

---

### Option 3: AWS Deployment

#### EC2 Instance Setup:

1. **Create EC2 instance**
   - OS: Ubuntu 20.04 or later
   - Instance type: t3.micro (free tier eligible)

2. **Connect via SSH**

3. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip install -r requirements.txt
   ```

4. **Run dashboard**
   ```bash
   streamlit run app.py --server.port 80
   ```

5. **Access**
   - URL: `http://your-ec2-public-ip`

#### Costs:
- Free tier: 1 year free
- After: ~$5-10/month

---

### Option 4: Docker Deployment

#### Dockerfile (create in project root):

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py"]
```

#### Build and run:
```bash
# Build image
docker build -t portfolio-dashboard .

# Run container
docker run -p 8501:8501 portfolio-dashboard

# Access: http://localhost:8501
```

---

## Security Considerations

### For Internal Network Only

✅ Safe deployment options:
- Local machine only
- Closed corporate network
- VPN-only access
- Password-protected network

### For Internet Access

⚠️ Add authentication:

1. **Create secrets.toml:**
   ```toml
   [credentials]
   username = "admin"
   password = "secure_password"
   ```

2. **Add to app.py:**
   ```python
   import streamlit as st

   # Check password
   if not st.session_state.get('authenticated'):
       password = st.text_input("Password:", type="password")
       if password == st.secrets["credentials"]["password"]:
           st.session_state.authenticated = True
       else:
           st.error("Invalid password")
           st.stop()
   ```

3. **Never commit secrets to GitHub**
   - Add to .gitignore
   - Set via environment variables

---

## Maintenance & Monitoring

### Regular Tasks

**Daily:**
- Check dashboard is running
- Verify data is current

**Weekly:**
- Update CSV files
- Review data quality
- Check for errors in logs

**Monthly:**
- Update dependencies: `pip install --upgrade -r requirements.txt`
- Archive old data
- Check storage usage

**Quarterly:**
- Security review
- Performance optimization
- Backup verification

### Restart Dashboard

**If it crashes:**

Windows:
```bash
# Kill process
taskkill /PID <process_id> /F

# Restart
streamlit run app.py
```

macOS/Linux:
```bash
# Kill process
kill -9 <process_id>

# Restart
streamlit run app.py
```

Or simply Ctrl+C and restart.

---

## Troubleshooting Deployment

### "Port already in use" Error
```bash
# Use different port
streamlit run app.py --server.port 8502
```

### "Module not found" Error
```bash
# Install requirements
pip install -r requirements.txt

# Or upgrade
pip install --upgrade -r requirements.txt
```

### "Data files not found" (Cloud)
- Ensure CSV files are in repository
- Check /data folder is pushed to GitHub
- Verify paths in code

### Dashboard loads slowly
- Reduce data file size
- Archive old data
- Increase server resources
- Add caching (already implemented)

### Memory issues
- Reduce data
- Archive old entries
- Increase server RAM (cloud)
- Optimize code

---

## Sharing Best Practices

### For Stakeholders

1. **Send dashboard link** (Streamlit Cloud)
2. **Share read-only** (no editing)
3. **Include instructions**
4. **Provide support contact**

### Example Email:
```
Subject: Client Portfolio Dashboard - Access

Hi Team,

Your portfolio dashboard is ready! Access it here:
https://yourname-portfolio.streamlit.app

Navigation:
- Executive Dashboard: High-level overview
- Portfolio Overview: Detailed metrics
- Client Details: Individual client view
- At-Risk Items: Quick alerts

The dashboard updates automatically when data files are updated.

For questions or issues, contact [your email]

Best regards,
```

### For Data Updates

1. **Weekly updates**
   - Email team: "Data updated - refresh your browser"
   - Show what changed

2. **Major changes**
   - Notify all users
   - Provide summary of changes
   - Schedule Q&A if needed

3. **Version tracking**
   - Keep changelog in README
   - Tag releases on GitHub
   - Version number in app

---

## Performance Optimization

### For Better Speed

1. **Local Caching**
   - Already implemented (1 hour cache)
   - Click refresh to update immediately

2. **Data Optimization**
   - Archive old data
   - Remove unnecessary columns
   - Compress CSV files

3. **Server Optimization (Cloud):**
   - Upgrade server tier
   - Use CDN for static files
   - Implement pagination
   - Add search/filtering

### Load Testing

Check performance:
```bash
# Using ab (Apache Bench)
ab -n 100 -c 10 http://localhost:8501

# Or using wrk
wrk -t4 -c100 -d30s http://localhost:8501
```

---

## Backup & Recovery

### Backup Strategy

**Local backup (weekly):**
```bash
# Windows
xcopy data backups\%date:~-4,4%%date:~-10,2%%date:~-7,2% /E /I /Y

# macOS/Linux
cp -r data backups/$(date +%Y%m%d)
```

**GitHub backup (automatic):**
- Push to GitHub regularly
- Commits serve as version history

### Recovery

1. Stop dashboard
2. Restore CSV files from backup
3. Restart dashboard
4. Click refresh

---

## Scaling Strategy

### If Dashboard Gets Slow

1. **Check data size**
   ```bash
   # Check file size
   ls -lh data/*.csv
   ```

2. **Archive old data**
   - Move 1+ year old to archive folder
   - Keep last 12-24 months active

3. **Add indexes**
   - Modify analyzer.py
   - Pre-calculate metrics

4. **Upgrade server**
   - More RAM
   - Better CPU
   - Paid tier on Streamlit Cloud

---

## Updates & Maintenance

### Updating Dependencies
```bash
pip install --upgrade -r requirements.txt
streamlit run app.py
```

### Adding New Features

1. Create feature branch: `git checkout -b feature-name`
2. Add code
3. Test locally
4. Commit: `git commit -m "Add feature"`
5. Push: `git push origin feature-name`
6. Create pull request
7. Merge to main
8. Redeploy

### Version Control

Tag releases:
```bash
git tag -a v1.0.1 -m "Add new chart"
git push origin v1.0.1
```

---

## Support Resources

### Documentation
- Streamlit: https://docs.streamlit.io/
- Plotly: https://plotly.com/python/
- Pandas: https://pandas.pydata.org/docs/

### Communities
- Stack Overflow: #streamlit
- GitHub Discussions
- Streamlit Forum

### Troubleshooting
- Check logs: `streamlit run app.py --logger.level=debug`
- Review errors in browser console (F12)
- Check dashboard health status

---

**Version:** 1.0.0  
**Last Updated:** February 2024

For questions or issues, refer to README.md or open an issue on GitHub.
