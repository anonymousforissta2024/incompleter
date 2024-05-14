#Source: https://stackoverflow.com/questions/74549909/bentoml-localhost-server-returns-with-typeerror-runnermethod-object-is-not-ca
import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

BENTO_MODEL_TAG = "mmrt_model:p2ya6otlggzx4me4"

estimator_runner = bentoml.keras.get(BENTO_MODEL_TAG).to_runner()

MMRT_service = bentoml.Service("MMRT_Estimator", runners=[estimator_runner])

@MMRT_service.api(input=NumpyNdarray(), output=float)
def predict(input_data: np.ndarray) -> float:
    return estimator_runner.predict(input_data)