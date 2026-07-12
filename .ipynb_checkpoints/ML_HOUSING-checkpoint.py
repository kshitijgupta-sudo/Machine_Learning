#CHECKING SYSTEM CONFIGURATION
import sys
assert sys.version_info >= (3,7)

#CHECKING DEPENDENCIES
from packaging import version 
import sklearn
assert version.parse(sklearn.__version__) >= version.parse("1.0.1")

#Welcome to Machine Learning Housing Corp.! 
#Your task is to predict median house values in Californian districts, given a number of features 
#from these districts.

#Download the Data

from pathlib import Path
import pandas as pd
import tarfile
import urllib.request


def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("Datasets").mkdir(parents=True , exist_ok = True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
    
    with tarfile.open(tarball_path) as housing_tarball:
        housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))


housing = load_housing_data()

#QUICK LOOK AT THE DATA
housing.head()


#extra code - to save the graphs to be plotted as high-res pngs
IMAGES_PATH = Path() / "images" / "ML SCKIKILIT"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)


import matplotlib.pyplot as plt

# extra code – the next 5 lines define the default font sizes
plt.rc('font', size=14)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

housing.hist(bins=50, figsize=(12, 8))
save_fig("attribute_histogram_plots")  # extra code
plt.show()
