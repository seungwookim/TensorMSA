import json
from rest_framework.response import Response
from rest_framework.views import APIView
from tfmsacore.utils.json_conv import JsonDataConverter as jc
from tfmsacore.evaluation import eval_conv_network
from tfmsacore import netconf

class ConvNeuralNetEval(APIView):
    """
    1. Name : ConvNeuralNetEval
    2. Steps - CNN essential steps
        - post /api/v1/type/common/env/
        - post /api/v1/type/common/nninfo/{nnid}/
        - post /api/v1/type/imagedata/base/{baseid}/
        - post /api/v1/type/imagedata/base/{baseid}/table/{tb}/
        - post /api/v1/type/imagedata/base/{baseid}/table/{tb}/label/{label}/data/
        - post /api/v1/type/imagedata/base/{baseid}/table/{tb}/label/{label}/data/{args}/
        - post /api/v1/type/imagedata/base/{baseid}/table/{tb}/label/{label}/format/{nnid}/
        - post /api/v1/type/imagedata/base/{baseid}/table/{tb}/label/{label}/format/{nnid}/
        - post /api/v1/type/cnn/conf/{nnid}/
        - post /api/v1/type/cnn/train/{nnid}/
        - post /api/v1/type/cnn/eval/{nnid}/
        - post /api/v1/type/cnn/predict/{nnid}/
    3. Description \n
        Evaluate Network accuracy
    """

    # read
    def post(self, request, nnid):
        """
        - desc : evaluate train result
        """
        try:
            netconf.set_off_eval(nnid)
            jd = jc.load_obj_json(str(request.body, 'utf-8'))
            result = eval_conv_network(nnid, jd.samplenum, jd.samplemethod)
            return_data = {"status": "ok", "result": result}
            netconf.set_on_eval(nnid)
            return Response(json.dumps(return_data))
        except Exception as e:
            return_data = {"status": "404", "result": str(e)}
            return Response(json.dumps(return_data))
