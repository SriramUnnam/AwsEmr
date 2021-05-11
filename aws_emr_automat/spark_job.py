from pyspark import SparkContext
from pyspark.sql import SQLContext
sc = SparkContext()
sqlContext = SQLContext(sc)
df = sqlContext.read.option("multiline","true").json("S3_URI/sampl.json")
df.write.parquet("S3_URI/sampl.parquet")