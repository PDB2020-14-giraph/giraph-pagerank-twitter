#!/bin/bash

set -e
set -x

/etc/giraph-bootstrap.sh

cd /myhome

$HADOOP_HOME/bin/hdfs dfsadmin -safemode leave

$HADOOP_HOME/bin/hdfs dfs -put twt.txt /user/root/input/twt.txt

cd /myhome/giraph-work

javac -cp /usr/local/giraph/giraph-examples/target/giraph-examples-1.1.0-SNAPSHOT-for-hadoop-2.4.1-jar-with-dependencies.jar:$($HADOOP_HOME/bin/hadoop classpath) mypackage/PageRank.java

cp /usr/local/giraph/giraph-examples/target/giraph-examples-1.1.0-SNAPSHOT-for-hadoop-2.4.1-jar-with-dependencies.jar ./myjar.jar

jar uf myjar.jar mypackage

$HADOOP_HOME/bin/hadoop jar myjar.jar org.apache.giraph.GiraphRunner mypackage.PageRank --yarnjars myjar.jar --workers 2 --vertexInputFormat org.apache.giraph.io.formats.JsonLongDoubleFloatDoubleVertexInputFormat --vertexInputPath /user/root/input/twt.txt -vertexOutputFormat org.apache.giraph.io.formats.IdWithValueTextOutputFormat --outputPath /user/root/output-twt

$HADOOP_HOME/bin/hdfs dfs -get /user/root/output-twt/part-m-00001 /myhome/output-twt.txt