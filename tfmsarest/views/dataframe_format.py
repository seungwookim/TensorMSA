import json
from rest_framework.response import Response
from rest_framework.views import APIView
from tfmsacore.utils import CusJsonEncoder
from tfmsacore import data
from tfmsacore.utils.json_conv import JsonDataConverter as jc
from tfmsacore import netconf

class DataFrameFormat(APIView):
    """
    1. Name : DataFrameData (step 6)
    2. Steps - WDNN essential steps
        - post /api/v1/type/common/env/
        - post /api/v1/type/common/job/{nnid}/
        - post /api/v1/type/dataframe/base/{baseid}/table/{tb}/
        - post /api/v1/type/dataframe/base/{baseid}/table/{tb}/data/
        - post /api/v1/type/dataframe/base/{baseid}/table/{tb}/data/{args}/
        - post /api/v1/type/dataframe/base/{baseid}/table/{tb}/format/{nnid}/
        - post /api/v1/type/wdnn/conf/{nnid}/
        - post /api/v1/type/wdnn/train/{nnid}/
        - post /api/v1/type/wdnn/eval/{nnid}/
        - post /api/v1/type/wdnn/predict/{nnid}/
    3. Description \n
        Manage Data Structure (Column type, Combine Columns)
    """
    def post(self, request, baseid, tb, nnid):
        """
        - desc : create a format data
        - desc : update data format information \n
            <textfield>
            <font size = 1>

                { "cross_cell":
                    {
                      "col12": {"column2_0": "native_country", "column2_1": "occupation"},
                      "col1": {"column_1": "occupation", "column_0": "education"}
                    },
                  "cell_feature":
                    {
                      "hours_per_week": "CONTINUOUS_COLUMNS",
                      "native_country": "CATEGORICAL",
                      "relationship": "CATEGORICAL",
                      "gender": "CATEGORICAL",
                      "age": "CONTINUOUS_COLUMNS",
                      "marital_status": "CATEGORICAL",
                      "race": "CATEGORICAL",
                      "capital_gain": "CONTINUOUS_COLUMNS",
                      "workclass": "CATEGORICAL",
                      "capital_loss": "CONTINUOUS_COLUMNS",
                      "education": "CATEGORICAL",
                      "education_num": "CONTINUOUS_COLUMNS",
                      "occupation": "CATEGORICAL"
                    },
                  "label":
                    {
                       "income_bracket" : "LABEL"
                    }
                }
            </font>
            </textfield>
            ---
            parameters:
            - name: body
              paramType: body
              pytype: json
        """
        try:
            jd = jc.load_obj_json("{}")
            jd.dir = baseid
            jd.table = tb
            jd.nn_id = nnid
            jd.datadesc = str(request.body,'utf-8')
            netconf.save_format(nnid, str(request.body,'utf-8'))
            result = netconf.update_network(jd)
            netconf.set_on_data(nnid)
            netconf.set_on_data_conf(nnid)
            return_data = {"status": "200", "result": result}
            return Response(json.dumps(return_data))
        except Exception as e:
            netconf.set_off_data(nnid)
            netconf.set_off_data_conf(nnid)
            return_data = {"status": "400", "result": str(e)}
            return Response(json.dumps(return_data))

    def get(self, request, baseid, tb, nnid):
        """
        - desc : return network data format information
        """
        try:
            result = netconf.load_ori_format()(nnid, request.body)
            return_data = {"status": "200", "result": result}
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "400", "result": str(e)}
            return Response(json.dumps(return_data))

    def put(self, request, baseid, tb, nnid):
        """
        - desc : update data format information
        """
        try:
            jd = jc.load_obj_json("{}")
            jd.dir = baseid
            jd.table = tb
            jd.nn_id = nnid
            jd.datadesc = 'Y'
            netconf.remove_format(nnid)
            netconf.save_format(nnid, request.body)
            result = netconf.update_network(jd)
            return_data = {"status": "200", "result": result}
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "400", "result": str(e)}
            return Response(json.dumps(return_data))

    def delete(self, request, baseid, tb, nnid):
        """
        - desc : delete data format information
        """
        try:
            jd = jc.load_obj_json("{}")
            jd.dir = ""
            jd.table = ""
            jd.nn_id = nnid
            jd.datadesc = ""
            netconf.remove_format(nnid)
            result = netconf.update_network(jd)
            netconf.set_on_data(nnid)
            netconf.set_on_data_conf(nnid)
            return_data = {"status": "200", "result": result}
            return Response(json.dumps(return_data))
        except Exception as e:
            netconf.set_off_data(nnid)
            netconf.set_off_data_conf(nnid)
            return_data = {"status": "400", "result": str(e)}
            return Response(json.dumps(return_data))

