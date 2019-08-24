from bigml.model import Model


class BIGML_Model:

    def __init__(self, model_path='model/5d598906eba31d627e0007b6'):
        self.model = Model(model_path)
        self.model.get_data_distribution()

    def get_predict(self, sample_dict):
        return self.model.predict(sample_dict)

    def get_data_distribution(self):
        return self.model.get_data_distribution()
