from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import *
from pyspark.sql.types import *


def define_claim_schema() -> StructType:
    return StructType([
        StructField('claim_id', StringType(), True),
        StructField('policy_id', StringType(), True),
        StructField('customer_id', StringType(), True),
        StructField('claim_amount', DoubleType(), True),
        StructField('claim_status', StringType(), True),
        StructField('claim_date', StringType(), True)
    ])


def load_claims_data(
    spark: SparkSession,
    path: str,
    schema: StructType
) -> DataFrame:
    result = spark.read.csv(
        path,
        header=True,
        schema=schema
    )
    return result.withColumn('claim_date', to_date('claim_date'))


def load_policy_data(
    spark: SparkSession,
    path: str
) -> DataFrame:
    policy_df = spark.read.csv(
        path,
        header=True,
        inferSchema=True
    )
    return policy_df


def join_claims_with_policies(
    claims_df: DataFrame,
    policies_df: DataFrame
) -> DataFrame:
    joined = claims_df.join(
        policies_df,
        on='policy_id',
        how='inner'
    )

    return joined.select(
        'claim_id',
        'policy_id',
        'customer_id',
        'claim_amount',
        'claim_status',
        'claim_date',
        'policy_type',
        'region',
        'annual_premium'
    )


def policy_type_with_highest_approved_claim_amount(
    df: DataFrame
) -> Tuple[str, float]:

    result = df.filter(
        col('claim_status') == 'Approved'
    )

    result = result.filter(
        col('policy_type').isNotNull()
        & (trim(col('policy_type')) != '')
        & col('claim_amount').isNotNull()
    )

    result = (
        result
        .groupBy(col('policy_type'))
        .agg(
            sum(col('claim_amount')).alias(
                'total_approved_claim_amount'
            )
        )
        .orderBy(
            col('total_approved_claim_amount').desc(),
            col('policy_type').asc()
        )
        .limit(1)
        .collect()
    )

    if result:
        return (
            str(result[0]['policy_type']),
            float(result[0]['total_approved_claim_amount'])
        )
    else:
        return ("", 0.0)
