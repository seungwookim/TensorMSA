# -*- coding: utf-8 -*-
import os
from tfmsacore.utils.json_conv import JsonDataConverter
from tfmsacore.utils.logger import tfmsa_logger
from django.conf import settings

def chk_conf(net_id):
    """
    check if configuraiotn data exist with requested net id
    :param net_id: neural network id
    :return:
    --------------------------------------------------------------
    16.10.22  jh100  bugfix add "/" make folder od nnid
    """
    directory = settings.HDFS_CONF_ROOT + "/" + net_id + "/" #Bug fix by jh100 16.10.22
    net_id = net_id + "_conf.json"

    try:
        if os.path.isfile(directory + net_id):
            if(os.stat(directory + net_id).st_size == 0):
                return False
            else:
                return True
        else :
            return False
    except :
        return False


def load_conf(net_id):
    """
    load json from  path and return it as python object form
    :param net_id: neural network id
    :return:
    --------------------------------------------------------------
    16.10.22  jh100  bugfix add "/" make folder od nnid
    """
    directory = settings.HDFS_CONF_ROOT + "/" + net_id + "/" #Bug fix by jh100 16.10.22
    net_id = net_id + "_conf.json"

    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        model_conf = open(directory + net_id, 'r')
        json_data = JsonDataConverter().load_obj_json(model_conf)
        return json_data
    except Exception as e:
        print(e)
        raise Exception(e)
    finally :
        model_conf.close()



def load_ori_conf(net_id):
    """
    load json from  path and return it as str
    :param net_id: neural network id
    :return:
    --------------------------------------------------------------
    16.10.22  jh100  bugfix add "/" make folder od nnid
    """
    directory = settings.HDFS_CONF_ROOT + "/" + net_id + "/" #Bug fix by jh100 16.10.22
    net_id = net_id + "_conf.json"

    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        model_conf = open(directory +net_id, 'r')
        json_data = model_conf.read().split()
    except :
        raise SystemError("json load error")
    finally :
        model_conf.close()

    return json_data

def save_conf(net_id, conf_data):
    """
    save json format to json file
    :param net_id: neural network id
    :param conf_data: neural network configuration json data
    :return:
    --------------------------------------------------------------
    16.10.22  jh100  bugfix add "/" make folder od nnid
    """

    directory = settings.HDFS_CONF_ROOT + "/" + net_id + "/" #Bug fix by jh100 16.10.22
    net_id = net_id + "_conf.json"

    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        f = open(directory + net_id, 'w')
        if(isinstance(conf_data, (str))):
            f.write(conf_data)
        else :
            f.write(str(conf_data, 'utf-8'))
    except:
        raise SystemError("json conf save error")
    finally:
        f.close()


def remove_conf(net_id):
    """
    remove json from  path and return it as python object form
    :param net_id: neural network id
    :return:
    --------------------------------------------------------------
    16.10.22  jh100  bugfix add "/" make folder od nnid
    """
    directory = settings.HDFS_CONF_ROOT + "/" + net_id + "/" #Bug fix by jh100 16.10.22
    net_id = net_id + "_conf.json"

    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        if os.path.isfile(directory + net_id):
            os.remove(directory + net_id)
    except Exception as e:
        tfmsa_logger("removing conf fail : {0}".format(e))
        raise Exception(e)