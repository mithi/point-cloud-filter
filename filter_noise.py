import pcl

##################################################################################
# This pipeline reduces the statistical noise of the scene 

# port of http://pointclouds.org/documentation/tutorials/statistical_outlier.php
# download http://svn.pointclouds.org/data/tutorials/table_scene_lms400.pcd

point_cloud = pcl.load("point_clouds/table_scene_lms400.pcd")

noise_filter = point_cloud.make_statistical_outlier_filter()

# Set the number of neighboring points to analyze for any given point
noise_filter.set_mean_k(50)

# Any point with a mean distance larger than global (mean distance+x*std_dev)
# will be considered outlier
noise_filter.set_std_dev_mul_thresh(1.0)

pcl.save(noise_filter.filter(), "point_clouds/table_scene_lms400_inliers.pcd")

noise_filter.set_negative(True)
pcl.save(noise_filter.filter(), "point_clouds/table_scene_lms400_outliers.pcd")


