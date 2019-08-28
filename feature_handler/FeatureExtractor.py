import pandas as pd
import os
from feature_handler.FeatureCalculator import FeatureCalculator
global dataset_path
global sauces

dataset_path = 'C:\\Users\\Saimon\\Desktop\\dataset_iot'
sauces = ['ketchup', 'mayo', 'soy']


class FeatureExtractor:

    @staticmethod
    def convert_differences(volumes):

        diff_list = []
        for i in range(len(volumes) - 1):
            diff_list.append(volumes[i+1] - volumes[i])
        return diff_list

    @staticmethod
    def peak_build(diff_list):
        peak = []
        peaks = []
        for interval in diff_list:
            if interval > 0:
                peak.append(interval)
            elif len(peak) > 0:
                df = pd.DataFrame(peak, columns=['diff'])
                peaks.append(df)
                peak = []

        if len(peak) != 0:
            df = pd.DataFrame(peak, columns=['diff'])
            peaks.append(df)
        return peaks

    @staticmethod
    def extract_dataset(csv_path='test1.csv'):
        dict_list = []
        for dirName, subdirList, fileList in os.walk(os.path.join(dataset_path)):
            for fname in fileList:
                if fname.endswith('.csv'):
                    df = pd.read_csv(os.path.join(dirName, fname))
                    peak_list = FeatureExtractor.peak_build(FeatureExtractor.convert_differences(volumes=df['volume']))
                    if 'ketchup' in fname:
                        sauce_type = sauces[0]
                    elif 'mayo' in fname:
                        sauce_type = sauces[1]
                    else:
                        sauce_type = sauces[2]

                    for peak in peak_list:
                        dict_row = {}
                        fc = FeatureCalculator(peak)
                        dict_row.update([('sum', fc.sum_change()), ('mean', fc.mean_change()), ('std', fc.std_change()),
                                         ('var', fc.var_change()), ('max', fc.max_change()), ('min', fc.min_change()),
                                         ('size', fc.size_change()), ('label', sauce_type)])
                        dict_list.append(dict_row)
        df = pd.DataFrame(dict_list)
        df.to_csv(csv_path)

    @staticmethod
    def convert_sample(last_values):
        dict_row = {}
        df = pd.DataFrame(FeatureExtractor.convert_differences(last_values), columns=['diff'])
        fc = FeatureCalculator(df)
        dict_row.update([('sum', fc.sum_change()), ('mean', fc.mean_change()), ('std', fc.std_change()),
                         ('var', fc.var_change()), ('max', fc.max_change()), ('min', fc.min_change()),
                         ('size', fc.size_change())])
        return dict_row


if __name__ == "__main__":
    FeatureExtractor.extract_dataset()