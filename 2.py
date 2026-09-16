import pandas as pd

class FlightDelayAnalyzer:

    def create_flight_log_df(self, flight_log: list) -> pd.DataFrame:
        return pd.DataFrame(
            flight_log,
            columns=["FlightID", "AirlineCode", "Route", "Delay"]
        )

    def create_airline_master_df(self, airline_master: list) -> pd.DataFrame:
        return pd.DataFrame(
            airline_master,
            columns=["AirlineCode", "AirlineName"]
        )

    def merge_airline_names(
        self,
        flight_log_df: pd.DataFrame,
        airline_master_df: pd.DataFrame
    ) -> pd.DataFrame:
        return flight_log_df.merge(
            airline_master_df,
            on="AirlineCode",
            how="left"
        )

    def average_delay_by_airline(self, merged_df: pd.DataFrame) -> pd.DataFrame:
        return (
            merged_df.groupby("AirlineName")["Delay"]
            .mean()
            .reset_index()
            .rename(columns={"Delay": "Average Delay"})
        )

    def filter_high_delays(
        self,
        flight_log_df: pd.DataFrame,
        threshold: int
    ) -> pd.DataFrame:
        return flight_log_df[flight_log_df["Delay"] > threshold]

    def most_delayed_route(self, flight_log_df: pd.DataFrame) -> pd.DataFrame:
        result = (
            flight_log_df.groupby("Route")["Delay"]
            .mean()
            .reset_index()
            .rename(columns={"Delay": "Average Delay"})
        )

        return (
            result.sort_values("Average Delay", ascending=False)
            .head(1)
            .reset_index(drop=True)
        )