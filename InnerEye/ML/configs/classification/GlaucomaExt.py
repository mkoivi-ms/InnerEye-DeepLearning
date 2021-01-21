from InnerEye.ML.configs.classification.GlaucomaPublic import GlaucomaPublic  

class GlaucomaExt(GlaucomaPublic):
    def __init__(self) -> None:
        super().__init__(azure_dataset_id="glaucoma")