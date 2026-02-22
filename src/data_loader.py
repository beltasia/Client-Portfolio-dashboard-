import pandas as pd
import os
from pathlib import Path
from typing import Dict, List

class DataLoader:
    """Load and cache data from CSV/JSON files"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.cache = {}
    
    def load_csv(self, filename: str) -> pd.DataFrame:
        """Load CSV file and cache it"""
        if filename in self.cache:
            return self.cache[filename]
        
        filepath = self.data_dir / filename
        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        df = pd.read_csv(filepath)
        self.cache[filename] = df
        return df
    
    def load_json(self, filename: str) -> Dict:
        """Load JSON file and cache it"""
        if filename in self.cache:
            return self.cache[filename]
        
        filepath = self.data_dir / filename
        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        import json
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        self.cache[filename] = data
        return data
    
    def get_clients(self) -> pd.DataFrame:
        """Load clients data"""
        df = self.load_csv("clients.csv")
        df['start_date'] = pd.to_datetime(df['start_date'])
        return df
    
    def get_engagements(self) -> pd.DataFrame:
        """Load engagements data"""
        df = self.load_csv("engagements.csv")
        df['start_date'] = pd.to_datetime(df['start_date'])
        df['end_date'] = pd.to_datetime(df['end_date'])
        return df
    
    def get_deliverables(self) -> pd.DataFrame:
        """Load deliverables data"""
        df = self.load_csv("deliverables.csv")
        df['due_date'] = pd.to_datetime(df['due_date'])
        df['completion_date'] = pd.to_datetime(df['completion_date'], errors='coerce')
        return df
    
    def get_monthly_summaries(self) -> pd.DataFrame:
        """Load monthly summaries data"""
        return self.load_csv("monthly_summaries.csv")
    
    def refresh(self):
        """Clear cache and reload all data"""
        self.cache.clear()
