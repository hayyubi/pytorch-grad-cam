import numpy as np
from pytorch_grad_cam.base_cam import BaseCAM


class XGradCAM(BaseCAM):
    def __init__(
            self,
            model,
            target_layers,
            use_cuda=False,
            reshape_transform=None,
            input_dict_key: str = None,
            out_dict_key=None):
        super(
            XGradCAM,
            self).__init__(
            model,
            target_layers,
            use_cuda,
            reshape_transform,
            input_dict_key=input_dict_key,
            out_dict_key=out_dict_key)

    def get_cam_weights(self,
                        input_tensor,
                        target_layer,
                        target_category,
                        activations,
                        grads):
        sum_activations = np.sum(activations, axis=(2, 3))
        eps = 1e-7
        weights = grads * activations / \
            (sum_activations[:, :, None, None] + eps)
        weights = weights.sum(axis=(2, 3))
        return weights
