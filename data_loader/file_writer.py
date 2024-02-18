#!/usr/bin/python3
import os
import sys
import numpy as np

class FileWriter():
  def __init__(self):
    pass

  def write_timestamp(self, timestamps, file_path):
    with open(file_path, 'w') as file:
      for time in timestamps:
        file.write('{:9f}\n'.format(time))

  def write_kitti_calibration_intrinsics(self, platform, int_ext_loader, file_path):
    """
    Writes the KITTI camera intrinsics to a file.

    Args:
        platform: The platform on which the data was collected. Can be 'vehicle' or 'frame'.
        int_ext_loader: The Intrinsics and Extrinsics loader object.
        file_path: The path to the file to write the intrinsics to.

    Returns:
        None

    """
    with open(file_path, 'w') as file:
      if platform == 'vehicle':
        T = int_ext_loader.tf_graph.get_relative_transform('vehicle_frame_cam00', 'body_imu')[:3, :4]
        str = 'image_00: ' + ' '.join('{:9f}'.format(x) for x in T.flatten()) + '\n'
        file.write(str)
        T = int_ext_loader.tf_graph.get_relative_transform('vehicle_frame_cam01', 'body_imu')[:3, :4]
        str = 'image_01: ' + ' '.join('{:9f}'.format(x) for x in T.flatten()) + '\n'
        file.write(str)
      else:
        T = int_ext_loader.tf_graph.get_relative_transform('frame_cam00', 'body_imu')[:3, :4]
        str = 'image_00: ' + ' '.join('{:9f}'.format(x) for x in T.flatten()) + '\n'
        file.write(str)
        T = int_ext_loader.tf_graph.get_relative_transform('frame_cam01', 'body_imu')[:3, :4]
        str = 'image_01: ' + ' '.join('{:9f}'.format(x) for x in T.flatten()) + '\n'
        file.write(str)

      T = int_ext_loader.tf_graph.get_relative_transform('event_cam00', 'body_imu')[:3, :4]
      str = 'image_02: ' + ' '.join('{:9f}'.format(x) for x in T.flatten()) + '\n'
      file.write(str)
      T = int_ext_loader.tf_graph.get_relative_transform('event_cam01', 'body_imu')[:3, :4]
      str = 'image_03: ' + ' '.join('{:9f}'.format(x) for x in T.flatten()) + '\n'
      file.write(str)

  def write_kitti_calibration_extrinsics(self, platform, int_ext_loader, file_path):
    """
    Writes the KITTI camera extrinsics to a file.

    Args:
        platform (str): The platform on which the calibration was performed.
            Can be either 'vehicle' or 'frame'.
        int_ext_loader (IntExtLoader): The IntExtLoader object used to load
            the intrinsic and extrinsic parameters.
        file_path (str): The path to the file where the extrinsics will be
            written.

    Returns:
        None

    """
    with open(file_path, 'w') as file:
      if platform == 'vehicle':
        base_frame_id = 'vehicle_frame_cam00'
        sensor_left_frame_camera = 'vehicle_frame_left_camera'
        sensor_right_frame_camera ='vehicle_frame_right_camera'
      else:
        base_frame_id = 'frame_cam00'
        sensor_left_frame_camera = 'frame_left_camera'
        sensor_right_frame_camera = 'frame_right_camera'
        
      sensor_left_event_camera = 'event_left_camera'
      sensor_right_event_camera = 'event_right_camera'

      ##### Frame camera
      camera = int_ext_loader.sensor_collection[sensor_left_frame_camera]
      T = int_ext_loader.tf_graph.get_relative_transform(camera.frame_id, base_frame_id)
      file.write('calib_time: {}\n'.format(camera.dataset_name))
      file.write('corner_dist: 0.1\n')
      file.write('S_00: {} {}\n'.format(camera.width, camera.height))
      file.write('K_00: {} {} {} {} {} {} {} {} {}\n'.format(camera.K[0][0], camera.K[0][1], camera.K[0][2], camera.K[1][0], camera.K[1][1], camera.K[1][2], camera.K[2][0], camera.K[2][1], camera.K[2][2]))
      file.write('D_00: {} {} {} {} {}\n'.format(camera.D[0][0], camera.D[0][1], camera.D[0][2], camera.D[0][3], camera.D[0][4]))
      file.write('R_00: {} {} {} {} {} {} {} {} {}\n'.format(T[0][0], T[0][1], T[0][2], T[1][0], T[1][1], T[1][2], T[2][0], T[2][1], T[2][2]))
      file.write('T_00: {} {} {}\n'.format(T[0][3], T[1][3], T[2][3]))
      file.write('S_rect_00: {} {}\n'.format(camera.width, camera.height))
      file.write('R_rect_00: {} {} {} {} {} {} {} {} {}\n'.format(T[0][0], T[0][1], T[0][2], T[1][0], T[1][1], T[1][2], T[2][0], T[2][1], T[2][2]))
      file.write('P_rect_00: {} {} {} {} {} {} {} {} {}\n'.format(camera.K[0][0], camera.K[0][1], camera.K[0][2], camera.K[1][0], camera.K[1][1], camera.K[1][2], camera.K[2][0], camera.K[2][1], camera.K[2][2]))

      camera = int_ext_loader.sensor_collection[sensor_right_frame_camera]
      T = int_ext_loader.tf_graph.get_relative_transform(camera.frame_id, base_frame_id)
      file.write('S_01: {} {}\n'.format(camera.width, camera.height))
      file.write('K_01: {} {} {} {} {} {} {} {} {}\n'.format(camera.K[0][0], camera.K[0][1], camera.K[0][2], camera.K[1][0], camera.K[1][1], camera.K[1][2], camera.K[2][0], camera.K[2][1], camera.K[2][2]))
      file.write('D_01: {} {} {} {} {}\n'.format(camera.D[0][0], camera.D[0][1], camera.D[0][2], camera.D[0][3], camera.D[0][4]))
      file.write('R_01: {} {} {} {} {} {} {} {} {}\n'.format(T[0][0], T[0][1], T[0][2], T[1][0], T[1][1], T[1][2], T[2][0], T[2][1], T[2][2]))
      file.write('T_01: {} {} {}\n'.format(T[0][3], T[1][3], T[2][3]))
      file.write('S_rect_01: {} {}\n'.format(camera.width, camera.height))
      file.write('R_rect_01: {} {} {} {} {} {} {} {} {}\n'.format(T[0][0], T[0][1], T[0][2], T[1][0], T[1][1], T[1][2], T[2][0], T[2][1], T[2][2]))
      file.write('P_rect_01: {} {} {} {} {} {} {} {} {}\n'.format(camera.K[0][0], camera.K[0][1], camera.K[0][2], camera.K[1][0], camera.K[1][1], camera.K[1][2], camera.K[2][0], camera.K[2][1], camera.K[2][2]))
        
      ##### Event camera
      camera = int_ext_loader.sensor_collection[sensor_left_event_camera]
      T = int_ext_loader.tf_graph.get_relative_transform(camera.frame_id, base_frame_id)
      file.write('S_02: {} {}\n'.format(camera.width, camera.height))
      file.write('K_02: {} {} {} {} {} {} {} {} {}\n'.format(camera.K[0][0], camera.K[0][1], camera.K[0][2], camera.K[1][0], camera.K[1][1], camera.K[1][2], camera.K[2][0], camera.K[2][1], camera.K[2][2]))
      file.write('D_02: {} {} {} {} {}\n'.format(camera.D[0][0], camera.D[0][1], camera.D[0][2], camera.D[0][3], camera.D[0][4]))
      file.write('R_02: {} {} {} {} {} {} {} {} {}\n'.format(T[0][0], T[0][1], T[0][2], T[1][0], T[1][1], T[1][2], T[2][0], T[2][1], T[2][2]))
      file.write('T_02: {} {} {}\n'.format(T[0][3], T[1][3], T[2][3]))
      file.write('S_rect_02: {} {}\n'.format(camera.width, camera.height))
      file.write('R_rect_02: {} {} {} {} {} {} {} {} {}\n'.format(T[0][0], T[0][1], T[0][2], T[1][0], T[1][1], T[1][2], T[2][0], T[2][1], T[2][2]))
      file.write('P_rect_02: {} {} {} {} {} {} {} {} {}\n'.format(camera.K[0][0], camera.K[0][1], camera.K[0][2], camera.K[1][0], camera.K[1][1], camera.K[1][2], camera.K[2][0], camera.K[2][1], camera.K[2][2]))

      camera = int_ext_loader.sensor_collection[sensor_right_event_camera]
      T = int_ext_loader.tf_graph.get_relative_transform(camera.frame_id, base_frame_id)
      file.write('S_03: {} {}\n'.format(camera.width, camera.height))
      file.write('K_03: {} {} {} {} {} {} {} {} {}\n'.format(camera.K[0][0], camera.K[0][1], camera.K[0][2], camera.K[1][0], camera.K[1][1], camera.K[1][2], camera.K[2][0], camera.K[2][1], camera.K[2][2]))
      file.write('D_03: {} {} {} {} {}\n'.format(camera.D[0][0], camera.D[0][1], camera.D[0][2], camera.D[0][3], camera.D[0][4]))
      file.write('R_03: {} {} {} {} {} {} {} {} {}\n'.format(T[0][0], T[0][1], T[0][2], T[1][0], T[1][1], T[1][2], T[2][0], T[2][1], T[2][2]))
      file.write('T_03: {} {} {}\n'.format(T[0][3], T[1][3], T[2][3]))
      file.write('S_rect_03: {} {}\n'.format(camera.width, camera.height))
      file.write('R_rect_03: {} {} {} {} {} {} {} {} {}\n'.format(T[0][0], T[0][1], T[0][2], T[1][0], T[1][1], T[1][2], T[2][0], T[2][1], T[2][2]))
      file.write('P_rect_03: {} {} {} {} {} {} {} {} {}\n'.format(camera.K[0][0], camera.K[0][1], camera.K[0][2], camera.K[1][0], camera.K[1][1], camera.K[1][2], camera.K[2][0], camera.K[2][1], camera.K[2][2]))

if __name__ == '__main__':
  file_writer = FileWriter()
  file_writer.write_timestamp([335456451.123156465487878, 121212121211.45454554556666], file_path='/Rocket_ssd/dataset/tmp/timestamps.txt')
