from rest_framework import serializers

from tfmsacore import models


class NNInfoSerializer(serializers.ModelSerializer):
    """
    Table : store Neural Network base information
    """
    class Meta:
        model = models.NNInfo
        fields = ('nn_id', 'category', 'subcate', 'name', 'desc', 'type', 'acc', 'train', 'config', 'dir', 'table',
                  'query', 'preprocess', 'datadesc', 'datasets', 'imagex', 'imagey', 'imagepre', 'datavaild',
                  'confvaild', 'samplepercent', 'samplenum', 'samplemethod', 'testpass', 'testfail'  )



class JobManagementSerializer(serializers.ModelSerializer):
    """
    Table : Train Job Tracker
    """
    class Meta:
        model = models.JobManagement
        fields = ('nn_id', 'type','request', 'start', 'end', 'status', 'progress', 'acc', 'epoch', 'testsets',
                  'datapointer', 'endpointer', 'batchsize')


class ServerConfSerializer(serializers.ModelSerializer):
    """
    Table : ServerConf
    """
    class Meta:
        model = models.ServerConf
        fields = ('version', 'state', 'store_type', 'fw_capa', 'livy_host', 'livy_sess', 'spark_host', 'spark_core',
                  'spark_memory', 'hdfs_host', 'hdfs_root', 's3_host', 's3_access', 's3_sess', 's3_bucket')


class TrainResultLossSerializer(serializers.ModelSerializer):
    """
    Table : TrainResultLoss
    """
    class Meta:
        model = models.TrainResultLoss
        fields = ('nn_id', 'key', 'loss', 'step', 'max_step', 'trainDate', 'testsets')

class TrainResultAccSerializer(serializers.ModelSerializer):
    """
    Table : TrainResultAcc
    """
    class Meta:
        model = models.TrainResultAcc
        fields = ('nn_id', 'key', 'label', 'guess', 'ratio')

class DataSchemaCategorySerializer(serializers.ModelSerializer):
    """
    Table : DataSchemaCategory
    """
    class Meta:
        model = models.DataSchemaCategory
        fields = ('schema', 'filetype', 'datastep', 'category', 'subcate', 'order')

class MetaCategorySerializer(serializers.ModelSerializer):
    """
    Table : MetaCategory
    """
    class Meta:
        model = models.MetaCategory
        fields = ('category_id', 'category_name', 'desc', 'order')

class MetaSubCategorySerializer(serializers.ModelSerializer):
    """
    Table : MetaSubCategory
    """
    class Meta:
        model = models.MetaSubCategory
        fields = ('category_id', 'subcateogry_id', 'subcategory_name', 'desc', 'order')

class DataTableInfoSerializer(serializers.ModelSerializer):
    """
    Table : MetaSubCategory
    """
    class Meta:
        model = models.DataTableInfo
        fields = ('table_name', 'col_len', 'row_len')