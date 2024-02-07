# FusionPortable_dataset_tools

### Download
1. Please visit [FusionPortable dataset](https://fusionportable.github.io/dataset/fusionportable) to check and download data.
2. Download the compressed rosbag.
3. When finished, use the similar command ```7z e 20220216_garden_day.7z``` to extract data.

<!-- ### Notice 20230928
Please add this line in ```/etc/hosts```: ```143.89.6.5 www.ram-lab.com filebrowser.ram-lab.com``` to visit the dataset page. -->

### Installation
Clone the Repo
```
git clone https://github.com/HKUSTGZ-IADC/iadc_dataset_tools.git
cd iadc_dataset_tools
```
Setup the Python environment (tested on Python-3.9), or using Anaconda
```
conda create -n fp_dataset python=3.9
pip install -r requirements
```

### Usage
1. Open the ```write_rosbag_to_files.ipynb``` and ```run all``` to convert the rosbag into individual raw files


### Some Issues with Dependencies
1. Something wrong with the ```ros_numpy```
```python
File ~/anaconda3/envs/fp_dataset/lib/python3.9/site-packages/ros_numpy/point_cloud2.py:224
    221             new_cloud_arr[field_name] = cloud_arr[field_name]
...
AttributeError: module 'numpy' has no attribute 'float'.
```
Please goto ```~/anaconda3/envs/fp_dataset/lib/python3.9/site-packages/ros_numpy/point_cloud2.py:224``` and replace the original line with
```python
def get_xyz_points(cloud_array, remove_nans=True, dtype=np.float64):
```

### Inquiry
Please feel free to contact Dr.Jianhao Jiao (jiaojh1994 at gmail.com) or Mr.Hexiang Wei (hweiak at connect.ust.hk) if you have any questions.
