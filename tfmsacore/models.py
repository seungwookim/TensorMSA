from django.db import models


class NNInfo(models.Model):
    nn_id = models.CharField(max_length=10, blank=False, primary_key=True)       # unique key name (nn00000001)
    category = models.CharField(max_length=10, blank=False)                      # business category
    subcate = models.CharField(max_length=10, blank=False)                       # business sub category
    name = models.CharField(max_length=100, blank=True, default='')              # business name
    desc = models.CharField(max_length=5000, blank=True, default='')             # description for network
    type = models.CharField(max_length=100, blank=True, default='')              # network types
    acc = models.CharField(max_length=20, blank=True, default='')                # accuracy of model from last training
    train = models.CharField(max_length=1, blank=True, default='')               # if trained model exist  (Y,N)
    config = models.CharField(max_length=1, blank=True, default='')              # if config exist (Y, N)
    dir = models.CharField(max_length=200, blank=True, default='')               # path where conf files saved
    table = models.CharField(max_length=100, blank=True, default='')             # table name to get data
    query = models.CharField(max_length=5000, blank=True, default='')            # SQL query to get data
    preprocess = models.CharField(max_length=50, blank=True, default='')         # preprocess type (1, dataframe, 2, image, ..etc)
    datadesc = models.CharField(max_length=50000, blank=True, default='')        # if data format specified (null = N, len>0 = Y)
    datasets = models.CharField(max_length=50000, blank=True, default='')        # if data preprocess done (null = N, eln>0 = Y)
    datasize = models.CharField(max_length=50, blank=True, default='')           # length of data read from spark at once
    imagex = models.CharField(max_length=50, blank=True, default='')             # image prerpcoess x size
    imagey = models.CharField(max_length=50, blank=True, default='')             # image preprocess y size
    imagepre = models.CharField(max_length=1, blank=True, default='')            # if image preprocessed (Y,N)
    datavaild = models.CharField(max_length=1, blank=True, default='')           # vaildation check for data (Y,N)
    confvaild = models.CharField(max_length=1, blank=True, default='')           # validation check for conf (Y,N)
    samplepercent = models.CharField(max_length=1000, blank=True, default='')    # percentage of sampling from raw data
    samplenum = models.CharField(max_length=1000, blank=True, default='')        # number of samples for test
    samplemethod = models.CharField(max_length=10, blank=True, default='')       # samplling method (1 : random)
    testpass = models.CharField(max_length=1000, blank=True, default='')         # number of match
    testfail = models.CharField(max_length=1000, blank=True, default='')         # number of unmatch
    created = models.DateTimeField(auto_now_add=True)                            # day created

    def json(self):
        return dict(
            nn_id = self.nn_id,
            category=self.category,
            subcate=self.subcate,
            name=self.name,
            desc=self.desc,
            type=self.type,
            acc=self.acc,
            train=self.train,
            config=self.config,
            dir=self.dir,
            table=self.table,
            query=self.query,
            preprocess=self.preprocess,
            datadesc=self.datadesc,
            datasets=self.datasets,
            datasize=self.datasize,
            imagex=self.imagex,
            imagey=self.imagey,
            imagepre=self.imagepre,
            datavaild=self.datavaild,
            confvaild=self.confvaild,
            samplepercent=self.samplepercent,
            samplenum=self.samplenum,
            samplemethod=self.samplemethod,
            testpass=self.testpass,
            testfail=self.testfail
        )

    def __getitem__(self, item):
        return self.__dict__[item]


