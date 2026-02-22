import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime
from typing import Dict, List

class DashboardCharts:
    """Create dashboard visualizations"""
    
    @staticmethod
    def portfolio_metrics(summary: Dict) -> go.Figure:
        """Create portfolio metrics gauge chart"""
        fig = go.Figure()
        
        metrics_data = [
            {'title': 'Active Clients', 'value': summary['active_clients'], 'total': summary['total_clients']},
            {'title': 'Active Engagements', 'value': summary['active_engagements'], 'total': summary['total_engagements']},
            {'title': 'Avg Progress', 'value': round(summary['average_progress'], 1), 'total': 100},
        ]
        
        return fig
    
    @staticmethod
    def client_health_chart(health_data: pd.DataFrame) -> go.Figure:
        """Create client health score chart"""
        fig = px.bar(
            health_data.head(10),
            x='client_name',
            y='health_score',
            color='health_score',
            color_continuous_scale='RdYlGn',
            title='Client Health Scores (Top 10)',
            labels={'health_score': 'Health Score', 'client_name': 'Client'},
            hover_data=['status', 'avg_progress', 'budget_utilization']
        )
        
        fig.update_layout(
            height=400,
            showlegend=False,
            hovermode='x unified'
        )
        
        return fig
    
    @staticmethod
    def engagement_progress_chart(engagement_data: pd.DataFrame) -> go.Figure:
        """Create engagement progress chart"""
        fig = px.bar(
            engagement_data.sort_values('progress', ascending=False).head(15),
            x='engagement_name',
            y='progress',
            color='status',
            title='Engagement Progress Status',
            labels={'progress': 'Progress (%)', 'engagement_name': 'Engagement'},
            color_discrete_map={
                'In Progress': '#3498db',
                'Completed': '#2ecc71',
                'On Hold': '#e74c3c',
                'Paused': '#f39c12'
            }
        )
        
        fig.update_layout(
            height=400,
            xaxis_tickangle=-45,
            hovermode='x unified'
        )
        
        return fig
    
    @staticmethod
    def budget_utilization_chart(engagement_data: pd.DataFrame) -> go.Figure:
        """Create budget utilization scatter chart"""
        fig = px.scatter(
            engagement_data,
            x='budget_utilization_pct',
            y='progress',
            size='budget_allocated',
            color='status',
            hover_name='engagement_name',
            title='Budget Utilization vs Progress',
            labels={
                'budget_utilization_pct': 'Budget Utilization (%)',
                'progress': 'Progress (%)'
            },
            color_discrete_map={
                'In Progress': '#3498db',
                'Completed': '#2ecc71',
                'On Hold': '#e74c3c',
                'Paused': '#f39c12'
            }
        )
        
        fig.update_layout(height=400, hovermode='closest')
        
        return fig
    
    @staticmethod
    def monthly_revenue_chart(trends_data: pd.DataFrame) -> go.Figure:
        """Create monthly revenue trend chart"""
        monthly_rev = trends_data.groupby('date')['revenue_generated'].sum().reset_index()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=monthly_rev['date'],
            y=monthly_rev['revenue_generated'],
            mode='lines+markers',
            fill='tozeroy',
            name='Revenue',
            line=dict(color='#2ecc71', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title='Monthly Revenue Generated',
            xaxis_title='Month',
            yaxis_title='Revenue ($)',
            height=350,
            hovermode='x unified',
            template='plotly_white'
        )
        
        return fig
    
    @staticmethod
    def hours_spent_chart(trends_data: pd.DataFrame) -> go.Figure:
        """Create monthly hours spent chart"""
        monthly_hours = trends_data.groupby('date')['hours_spent'].sum().reset_index()
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=monthly_hours['date'],
            y=monthly_hours['hours_spent'],
            name='Hours Spent',
            marker=dict(color='#3498db')
        ))
        
        fig.update_layout(
            title='Monthly Hours Spent',
            xaxis_title='Month',
            yaxis_title='Hours',
            height=350,
            hovermode='x unified',
            template='plotly_white',
            showlegend=False
        )
        
        return fig
    
    @staticmethod
    def deliverable_status_chart(deliverables: pd.DataFrame) -> go.Figure:
        """Create deliverable status pie chart"""
        status_counts = deliverables['status'].value_counts()
        
        colors = {
            'Completed': '#2ecc71',
            'In Progress': '#3498db',
            'Pending': '#f39c12',
            'On Hold': '#e74c3c'
        }
        
        fig = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title='Deliverable Status Distribution',
            color_discrete_map=colors
        )
        
        fig.update_layout(height=400)
        
        return fig
    
    @staticmethod
    def industry_distribution_chart(clients: pd.DataFrame) -> go.Figure:
        """Create industry distribution chart"""
        industry_counts = clients['industry'].value_counts()
        
        fig = px.bar(
            x=industry_counts.index,
            y=industry_counts.values,
            title='Clients by Industry',
            labels={'x': 'Industry', 'y': 'Number of Clients'},
            color_discrete_sequence=['#3498db']
        )
        
        fig.update_layout(
            height=350,
            showlegend=False,
            xaxis_tickangle=-45
        )
        
        return fig
    
    @staticmethod
    def client_status_breakdown(clients: pd.DataFrame) -> go.Figure:
        """Create client status breakdown"""
        status_counts = clients['status'].value_counts()
        
        colors = {
            'Active': '#2ecc71',
            'Completed': '#95a5a6',
            'Paused': '#e74c3c'
        }
        
        fig = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title='Client Status Breakdown',
            color_discrete_map=colors
        )
        
        fig.update_layout(height=350)
        
        return fig
    
    @staticmethod
    def satisfaction_trend_chart(trends_data: pd.DataFrame) -> go.Figure:
        """Create satisfaction score trend"""
        satisfaction = trends_data.groupby('date')['satisfaction_score'].mean().reset_index()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=satisfaction['date'],
            y=satisfaction['satisfaction_score'],
            mode='lines+markers',
            fill='tozeroy',
            name='Satisfaction Score',
            line=dict(color='#9b59b6', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title='Client Satisfaction Trend',
            xaxis_title='Month',
            yaxis_title='Satisfaction Score (0-5)',
            height=350,
            hovermode='x unified',
            template='plotly_white',
            yaxis=dict(range=[0, 5])
        )
        
        return fig
    
    @staticmethod
    def quality_metrics_chart(deliverables: pd.DataFrame) -> go.Figure:
        """Create quality score distribution"""
        quality_scores = deliverables[deliverables['quality_score'].notna()]['quality_score']
        
        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=quality_scores,
            nbinsx=10,
            name='Quality Scores',
            marker=dict(color='#1abc9c')
        ))
        
        fig.update_layout(
            title='Deliverable Quality Score Distribution',
            xaxis_title='Quality Score',
            yaxis_title='Count',
            height=350,
            hovermode='x unified',
            template='plotly_white'
        )
        
        return fig
