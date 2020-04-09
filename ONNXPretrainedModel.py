import onnxruntime as rt
import numpy as np

class ONNXPretrainedModel(object):
    '''
    ONNXPretrainedModel

    Acts just like an sklearn model you've already trained.

    Supported API:
    * predict(x_test)

    Just a thin wrapper around an ONNX session.
    '''

    def __init__(self, file_path=None):
        self.sess = rt.InferenceSession(file_path)
        self.input_name = self.sess.get_inputs()[0].name
        self.label_name = self.sess.get_outputs()[0].name

    def predict(self, x_ND):
        ''' Make predictions given input features 

        Args
        ----
        x_ND : 2D array, shape (N, D) = (n_examples, n_dims)
            Input features dataset
            Row n provides the D-dim feature vector for n-th example

        Returns
        -------
        yhat_N : 1D array, shape (N,1)
            Predictions for each provided example
        '''
        yhat_N = self.sess.run(
            [self.label_name],
            {self.input_name: x_ND.astype(np.float32)})[0]
        return yhat_N