class JobManagement(models.Model):
    nn_id = models.CharField(max_length=10, blank=False, primary_key=True)                  # neural network key
    type = models.CharField(max_length=10, blank=False , default='')                        # init(0), preprocess(1), training(2)
    request = models.DateTimeField(auto_now_add=False, null=True, blank=True )              # time job registerd
    start = models.DateTimeField(auto_now_add=False, null=True, blank=True )                # time job started
    end = models.DateTimeField(auto_now_add=False, null=True, blank=True )                  # time job finished
    status = models.CharField(max_length=3, blank=True, default='')                         # request(1), running(3), finish(5), error(9)
    progress = models.CharField(max_length=3, blank=True, default='')                       # data(10), pre(30), train(50), evaluation(70), finish(100)
    acc = models.CharField(max_length=5, blank=True, default='')                            # accuracy of model from last training
    epoch = models.CharField(max_length=20, blank=True, default='')                         # itetraions time of training
    testsets = models.CharField(max_length=20, blank=True, default='')                      # number of evaluation data set
    datapointer = models.CharField(max_length=100, blank=True, default='')                  # current data pointer (used when data is too big)

    def json(self):
        return dict(
            nn_id = self.nn_id,
            type=self.type,
            request=str(self.request),
            start=str(self.start),
            end=str(self.end),
            status=self.status,
            progress=self.progress,
            acc=self.acc,
            epoch = self.epoch,
            testsets = self.testsets
        )

    def __getitem__(self, item):
        return self.__dict__[item]


class ServerConf(models.Model):
    version = models.AutoField(primary_key=True)                                 # version id (primary)
    state = models.CharField(max_length=1, blank=True, default='')               # A(alive) , D(Dead)
    store_type = models.CharField(max_length=10, blank=True, default='')         # choose hdfs(0), hbase(1), s3(2)
    fw_capa = models.CharField(max_length=5, blank=True, default='')             # maximum training capa at once
    livy_host = models.CharField(max_length=100, blank=True, default='')         # livy host (ip : port)
    livy_sess = models.CharField(max_length=5, blank=True, default='')           # livy max spark session
    spark_host = models.CharField(max_length=100, blank=True, default='')        # spark host (ip : port)
    spark_core = models.CharField(max_length=5, blank=True, default='')          # spark core limit per session
    spark_memory = models.CharField(max_length=10, blank=True, default='')       # spark memory limit per session
    hdfs_host = models.CharField(max_length=100, blank=True, default='')         # hdfs host (ip : port)
    hdfs_root = models.CharField(max_length=50, blank=True, default='')          # hdfs file root
    s3_host = models.CharField(max_length=100, blank=True, default='')           # aws host (ip : port)
    s3_access = models.CharField(max_length=100, blank=True, default='')         # aws access key
    s3_sess = models.CharField(max_length=100, blank=True, default='')           # aws session key
    s3_bucket = models.CharField(max_length=100, blank=True, default='')         # aws bucket name

    def json(self):
        return dict(
            version = self.version,
            state=self.state,
            store_type=self.store_type,
            fw_capa=self.fw_capa,
            livy_host=self.livy_host,
            livy_sess=self.livy_sess,
            spark_host=self.spark_host,
            spark_core=self.spark_core,
            spark_memory=self.spark_memory,
            hdfs_host=self.hdfs_host,
            hdfs_root=self.hdfs_root,
            s3_host=self.s3_host,
            s3_access=self.s3_access,
            s3_sess=self.s3_sess,
            s3_bucket=self.s3_bucket
        )

    def __getitem__(self, item):
        return self.__dict__[item]


class TrainResults(models.Model):
    nn_id = models.CharField(max_length=10, blank=True, default='')                           # neural network key
    loss = models.CharField(max_length=10, blank=True, default='')                          # loss
    step = models.CharField(max_length=10, blank=True, default='')                          # current step
    max_step = models.CharField(max_length=10, blank=True, default='')                      # final step
    trainDate = models.CharField(max_length=20, blank=True, default='')                     # train date
    testsets = models.CharField(max_length=20, blank=True, default='')                      # number of evaluation data set

   #nnid	loss	step	max_step	traningdate	train_num
    def json(self):
        return dict(
            nn_id = self.nn_id,
            loss=self.loss,
            step=self.step,
            max_step=self.max_step,
            trainDate=self.trainDate,
            testsets = self.testsets
        )


    def __getitem__(self, item):
        return self.__dict__[item]
