import matplotlib.pyplot as plt
import pandas as np
import configparser 
import os

def graph(df: np.DataFrame):

    plt.plot(df['Timestamp'], df['Avg_price'])
    plt.xlabel('Timestamp')
    plt.ylabel('Average price')
    plt.title('BTC to USD price')

    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_path)

    print(f"Saving file into {config.get('graph', 'dir')}")
    data_path = config.get('graph', 'dir')
    data_filename = config.get('graph', 'filename')
    file_path = os.path.join(data_path, data_filename)

    plt.savefig(file_path)
