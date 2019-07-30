## 08-07-2019

notes:

- atom :
  - package manager: apm
    - apm install (in terminal)
    - shift + command + p = command
  - install date package

- drupal


- what is hadoop, set up on ubuntu
- what is mysql, apache ?

## 09-07-2019

The problem of how to work ?

XCEDE super computer.

----------

letter to hamid.


## 10-07-2019

hadoop on ubuntu : https://www.digitalvidya.com/blog/install-hadoop-on-ubuntu-and-run-your-first-mapreduce-program/

Hadoop ?

Latest Hadoop 3.0.0 comprises these main modules:
- Hadoop Common
- Hadoop Distributed File system
- Hadoop YARN
- Hadoop MapReduce

install

- separate login
  - add group, add user
- environment
  - java
  - ssh
- install Hadoop
  - download and mv to /usr/local
- configuration
- format hadoop file system
- start hadoop damons

**When we want to run hadoop, start dfs and yarn**

**When start a new task, delete all the file in datanode**

```sh
netstat -lpten | grep java
# see tcp connections.
```

## 2019-07-11

oil change and check of my car.

No more work at weekend.

## 2019-07-14

Sunday. Check answer.

## 2019-07-16

On mac, we got error.

Exception in thread "main" java.net.ConnectException: Call From atan-115b-11.cs.iastate.edu/10.26.54.106 to localhost:9000 failed on connection exception: java.net.ConnectException: Connection refused; For more details see:  http://wiki.apache.org/hadoop/ConnectionRefused


## 2019-07-17

I didn't went lab today.

## 2019-07-18

Time pass so quickly. It turns out every one knows what to do except me.

- learn hadoop on mac / ubuntu

  - jar on mac to virtualBox

- connection failed : we need start dfs

hadoop works like a server. This server manage many namenode and datanode, distribute resources. Our computer works like a client. This client upload files and codes to server and server start new jobs about it.

```sh
hadoop fs -put
hadoop fs -ls hdfs://localhost:54310/
```

- hadoop com.sun.tools.javac.Main wordCount.java

error bad substitution. no HADOOP_CLASS. java/lib/tools.jar

- jar vtf jarfile (https://blog.csdn.net/liuhui_306/article/details/51872567)

## 2019-07-19

- mac virtualbox share folder.
https://www.youtube.com/watch?v=YSLNqXxyUtk
```sh
sudo mount -t vboxsf mac_share /media/test1
```

- map reduce java code

## 2019-07-23

I don't know what to do?

## 2019-07-27

- rent house 1217 delever (first property)
- jinqiao invited me a dinner.
- no one in lab at night.


- what to do?
  - sumon paper
  - read source code of python parser
  - write r parser

## 2019-07-30

- moving into new apartment (aug 1st noon)
- R parser in JAVA
