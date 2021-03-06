import json
from rest_framework.response import Response
from rest_framework.views import APIView
from tfmsacore import netconf
from tfmsacore import service
from TensorMSA import const


class WideDeepNetTrain(APIView):
    """
    1. Name : WideDeepNetTrain (step 8)
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
        Manage data store data CRUD (strucutre : schema - table - data)
    """

    def post(self, request, nnid):
        """
        - desc : train requested model and save
        """
        try:
            result = service.JobManager().regit_job(nnid, const.JOB_TYPE_WDNN_TRAIN)
            return_data = {"status": "200", "result": result}
            print("wdnn_Tran result" + str(return_data))
            return Response(json.dumps(return_data))
        except Exception as e:
            netconf.set_off_train(nnid)
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))
