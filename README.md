# TensorMSA : Tensorflow Micro Service Architecture 
<b>1.TensorMSA </b> </br>
   - Tensor Micro Service Architecture is a project started to make TensorFlow more accessable from Java legacy systems
   with out modifying too much source codes. 

<b>2. Function </b></br>
   - REST APIs corresponding to Tensorflow 
   - JAVA API component interface with python REST APIS
   - Easy to use UI component provide NN configuration, train remotly, save & load NN models, handling train data sets
   - Train NN models via Spark cluster supported 
   - Android mobile SDK are also part of the plan (gather data and predict) 
   
<b>3. Schedule </b></br>
   - We just started this projects (2016.8)
   - We are still on research process now
   - Expected to release first trial version on December 2016 

<b>4. Stack </b></br>
   - FE : React(ES6), SVG, D3, Pure CSS
   - BE : Django F/W, Tensorflow, PostgreSQL, Spark

<b>5. Methodology </b></br>
   - Agile (CI, TDD, Pair programming and Cloud)

# Overview
Like described bellow, purpose of this project is provide deep learning management system via rest service so that non 
python legacy systems can use deep learning easily
<p align="center">
  <img src="https://raw.githubusercontent.com/seungwookim/TensorMSA/master/ProjectDesc3.png" width="750"/>
</p>

# Docker(Cluster Mode)*[(Docker Hub)](https://hub.docker.com/r/tmddno1/tensormsa/)**[(usage)](http://wp.me/p7xrpI-dr)*
   - Docker Packages </br>
   ```python
      data-master : docker pull tmddno1/tfmsa_name_node:v2
      data-slave : docker pull tmddno1/tfmsa_data_node:v2
      tfmsa-was : docker pull tmddno1/tensormsa:v2 
      CI tools : docker pull tmddno1/jenkins:v1  
   ```

   - Start master/slave node container *[(set up)](http://wp.me/p7xrpI-eH)*   </br>
   ```python
      docker run --net=host -d tmddno1/tfmsa_name_node:v2
      docker run --net=host -d tmddno1/tfmsa_name_node:v2
   ```
   - Start tfmsa-was container (dev purpose)  </br>
   
   ```python
       docker run -it --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"  -p 8989:8989 tmddno1/tensormsa:v2
   ```
   - Start tfmsa-was container (dev purpose) </br>
   
   ```python
       docker run -it -p 8989:8989 -d --name tmddno1/tensormsa:v1
   ```   
   - Start CI Tool  </br>
 
   ```python
       docker run -it -p 8080:8080 -d --name tmddno1/jenkins:v1
   ```    
   
   - Check servers  </br>
   ```python
      TensorMSA : http://locahost:8989  
      Jenkins : http://locahost:8080  
      Hadoop :http://localhost:50070 
      Yarn : http://localhost:8088  
      Hbase : http://localhost:16010
   ``` 
# Docker - Settings 
   - Server information  
   ```python
      path : /home/dev/TensorMSA/TensorMSA/settings.py
      
      # custom setting need for tensormsa
      DATA_STORE_MODE = '1' # 1 (HDFS), 2(HIVE), 3(S3), 4(Local)
      LIVY_HOST = '8b817bad1154:8998'
      LIVY_SESS = '1'
      SPARK_HOST = '8b817bad1154:7077'
      SPARK_CORE = '1'
      SPARK_MEMORY = '1G'
      SPARK_WORKER_CORE = '2'
      SPARK_WORKER_MEMORY = '4G'
      FILE_ROOT = '/tensormsa'
      HDFS_HOST = '587ed1df9441:9000'
      HDFS_ROOT = '/tensormsa'
      HDFS_DF_ROOT = '/tensormsa/dataframe'
      HDFS_CONF_ROOT = '/tensormsa/config'
      HDFS_MODEL_ROOT = '/tensormsa/model'
   ```

# Docker Trouble Shooting 
  *[(Base Size Trouble Shooting)](http://wp.me/p7xrpI-ep)* : if you suffer "not enough space" related error with docker
  

# Install*[(link)](http://hugrypiggykim.com/2016/09/03/python-tensorflow-django-%ea%b0%9c%eb%b0%9c%ed%99%98%ea%b2%bd-%ea%b5%ac%ec%b6%95-%ec%a2%85%ed%95%a9/)*

<b>1.Install Anaconda </b> </br>
   - download Anaconda :  https://www.continuum.io/downloads
   - install (make sure anaconda works as default interpreter) 
   
   ```python
       bash /home/user/Downloads/Anaconda2-4.1.1-Linux-x86_64.sh
   ```
   ```python
       vi ~/.bashrc
       export PATH="$HOME/anaconda2/bin;$PATH"
   ```

<b>2.Install Tensorflow</b> </br>
   - install Tensorflow using conda </br>
   
   ```python
       conda create -n tensorflow python=2.7
       source activate tensorflow
       conda install -c conda-forge tensorflow
   ```

<b>3.Install Django</b> </br>
   - install Django, Django Rest Framework and Postgresql plugin</br>
   
   ```python
       [Django]
       conda install -c anaconda django=1.9.5
       [Django Rest Frame Work]
       conda install -c ioos djangorestframework=3.3.3
       [postgress plugin]
       conda install -c anaconda psycopg2=2.6.1
       [pygments]
       conda install -c anaconda pygments=2.1.3
   ```

<b>4.Install Postgresql</b> </br>

   - install</br>
   ```python
       yum install postgresql-server
   ```
   
   - check account and set pass</br>
   ```python
       cat /etc/passwd | grep postgres
       sudo passwd postgres
   ```
   
   - check PGDATA</br>
   ```python
       cat /var/lib/pgsql/.bash_profile
       env | grep PGDATA
   ```
   
   - init and run</br>
   ```python
       sudo -i -u postgres
       initdb
       pg_ctl start
       ps -ef | grep postgress
   ```
   
   - connect and create database</br>
   ```python
      # psql
       postgres=# create database tensormsa  ;
       postgres=# select *   from pg_database  ;
   ```  
   
   - create user for TesorMsA</br>
   ```python
       postgres=#CREATE USER tfmsauser WITH PASSWORD '1234';
       postgres=#ALTER ROLE tfmsauser SET client_encoding TO 'utf8'; 
       postgres=#ALTER ROLE tfmsauser SET default_transaction_isolation TO 'read committed'; 
       postgres=#ALTER ROLE testuser SET  imezone TO 'UTC';
       postgres=#GRANT ALL PRIVILEGES ON DATABASE tensormsa TO tfmsauser;
   ```

<b>5.get TensorMSA form git</b> </br>
   ```python
       git clone https://github.com/TensorMSA/TensorMSA.git
   ```

<b>5.migrate database</b> </br>
   - get to project folder where you can see 'manage.py'</br>

   ```python
       python manage.py makemigrations 
       python manage.py migrate
   ```

<b>6.run server</b> </br>
   - run server with bellow command</br>

   ```python
       ip addr | grep "inet "
       python manage.py runserver localhost:8989
   ```

# REST API / JAVA API Documents </br>
   - we are still on research process 
   - will be prepared on 2017
