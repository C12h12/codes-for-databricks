
import pandas as pd


class EVChargingAnalyzer:

    # 1. Create Charging Sessions DataFrame
    def create_sessions_df(self, session_data: list) -> pd.DataFrame:

        columns = [
            "SessionID",
            "StationID",
            "City",
            "ChargingDate",
            "EnergyKWh",
            "DurationMinutes",
            "PaymentStatus"
        ]

        return pd.DataFrame(session_data, columns=columns)

    # 2. Clean Charging Sessions
    def clean_sessions_data(self, df: pd.DataFrame) -> pd.DataFrame:

        valid_statuses = ["Paid", "Pending", "Failed"]

        result = df.dropna(
            subset=[
                "SessionID",
                "StationID",
                "City",
                "PaymentStatus"
            ]
        )

        result = result[
            (result["EnergyKWh"] > 0) &
            (result["DurationMinutes"] > 0) &
            (result["PaymentStatus"].isin(valid_statuses))
        ]

        return result.reset_index(drop=True)

    # 3. Add Long Session Flag
    def add_long_session_flag(
        self,
        df: pd.DataFrame,
        duration_threshold: int
    ) -> pd.DataFrame:

        result = df.copy()

        result["IsLongSession"] = (
            result["DurationMinutes"] > duration_threshold
        ).astype(int)

        return result

    # 4. Station Utilization Summary
    def station_utilization_summary(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        result = (
            df.groupby("StationID", as_index=False)
            .agg(
                SessionCount=("SessionID", "count"),
                TotalEnergyKWh=("EnergyKWh", "sum"),
                AverageDuration=("DurationMinutes", "mean")
            )
        )

        result["AverageDuration"] = result[
            "AverageDuration"
        ].round(1)

        return result

    # 5. High Energy Stations
    def high_energy_stations(
        self,
        df: pd.DataFrame,
        energy_threshold: float
    ) -> pd.DataFrame:

        result = (
            df.groupby("StationID", as_index=False)
            .agg(
                TotalEnergyKWh=("EnergyKWh", "sum")
            )
        )

        result = result[
            result["TotalEnergyKWh"] > energy_threshold
        ]

        return result.reset_index(drop=True)

    # 6. City Revenue Summary
    def city_revenue_summary(
        self,
        df: pd.DataFrame
    ) -> pd.DataFrame:

        paid_sessions = df[
            df["PaymentStatus"] == "Paid"
        ].copy()

        paid_sessions["Revenue"] = (
            paid_sessions["EnergyKWh"] * 18
        )

        result = (
            paid_sessions.groupby("City", as_index=False)
            .agg(Revenue=("Revenue", "sum"))
        )

        return result


# =====================================================
# TESTING
# =====================================================

analyzer = EVChargingAnalyzer()


# Uncleaned testing data
session_data = [
    [501, "ST01", "Bengaluru", "2025-02-01", 42.5, 75, "Paid"],
    [502, "ST02", "Chennai", "2025-02-01", 28.0, 50, "Paid"],
    [503, "ST01", "Bengaluru", "2025-02-02", 55.0, 130, "Pending"],
    [504, "ST03", "Mumbai", "2025-02-02", 0.0, 60, "Paid"],
    [505, "ST02", "Chennai", "2025-02-03", -10.0, 40, "Paid"],
    [506, None, "Delhi", "2025-02-03", 35.0, 80, "Paid"],
    [507, "ST04", None, "2025-02-04", 45.0, 90, "Paid"],
    [508, "ST01", "Bengaluru", "2025-02-04", 30.0, 0, "Pending"],
    [509, "ST03", "Mumbai", "2025-02-05", 25.0, -20, "Paid"],
    [510, "ST02", "Chennai", "2025-02-05", 20.0, 45, "Cancelled"],
    [511, "ST04", "Delhi", "2025-02-06", 60.0, 100, None],
    [512, "ST03", "Mumbai", "2025-02-06", 50.0, 110, "Failed"]
]


# TC1: Create DataFrame
print("\n===== TC1: CREATE SESSIONS DATAFRAME =====")

df = analyzer.create_sessions_df(session_data)

print(df)


# TC2: Clean Sessions
print("\n===== TC2: CLEAN SESSIONS DATA =====")

cleaned_df = analyzer.clean_sessions_data(df)

print(cleaned_df)


# TC3: Add Long Session Flag
print("\n===== TC3: LONG SESSION FLAG =====")

long_sessions_df = analyzer.add_long_session_flag(
    cleaned_df,
    90
)

print(long_sessions_df)


# TC4: Station Utilization Summary
print("\n===== TC4: STATION UTILIZATION SUMMARY =====")

utilization_df = analyzer.station_utilization_summary(
    cleaned_df
)

print(utilization_df)


# TC5: High Energy Stations
print("\n===== TC5: HIGH ENERGY STATIONS =====")

high_energy_df = analyzer.high_energy_stations(
    cleaned_df,
    80.0
)

print(high_energy_df)


# TC6: City Revenue Summary
print("\n===== TC6: CITY REVENUE SUMMARY =====")

revenue_df = analyzer.city_revenue_summary(
    cleaned_df
)

print(revenue_df)


# HTC1: Hidden Test - Invalid values and statuses
print("\n===== HTC1: INVALID DATA TEST =====")

invalid_data = [
    [601, "ST05", "Pune", "2025-02-10", 0, 60, "Paid"],
    [602, "ST05", "Pune", "2025-02-11", -5, 70, "Paid"],
    [603, "ST06", "Hyderabad", "2025-02-12", 20, 0, "Paid"],
    [604, "ST06", "Hyderabad", "2025-02-13", 30, -10, "Pending"],
    [605, "ST07", "Kolkata", "2025-02-14", 40, 80, "Cancelled"],
    [606, "ST07", "Kolkata", "2025-02-15", 45, 90, "Paid"]
]

invalid_df = analyzer.create_sessions_df(invalid_data)

cleaned_invalid_df = analyzer.clean_sessions_data(
    invalid_df
)

print(cleaned_invalid_df)


# HTC2: Hidden Test - Exact threshold
print("\n===== HTC2: EXACT THRESHOLD TEST =====")

threshold_data = [
    [701, "ST08", "Nagpur", "2025-03-01", 40.0, 60, "Paid"],
    [702, "ST08", "Nagpur", "2025-03-02", 40.0, 60, "Paid"],
    [703, "ST09", "Surat", "2025-03-03", 100.0, 70, "Paid"]
]

threshold_df = analyzer.create_sessions_df(
    threshold_data
)

exact_threshold_df = analyzer.high_energy_stations(
    threshold_df,
    80.0
)

print(exact_threshold_df)