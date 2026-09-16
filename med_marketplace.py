import pandas as pd


class ReturnsAnalyzer:

    # 1. Create Orders DataFrame
    def create_orders_df(self, order_data: list) -> pd.DataFrame:

        df = pd.DataFrame(
            order_data,
            columns=[
                "OrderID",
                "SellerID",
                "Category",
                "OrderDate",
                "OrderAmount"
            ]
        )

        return df

    # 2. Create Returns DataFrame
    def create_returns_df(self, return_data: list) -> pd.DataFrame:

        df = pd.DataFrame(
            return_data,
            columns=[
                "OrderID",
                "ReturnDate",
                "RefundAmount",
                "Reason"
            ]
        )

        return df

    # 3. Merge Orders with Returns
    def merge_orders_returns(
        self,
        orders_df: pd.DataFrame,
        returns_df: pd.DataFrame
    ) -> pd.DataFrame:

        result = pd.merge(
            orders_df,
            returns_df,
            on="OrderID",
            how="left"
        )

        return result

    # 4. Category-wise Refund Rate
    def category_refund_rate(
        self,
        merged_df: pd.DataFrame
    ) -> pd.DataFrame:

        result = (
            merged_df.groupby("Category")
            .agg(
                Orders=("OrderID", "size"),
                ReturnedOrders=("RefundAmount", "count")
            )
            .reset_index()
        )

        result["RefundRate"] = (
            result["ReturnedOrders"]
            / result["Orders"]
            * 100
        )

        result = result.sort_values("Category").reset_index(drop=True)

        return result

    # 5. High Return Sellers
    def high_return_sellers(
        self,
        merged_df: pd.DataFrame,
        n: int
    ) -> pd.DataFrame:

        result = (
            merged_df[merged_df["IsReturned"] == 1]
            .groupby("SellerID")
            .size()
            .reset_index(name="ReturnCount")
        )

        result = result[result["ReturnCount"] > n]

        return result.reset_index(drop=True)

    # 6. Clean Return Records
    def clean_returns_data(
        self,
        returns_df: pd.DataFrame
    ) -> pd.DataFrame:

        result = returns_df.dropna(subset=["Reason"])

        result = result[
            result["RefundAmount"].notna()
            & (result["RefundAmount"] > 0)
        ]

        return result.reset_index(drop=True)