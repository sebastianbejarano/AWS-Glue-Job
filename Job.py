 import pandas as pd
 import io
 import boto3

s3= boto3.resource("s3")
object = s3.Bucket("testing12432").Object("probando/datosprobando.csv.csv").get()["Body"].read().decode("utf-8")
print(object)

df = pd.read_csv(io.StringIO(object))
d = {"M":"MALE", "F":"FEMALE"}

df["Gender"]=df["Gender"].map(d)

print (df.head())

df.to_parquet("s3://testing12432/resultado0987/resultado2.parquet")
