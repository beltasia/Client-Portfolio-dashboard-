import streamlit as st
import pandas as pd
from datetime import datetime
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from data_loader import DataLoader
from analyzer import DataAnalyzer
from charts import DashboardCharts

# Page configuration
st.set_page_config(
    page_title="Client Portfolio Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styling
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .metric-value {
        font-size: 32px;
        font-weight: bold;
        color: #1f77b4;
    }
    .metric-label {
        font-size: 14px;
        color: #666;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize data loader
@st.cache_resource
def get_data_loader():
    return DataLoader(data_dir="data")

@st.cache_data(ttl=3600)
def load_all_data():
    loader = get_data_loader()
    return {
        'clients': loader.get_clients(),
        'engagements': loader.get_engagements(),
        'deliverables': loader.get_deliverables(),
        'summaries': loader.get_monthly_summaries()
    }

# Load data
try:
    data = load_all_data()
    analyzer = DataAnalyzer(
        data['clients'],
        data['engagements'],
        data['deliverables'],
        data['summaries']
    )
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.info("Make sure all CSV files are in the 'data' directory")
    st.stop()

# Sidebar navigation
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Select View",
    ["Executive Dashboard", "Portfolio Overview", "Client Details", "Engagement Analysis", 
     "Monthly Briefing", "At-Risk Items", "Reports"]
)

st.sidebar.divider()
st.sidebar.write(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
if st.sidebar.button("🔄 Refresh Data"):
    st.cache_data.clear()
    st.rerun()

# ==================== EXECUTIVE DASHBOARD ====================
if page == "Executive Dashboard":
    st.title("📈 Executive Dashboard")
    st.write("High-level portfolio overview and key metrics")
    
    # Get portfolio summary
    summary = analyzer.get_portfolio_summary()
    
    # Key metrics row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            "Total Clients",
            summary['total_clients'],
            delta=f"{summary['active_clients']} Active"
        )
    
    with col2:
        st.metric(
            "Total Engagements",
            summary['total_engagements'],
            delta=f"{summary['active_engagements']} Active"
        )
    
    with col3:
        st.metric(
            "Portfolio Value",
            f"${summary['total_contract_value']:,.0f}",
            delta="USD"
        )
    
    with col4:
        st.metric(
            "Completed Engagements",
            summary['completed_engagements'],
            delta=f"{(summary['completed_engagements']/summary['total_engagements']*100):.0f}%"
        )
    
    with col5:
        st.metric(
            "Avg Progress",
            f"{summary['average_progress']:.0f}%",
            delta="Active Projects"
        )
    
    st.divider()
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(
            DashboardCharts.client_health_chart(analyzer.get_client_health()),
            use_container_width=True,
            key="health_chart"
        )
    
    with col2:
        st.plotly_chart(
            DashboardCharts.engagement_progress_chart(analyzer.get_engagement_performance()),
            use_container_width=True,
            key="progress_chart"
        )
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.plotly_chart(
            DashboardCharts.deliverable_status_chart(data['deliverables']),
            use_container_width=True,
            key="deliverable_chart"
        )
    
    with col4:
        st.plotly_chart(
            DashboardCharts.client_status_breakdown(data['clients']),
            use_container_width=True,
            key="status_chart"
        )

# ==================== PORTFOLIO OVERVIEW ====================
elif page == "Portfolio Overview":
    st.title("🎯 Portfolio Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.plotly_chart(
            DashboardCharts.industry_distribution_chart(data['clients']),
            use_container_width=True,
            key="industry_chart"
        )
    
    with col2:
        st.plotly_chart(
            DashboardCharts.budget_utilization_chart(analyzer.get_engagement_performance()),
            use_container_width=True,
            key="budget_chart"
        )
    
    with col3:
        st.plotly_chart(
            DashboardCharts.quality_metrics_chart(data['deliverables']),
            use_container_width=True,
            key="quality_chart"
        )
    
    st.divider()
    
    # Performance table
    st.subheader("📋 Engagement Performance Details")
    perf_data = analyzer.get_engagement_performance()
    display_cols = ['engagement_id', 'engagement_name', 'status', 'progress', 
                    'budget_utilization_pct', 'avg_quality_score', 'deliverable_completion_pct']
    
    st.dataframe(
        perf_data[display_cols].sort_values('progress', ascending=False),
        use_container_width=True,
        hide_index=True
    )

# ==================== CLIENT DETAILS ====================
elif page == "Client Details":
    st.title("👥 Client Details")
    
    # Client selector
    client_list = data['clients'].sort_values('client_name')
    selected_client = st.selectbox(
        "Select a Client",
        client_list['client_id'],
        format_func=lambda x: f"{data['clients'][data['clients']['client_id']==x]['client_name'].values[0]} ({x})"
    )
    
    # Get client summary
    client_summary = analyzer.get_client_summary(selected_client)
    client_info = client_summary['client']
    
    # Client info
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Status", client_info['status'])
    with col2:
        st.metric("Industry", client_info['industry'])
    with col3:
        st.metric("Manager", client_info['manager'])
    with col4:
        st.metric("Start Date", client_info['start_date'].strftime('%Y-%m-%d'))
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Contract Value", f"${client_info['contract_value']:,.0f}")
    with col2:
        st.metric("Total Allocated", f"${client_summary['total_allocated']:,.0f}")
    with col3:
        st.metric("Total Spent", f"${client_summary['total_spent']:,.0f}")
    
    st.divider()
    
    # Engagements
    st.subheader("📌 Active Engagements")
    engagements_df = pd.DataFrame(client_summary['engagements'])
    if not engagements_df.empty:
        st.dataframe(
            engagements_df[['engagement_id', 'engagement_name', 'status', 'progress', 'budget_allocated', 'budget_spent']],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No engagements for this client")
    
    # Deliverables
    st.subheader("✅ Deliverables")
    deliverables_df = pd.DataFrame(client_summary['deliverables'])
    if not deliverables_df.empty:
        st.dataframe(
            deliverables_df[['deliverable_id', 'deliverable_name', 'status', 'due_date', 'quality_score']],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No deliverables for this client")

# ==================== ENGAGEMENT ANALYSIS ====================
elif page == "Engagement Analysis":
    st.title("🔍 Engagement Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(
            DashboardCharts.engagement_progress_chart(analyzer.get_engagement_performance()),
            use_container_width=True,
            key="eng_progress"
        )
    
    with col2:
        st.plotly_chart(
            DashboardCharts.budget_utilization_chart(analyzer.get_engagement_performance()),
            use_container_width=True,
            key="eng_budget"
        )
    
    st.divider()
    
    # Filter options
    col1, col2 = st.columns(2)
    
    with col1:
        status_filter = st.multiselect(
            "Filter by Status",
            data['engagements']['status'].unique(),
            default=data['engagements']['status'].unique()
        )
    
    with col2:
        min_progress = st.slider("Minimum Progress (%)", 0, 100, 0)
    
    # Filtered table
    filtered_eng = data['engagements'][
        (data['engagements']['status'].isin(status_filter)) &
        (data['engagements']['progress'] >= min_progress)
    ]
    
    st.subheader("Engagement Details")
    st.dataframe(
        filtered_eng.sort_values('progress', ascending=False),
        use_container_width=True,
        hide_index=True
    )

# ==================== MONTHLY BRIEFING ====================
elif page == "Monthly Briefing":
    st.title("📅 Monthly Briefing")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(
            DashboardCharts.monthly_revenue_chart(analyzer.get_monthly_trends()),
            use_container_width=True,
            key="revenue"
        )
    
    with col2:
        st.plotly_chart(
            DashboardCharts.hours_spent_chart(analyzer.get_monthly_trends()),
            use_container_width=True,
            key="hours"
        )
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.plotly_chart(
            DashboardCharts.satisfaction_trend_chart(analyzer.get_monthly_trends()),
            use_container_width=True,
            key="satisfaction"
        )
    
    with col4:
        st.subheader("📊 Monthly Summary")
        summaries = analyzer.get_monthly_trends().sort_values('date', ascending=False)
        
        for idx, row in summaries.head(3).iterrows():
            with st.expander(f"{int(row['month'])}/{int(row['year'])} - {row['client_id']}"):
                col_a, col_b, col_c = st.columns(3)
                col_a.metric("Revenue", f"${row['revenue_generated']:,.0f}")
                col_b.metric("Hours", f"{int(row['hours_spent'])}")
                col_c.metric("Satisfaction", f"{row['satisfaction_score']:.1f}/5.0")
                st.write(f"**Milestones:** {row['key_milestones']}")
                st.write(f"**Risks:** {row['risks']}")
    
    st.divider()
    
    # Summary table
    st.subheader("Monthly Metrics")
    st.dataframe(
        analyzer.get_monthly_trends().sort_values('date', ascending=False),
        use_container_width=True,
        hide_index=True
    )

# ==================== AT-RISK ITEMS ====================
elif page == "At-Risk Items":
    st.title("⚠️ At-Risk Items")
    
    at_risk = analyzer.get_at_risk_items()
    
    # Over budget
    st.subheader("🔴 Over Budget Engagements")
    if at_risk['over_budget_engagements']:
        over_budget_df = pd.DataFrame(at_risk['over_budget_engagements'])
        st.dataframe(over_budget_df, use_container_width=True, hide_index=True)
    else:
        st.success("✅ No over-budget engagements!")
    
    st.divider()
    
    # Paused engagements
    st.subheader("⏸️ Paused Engagements")
    if at_risk['paused_engagements']:
        paused_df = pd.DataFrame(at_risk['paused_engagements'])
        st.dataframe(paused_df, use_container_width=True, hide_index=True)
    else:
        st.success("✅ No paused engagements!")
    
    st.divider()
    
    # Overdue deliverables
    st.subheader("📅 Overdue Deliverables")
    if at_risk['at_risk_deliverables']:
        overdue_df = pd.DataFrame(at_risk['at_risk_deliverables'])
        st.dataframe(overdue_df, use_container_width=True, hide_index=True)
    else:
        st.success("✅ No overdue deliverables!")

# ==================== REPORTS ====================
elif page == "Reports":
    st.title("📄 Reports")
    
    report_type = st.selectbox(
        "Select Report Type",
        ["Health Score Report", "Financial Summary", "Deliverable Status", "Client Satisfaction"]
    )
    
    if report_type == "Health Score Report":
        st.subheader("Client Health Scores")
        health_data = analyzer.get_client_health()
        
        st.plotly_chart(
            DashboardCharts.client_health_chart(health_data),
            use_container_width=True,
            key="health_report"
        )
        
        st.dataframe(health_data, use_container_width=True, hide_index=True)
        
        if st.button("📥 Download Health Report"):
            csv = health_data.to_csv(index=False)
            st.download_button(
                label="Download as CSV",
                data=csv,
                file_name=f"health_report_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
    
    elif report_type == "Financial Summary":
        st.subheader("Financial Overview")
        
        col1, col2, col3 = st.columns(3)
        total_contract = data['clients']['contract_value'].sum()
        total_spent = data['engagements']['budget_spent'].sum()
        total_allocated = data['engagements']['budget_allocated'].sum()
        
        with col1:
            st.metric("Total Contract Value", f"${total_contract:,.0f}")
        with col2:
            st.metric("Total Allocated", f"${total_allocated:,.0f}")
        with col3:
            st.metric("Total Spent", f"${total_spent:,.0f}")
        
        st.divider()
        
        st.plotly_chart(
            DashboardCharts.monthly_revenue_chart(analyzer.get_monthly_trends()),
            use_container_width=True,
            key="financial_revenue"
        )
        
        # Financial table
        fin_data = analyzer.get_engagement_performance()[['engagement_id', 'engagement_name', 'budget_allocated', 'budget_spent', 'budget_utilization_pct']]
        st.dataframe(fin_data, use_container_width=True, hide_index=True)
    
    elif report_type == "Deliverable Status":
        st.subheader("Deliverable Completion Report")
        
        st.plotly_chart(
            DashboardCharts.deliverable_status_chart(data['deliverables']),
            use_container_width=True,
            key="deliverable_report"
        )
        
        st.dataframe(data['deliverables'], use_container_width=True, hide_index=True)
    
    elif report_type == "Client Satisfaction":
        st.subheader("Client Satisfaction Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(
                DashboardCharts.satisfaction_trend_chart(analyzer.get_monthly_trends()),
                use_container_width=True,
                key="satisfaction_report"
            )
        
        with col2:
            avg_satisfaction = analyzer.get_monthly_trends()['satisfaction_score'].mean()
            st.metric("Average Satisfaction", f"{avg_satisfaction:.2f}/5.0", delta="Out of 5")
            
            st.write("**Satisfaction by Month**")
            monthly_sat = analyzer.get_monthly_trends().groupby('date')['satisfaction_score'].mean().reset_index()
            st.dataframe(monthly_sat, use_container_width=True, hide_index=True)

st.sidebar.divider()
st.sidebar.markdown("---")
st.sidebar.markdown("**Version:** 1.0.0  \n**Data Source:** Local CSV Files  \n**Last Sync:** Auto")
