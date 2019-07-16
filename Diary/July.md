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
