PEM_FILE=/Users/alessio/Documents/Universita/big-data/alessio_bigdata.pem
PATH_STREAMING=/Users/alessio/Documents/Universita/big-data/hadoop-3.2.1/streaming/hadoop-streaming-3.2.1.jar
MAPPER=/Users/alessio/Documents/Universita/big-data/Big_Data_First_Project/job3/mapreduce/mapper.py
REDUCER=/Users/alessio/Documents/Universita/big-data/Big_Data_First_Project/job3/mapreduce/reducer.py
MAPPER2=/Users/alessio/Documents/Universita/big-data/Big_Data_First_Project/job3/mapreduce/mapper2.py
REDUCER2=/Users/alessio/Documents/Universita/big-data/Big_Data_First_Project/job3/mapreduce/reducer2.py
INPUT_PATH=/Users/alessio/Documents/Universita/big-data/Big_Data_First_Project/dataset/
START=/Users/alessio/Documents/Universita/big-data/Big_Data_First_Project/job3/mapreduce/script/start3.sh
RESTORE=/Users/alessio/Documents/Universita/big-data/Big_Data_First_Project/job3/mapreduce/script/restore.sh


INPUT_NAME=
INPUT_2_NAME=
CLUSTER_ADDRESS=

scp -i $PEM_FILE $PATH_STREAMING $CLUSTER_ADDRESS:~
scp -i $PEM_FILE $MAPPER $CLUSTER_ADDRESS:~
scp -i $PEM_FILE $REDUCER $CLUSTER_ADDRESS:~
scp -i $PEM_FILE $MAPPER2 $CLUSTER_ADDRESS:~
scp -i $PEM_FILE $REDUCER2 $CLUSTER_ADDRESS:~
scp -i $PEM_FILE $INPUT_PATH$INPUT_NAME $CLUSTER_ADDRESS:~
scp -i $PEM_FILE $INPUT_PATH$INPUT_2_NAME $CLUSTER_ADDRESS:~
scp -i $PEM_FILE $START $CLUSTER_ADDRESS:~
scp -i $PEM_FILE $RESTORE $CLUSTER_ADDRESS:~

ssh -i $PEM_FILE $CLUSTER_ADDRESS

