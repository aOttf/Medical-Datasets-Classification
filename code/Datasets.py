import pandas as pd
import numpy as np


def load_cancer():
    # data, target, feature_names
    result_dict = {'features': np.array(["Clump Thickness",
                                         "Uniformity of Cell Size",
                                         "Uniformity of Cell Shape",
                                         "Marginal Adhesion",
                                         "Single Epithelial Cell Size",
                                         "Bare Nuclei",
                                         "Bland Chromatin",
                                         "Normal Nucleoli",
                                         "Mitoses"])}

    df_dict = pd.read_csv('breast_cancer_wisconsin.csv', header=0).to_dict('split')
    df_data = np.array(df_dict['data'])
    result_dict['data'] = df_data[:, :-1]
    result_dict['target'] = df_data[:, -1]
    return result_dict


def load_hepatitis():
    result_dict = {'features': np.array(["AGE",
                                         "SEX",
                                         "STEROID",
                                         "ANTIVIRAL",
                                         "FATIGUE",
                                         "MALAISE",
                                         "ANOREXIA",
                                         "LIVER BIG",
                                         "LIVER FIRM",
                                         "SPLEEN PALPABLE",
                                         "SPIDERS",
                                         "ASCITES",
                                         "VARICES",
                                         "BILIRUBIN",
                                         "ALK PHOSPHATE",
                                         "SGOT",
                                         "ALBUMIN",
                                         "PROTIME",
                                         "HISTOLOGY"])
                   }

    df_dict = pd.read_csv('hepatitis.csv', header=0).to_dict('split')
    df_data = np.array(df_dict['data'])
    result_dict['data'] = df_data[:, 1:]
    result_dict['target'] = (df_data[:, 0]).astype(int)
    return result_dict
