import pandas as pd

class SolarFarmAnalyzer:
    def __init__(self):
        pass

    def create_production_df(self,data:list)->pd.DataFrame:
        df=pd.DataFrame(data,columns=["TurbineID","Date","Energy","WindSpeed","OutrageMinutes"])

        return df

    def total_energy_per_turbine(self,df:pd.DataFrame)->pd.DataFrame:
        result=(
            df.groupby('TurbineID',as_index=False).agg(
                TotalEnergy=('Energy','sum')
            )
        )
        result=result.reset_index(drop=True)
        return result

    def add_energy_per_min(self,df:pd.DataFrame)->pd.DataFrame:
        active_minutes=1440 - df['OutrageMinutes']

        df['EnergyPerMin']=df['Energy'] / active_minutes

        return df

    def categorize_wind_band(self,df:pd.DataFrame)->pd.DataFrame:
        df['WindBand']='Low'

        df.loc[df['WindSpeed']>=3,'WindBand']='Moderate'
        df.loc[df['WindSpeed']>=7,'WindBand']='High'

        return df

    def frequent_outrage_rows(self,df:pd.DataFrame,n:int)->pd.DataFrame:
        return df[df['OutrageMinutes']>n]

    def clean_and_top_days(self,df:pd.DataFrame)->pd.DataFrame:
        df=df.dropna()
        result=df.sort_values('Energy',ascending=False)
        return result


# Create analyzer object
analyzer = SolarFarmAnalyzer()


print("===== TEST 1: CREATE PRODUCTION DATAFRAME =====")

data = [
    ["T1", "2025-08-01", 500.0, 5.4, 30],
    ["T2", "2025-08-01", 800.0, 4.8, 0],
    ["T1", "2025-08-02", 895.0, 7.2, 45]
]

df = analyzer.create_production_df(data)

print(df)


print("\n===== TEST 2: TOTAL ENERGY PER TURBINE =====")

result = analyzer.total_energy_per_turbine(df)

print(result)


print("\n===== TEST 3: ENERGY PER UPTIME MINUTE =====")

result = analyzer.add_energy_per_min(df)

print(result)


print("\n===== TEST 4: CATEGORIZE WIND BAND =====")

result = analyzer.categorize_wind_band(df)

print(result)


print("\n===== TEST 5: FREQUENT OUTAGE ROWS =====")

result = analyzer.frequent_outrage_rows(df, 10)

print(result)


print("\n===== TEST 6: CLEAN & TOP PRODUCTION DAYS =====")

data_with_nulls = [
    ["T1", "2025-08-01", 500.0, 5.4, 30],
    ["T2", "2025-08-01", 800.0, 4.8, 0],
    ["T1", "2025-08-02", 895.0, 7.2, 45],
    [None, None, None, None, None]
]

df_with_nulls = analyzer.create_production_df(data_with_nulls)

result = analyzer.clean_and_top_days(df_with_nulls)

print(result)