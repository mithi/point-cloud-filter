# point-cloud-filter

Given point cloud data, we apply techniques to separate our object of interest.
You can learn more about [PCL here](http://pointclouds.org/documentation/tutorials/).

This is the [first perception exercise](https://github.com/udacity/RoboND-Perception-Exercises/tree/master/Exercise-1) 
from [Udacity's RoboND](https://www.udacity.com/robotics).

The scripts showcase the following techniques:
- Downsampling using the Voxel Grid Filter
- Getting the region of interest using a passthrough filter
- Segmentation of the table from everything else using Ransac Plane Fitting
- Reducing noise using statistical outlier filter

# Original Point Cloud
![Original Point Cloud](https://github.com/mithi/point-cloud-filter/blob/master/screenshots/table_top.png)

# Resulting Point Cloud
![Objects](https://github.com/mithi/point-cloud-filter/blob/master/screenshots/objects.png)

# Dependencies
- Python 2.7, this does not work on Python 3
- [PCL bindings](https://github.com/udacity/RoboND-Perception-Exercises/tree/master/python-pcl) by [Straw Lab](http://strawlab.org/)
- PCL tools `$ sudo apt-get install pcl-tools`
- I used Ubuntu 16.04.2 with ROS full-desktop-version

# Viewing Point Cloud Results
- The resulting point clouds can be found in the `/point_cloud` folder, you can view them with the ff command:
```
$ pcl_viewer filename.pcd 
```

# Running scripts
- There are three python scripts you can run all of which are commented well. 
```
$ python filename.py
```

# Original Table Scene
![Original Table Scene](https://github.com/mithi/point-cloud-filter/blob/master/screenshots/table_scene.png)

# Table Scene with Reduced Noise
![Table Scene with Reduced Noise](https://github.com/mithi/point-cloud-filter/blob/master/screenshots/table_scene_inliers.png)


