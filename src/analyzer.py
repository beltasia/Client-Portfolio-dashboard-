import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

class DataAnalyzer:
    """Analyze portfolio and client data"""
    
    def __init__(self, clients_df, engagements_df, deliverables_df, summaries_df):
        self.clients = clients_df
        self.engagements = engagements_df
        self.deliverables = deliverables_df
        self.summaries = summaries_df
    
    def get_portfolio_summary(self) -> Dict:
        """Get overall portfolio metrics"""
        return {
            'total_clients': len(self.clients),
            'active_clients': len(self.clients[self.clients['status'] == 'Active']),
            'total_contract_value': self.clients['contract_value'].sum(),
            'total_engagements': len(self.engagements),
            'active_engagements': len(self.engagements[self.engagements['status'] == 'In Progress']),
            'completed_engagements': len(self.engagements[self.engagements['status'] == 'Completed']),
            'average_progress': self.engagements[self.engagements['status'] == 'In Progress']['progress'].mean(),
        }
    
    def get_client_health(self) -> pd.DataFrame:
        """Get health metrics for each client"""
        client_engagement_count = self.engagements.groupby('client_id').size()
        client_avg_progress = self.engagements[self.engagements['status'] == 'In Progress'].groupby('client_id')['progress'].mean()
        client_budget_utilization = (self.engagements.groupby('client_id')['budget_spent'].sum() / 
                                      self.engagements.groupby('client_id')['budget_allocated'].sum())
        
        health_data = self.clients[['client_id', 'client_name', 'status']].copy()
        health_data['engagement_count'] = health_data['client_id'].map(client_engagement_count)
        health_data['avg_progress'] = health_data['client_id'].map(client_avg_progress).fillna(0)
        health_data['budget_utilization'] = health_data['client_id'].map(client_budget_utilization).fillna(0)
        
        # Calculate health score (0-100)
        health_data['health_score'] = (
            (health_data['avg_progress'] * 0.5) +  # 50% based on progress
            (100 - (health_data['budget_utilization'] * 100).clip(0, 100) * 0.3) +  # 30% on budget efficiency
            (health_data['engagement_count'].clip(0, 5) / 5 * 100 * 0.2)  # 20% on activity
        ).round(1)
        
        return health_data.sort_values('health_score', ascending=False)
    
    def get_engagement_performance(self) -> pd.DataFrame:
        """Get performance metrics for each engagement"""
        perf_data = self.engagements.copy()
        perf_data['budget_remaining'] = perf_data['budget_allocated'] - perf_data['budget_spent']
        perf_data['budget_utilization_pct'] = (perf_data['budget_spent'] / perf_data['budget_allocated'] * 100).round(1)
        
        # Add deliverable info
        deliverable_stats = self.deliverables.groupby('engagement_id').agg({
            'deliverable_id': 'count',
            'status': lambda x: (x == 'Completed').sum(),
            'quality_score': 'mean'
        }).rename(columns={
            'deliverable_id': 'total_deliverables',
            'status': 'completed_deliverables',
            'quality_score': 'avg_quality_score'
        })
        
        perf_data = perf_data.merge(deliverable_stats, left_on='engagement_id', right_index=True, how='left')
        perf_data['deliverable_completion_pct'] = (
            (perf_data['completed_deliverables'] / perf_data['total_deliverables'] * 100)
            .fillna(0).round(1)
        )
        perf_data['avg_quality_score'] = perf_data['avg_quality_score'].fillna(0).round(1)
        
        return perf_data
    
    def get_monthly_trends(self) -> pd.DataFrame:
        """Get monthly trends for revenue and hours"""
        trends = self.summaries.copy()
        trends['date'] = pd.to_datetime(trends[['year', 'month']].assign(day=1))
        trends = trends.sort_values('date')
        return trends
    
    def get_at_risk_items(self) -> Dict:
        """Identify at-risk engagements and deliverables"""
        at_risk = {
            'over_budget_engagements': [],
            'at_risk_deliverables': [],
            'paused_engagements': []
        }
        
        # Over budget engagements
        over_budget = self.engagements[self.engagements['budget_spent'] > self.engagements['budget_allocated']]
        at_risk['over_budget_engagements'] = over_budget[['engagement_id', 'engagement_name', 'budget_allocated', 'budget_spent']].to_dict('records')
        
        # Paused engagements
        paused = self.engagements[self.engagements['status'] == 'On Hold']
        at_risk['paused_engagements'] = paused[['engagement_id', 'engagement_name', 'progress']].to_dict('records')
        
        # Overdue deliverables
        today = pd.Timestamp.now()
        overdue = self.deliverables[
            (self.deliverables['due_date'] < today) & 
            (self.deliverables['status'] != 'Completed')
        ]
        at_risk['at_risk_deliverables'] = overdue[['deliverable_id', 'deliverable_name', 'due_date', 'status']].to_dict('records')
        
        return at_risk
    
    def get_client_summary(self, client_id: str) -> Dict:
        """Get detailed summary for a specific client"""
        client = self.clients[self.clients['client_id'] == client_id].iloc[0]
        client_eng = self.engagements[self.engagements['client_id'] == client_id]
        client_deliverables = self.deliverables[
            self.deliverables['engagement_id'].isin(client_eng['engagement_id'])
        ]
        
        return {
            'client': client.to_dict(),
            'engagements': client_eng.to_dict('records'),
            'deliverables': client_deliverables.to_dict('records'),
            'total_contract_value': client['contract_value'],
            'total_spent': client_eng['budget_spent'].sum(),
            'total_allocated': client_eng['budget_allocated'].sum(),
            'active_engagement_count': len(client_eng[client_eng['status'] == 'In Progress']),
            'completed_engagement_count': len(client_eng[client_eng['status'] == 'Completed']),
        }
