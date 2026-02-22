# Dashboard Configuration

# Data settings
DATA_DIR = "data"
CACHE_TTL = 3600  # Cache timeout in seconds (1 hour)

# Display settings
THEME = "light"
DEFAULT_PAGE = "Executive Dashboard"
SIDEBAR_STATE = "expanded"

# Chart settings
CHART_HEIGHT = 400
CHART_COLORS = {
    'primary': '#1f77b4',
    'success': '#2ecc71',
    'warning': '#f39c12',
    'danger': '#e74c3c',
    'info': '#3498db',
    'secondary': '#95a5a6'
}

# Status colors
STATUS_COLORS = {
    'Active': '#2ecc71',
    'Completed': '#95a5a6',
    'Paused': '#e74c3c',
    'In Progress': '#3498db',
    'Pending': '#f39c12',
    'On Hold': '#e74c3c'
}

# Metrics calculations
HEALTH_SCORE_WEIGHTS = {
    'progress': 0.5,
    'budget_efficiency': 0.3,
    'activity': 0.2
}

# Date format
DATE_FORMAT = "%Y-%m-%d"
DISPLAY_DATE_FORMAT = "%B %d, %Y"

# Refresh interval (minutes)
AUTO_REFRESH_INTERVAL = 60
