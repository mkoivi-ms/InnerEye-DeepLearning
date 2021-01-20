from InnerEye.ML.configs.segmentation.Lung import Lung  

class LungExt(Lung):
    def __init__(self) -> None:
        super().__init__(azure_dataset_id="lung")