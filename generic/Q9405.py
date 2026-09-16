#Solar Farm Maintenance Analysis
import pandas as pd

class SolarMaintenanceAnalyzer:

    def create_inspections_df(self,inspection_data:list)->pd.DataFrame:
        df=pd.DataFrame(inspection_data,
                        columns=['InspectionID',
                                 'SiteID',
                                 'Region',
                                 'InspectionDate',
                                 'OutputMWh',
                                 'DowntimeHours',
                                 'MaintenanceStatus'])
        return df

    def clean_inspection_data(self,df:pd.DataFrame)->pd.DataFrame:
        result=df.copy()
        result=result[result.notna().all(axis=1)
                      & (result['OutputMWh'] > 0)
                      & (result['DowntimeHours']>=0)
                      & (result['MaintenanceStatus'].isin(['Completed','Scheduled']))
                      ]
        columns=                        ['InspectionID',
                                         'SiteID',
                                         'Region',
                                         'InspectionDate',
                                         'OutputMWh',
                                         'DowntimeHours',
                                         'MaintenanceStatus']

        return result[columns].reset_index(drop=True)

    def add_attention_flag(self,df:pd.DataFrame,downtime_threshold:float)->pd.DataFrame:
        result=df.copy()
        result['NeedsAttention']=(result['DowntimeHours'] > downtime_threshold).astype(int)

        return result
    def site_performance_summary(self,df:pd.DataFrame)->pd.DataFrame:
        result=(df.groupby('SiteID',as_index=False).agg(
            InspectionCount=('InspectionID','count'),
            TotalOutputMWh=('OutputMWh','sum'),
            AverageDowntime=('DowntimeHours','mean')
        ))
        return result.sort_values('SiteID').reset_index(drop=True)

    def low_output_sites(self,df:pd.DataFrame,output_threshold:float)->pd.DataFrame:

        result=df.groupby('SiteID').agg(
            TotalOutputMWh=('OutputMWh','sum')
        )
        result=result[result['TotalOutputMWh']< output_threshold]
        return result.sort_values('SiteID').reset_index(drop=True)

    def regional_maintenance_cost(self,df:pd.DataFrame)->pd.DataFrame:
        result=df.copy()
        result=result[result['MaintenanceStatus']=='Completed']
        result['MaintenanceCost']=result['DowntimeHours'] * 250.0

        result1=result.groupby('Region',as_index=False).agg(
            Maintenance_cost=('MaintenanceCost','sum')
        )

        return result1.sort_values('Region').reset_index(drop=True)




analyzer = SolarMaintenanceAnalyzer()

# Uncleaned data
data = [
    [1, "S01", "North", "2026-01-01", 120.0, 2.0, "Completed"],
    [2, "S01", "North", "2026-01-02", 135.0, 1.5, "Scheduled"],
    [3, "S01", "North", "2026-01-03", 110.0, 4.5, "Completed"],
    [4, "S02", "South", "2026-01-04", 95.0, 3.0, "Completed"],
    [5, "S02", "South", "2026-01-05", 105.0, 2.5, "Scheduled"],
    [6, "S02", "South", "2026-01-06", -50.0, 4.0, "Completed"],
    [7, "S03", "East", "2026-01-07", 200.0, 6.0, "Completed"],
    [8, "S03", "East", "2026-01-08", 180.0, 5.5, "Scheduled"],
    [9, "S03", "East", "2026-01-09", 190.0, -1.0, "Completed"],
    [10, "S04", "West", "2026-01-10", 75.0, 1.0, "Completed"],
    [11, "S04", "West", "2026-01-11", 85.0, 2.0, "Scheduled"],
    [12, "S04", "West", "2026-01-12", 90.0, 3.5, "Completed"],
    [13, "S05", "Central", "2026-01-13", 250.0, 7.0, "Completed"],
    [14, "S05", "Central", "2026-01-14", 260.0, 6.5, "Scheduled"],
    [15, "S05", "Central", "2026-01-15", None, 4.0, "Completed"],
    [16, "S06", "North", "2026-01-16", 145.0, 2.5, "Completed"],
    [17, "S06", "North", "2026-01-17", 155.0, 3.5, "Scheduled"],
    [18, "S07", "South", "2026-01-18", 60.0, 8.0, "Completed"],
    [19, "S07", "South", "2026-01-19", 70.0, 9.0, "Pending"],
    [20, "S08", "East", "2026-01-20", 300.0, 1.5, "Completed"]
]

# Create DataFrame
df = analyzer.create_inspections_df(data)

print("Before Cleaning:")
print(df)

# Clean data
cleaned_df = analyzer.clean_inspection_data(df)

print("\nAfter Cleaning:")
print(cleaned_df)

# Add attention flag
flagged_df = analyzer.add_attention_flag(cleaned_df, 3.0)

print("\nAttention Flag:")
print(flagged_df)

# Site performance summary
print("\nSite Performance:")
print(analyzer.site_performance_summary(cleaned_df))

# Low output sites
print("\nLow Output Sites:")
print(analyzer.low_output_sites(cleaned_df, 250.0))

# Regional maintenance cost
print("\nMaintenance Cost:")
print(analyzer.regional_maintenance_cost(cleaned_df))