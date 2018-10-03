from dataset_generation import *
from bs4 import BeautifulSoup
import os
import codecs
from classifier_generation import *


def create_csv_datasets():

    for page_html in os.listdir('/home/arnaud/Desktop/ML_process_file/WebPageAlgo/NewPageWeb/'):
       page = codecs.open("/home/arnaud/Desktop/ML_process_file/WebPageAlgo/NewPageWeb/%s" % page_html, 'r')
       page = page.read()
       soup = BeautifulSoup(page, "lxml")
       df_derived_features = get_derived_features_filtered(soup)

       file = df_derived_features.to_csv('/home/arnaud/Desktop/ML_process_file/file_csv/csv/%s.csv' % page_html.replace(".html",""), sep=',', encoding='utf-8')


def merge_csv_datasets_into_df():

    dataset = []
    for file_csv in os.listdir('/home/arnaud/Desktop/ML_process_file/file_csv/'):
        with open('/home/arnaud/Desktop/ML_process_file/file_csv/%s' % file_csv) as f:
             dataframe = pd.read_csv(f)
             dataset.append(dataframe)

    data = pd.concat(dataset, ignore_index=True)

    file = data.to_csv('/home/arnaud/Desktop/ML_process_file/DATA_all1.csv', sep=',', encoding='utf-8')



if __name__ == "__main__":

   create_csv_datasets()

   merge_csv_datasets_into_df()
