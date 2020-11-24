import numpy as np
import open3d
pcd = open3d.geometry.PointCloud()
np_points = np.random.rand(100, 3)

# From numpy to Open3D
pcd.points = open3d.utility.Vector3dVector(np_points)

# From Open3D to numpy
np_points = np.asarray(pcd.points)

open3d.visualization.draw_geometries([pcd],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])
