# Create AWS EMR Cluster 
# Replace KEY_NAME and SUBNET_ID with your own values
aws emr create-cluster \
--name Udacity-HowToAccumulators \
--use-default-roles \
--release-label emr-5.28.0 \
--instance-count 3 \
--applications Name=Spark Name=Hadoop Name=Livy \
--ec2-attributes KeyName=<YOUR_KEY_NAME>,SubnetId=subnet-<SUBNET_ID> \
--instance-type m5.xlarge \
--log-uri s3://emrlogs/ 