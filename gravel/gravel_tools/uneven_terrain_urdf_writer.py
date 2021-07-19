
print("Enter dims: \n")
dims = int(input())

# print("Enter distance between tiles: \n")
dist = 0.92

# 0.92 for 0.001

before_stuff = """<?xml version="1.0"?>
<robot xmlns:xacro="http://ros.org/wiki/xacro" name="my_terrain">

  <material name="blue">
    <color rgba="0 0 0.8 1"/>
  </material>

  <link name="base_link"/>"""

link_string_pt_1 = """
  <link name="my_terrain"""

link_string_pt_2 = """">
    <visual>
      <geometry>
        <mesh filename="package://earl_gazebo/stl/gravel_l.dae" scale="0.001 0.001 0.001"/>
      </geometry>
      <origin rpy="0 0 0" xyz="0 0 0"/>
    </visual>
    <collision>
      <geometry>
        <mesh filename="package://earl_gazebo/stl/gravel_l.dae" scale="0.001 0.001 0.001"/>
      </geometry>
      <origin rpy="0 0 0" xyz="0 0 0"/>
    </collision>
    <inertial>
      <mass value="0.01" />
      <inertia ixx="0.01" ixy="0.01" iyy="0.01" iyz="0.01" izz="0.01" ixz="0.01"/>
    </inertial>
  </link>"""

joint_str_pt_1 = """  <joint name="base2terr"""
joint_str_pt_2 = """" type="fixed">
    <parent link="base_link"/>
    <child link="my_terrain"""

joint_str_pt_3 = """"/>
    <origin xyz=" """""
joint_str_pt_4 = """0" rpy="1.5708 0 0"/>
  </joint>"""

final_urdf = before_stuff + "\n\n"


for i in range(dims):
    for j in range(dims):
        x = (i * dist) - (dist * (dims / 2))
        y = (j * dist) - (dist * (dims / 2))
        link = link_string_pt_1 + "i" + str(i) + "j" + str(j) + link_string_pt_2 + "\n\n"
        joint = joint_str_pt_1 + "i" + str(i) + "j" + str(j) + joint_str_pt_2 + "i" + str(i) + "j" + str(j) + joint_str_pt_3 + str(x) + " " + str(y) + " "  + joint_str_pt_4 + "\n\n"
        final_urdf = final_urdf + link + joint

# print(final_urdf)
final_urdf = final_urdf + "\n\n</robot>"
text_file = open("whole_urdf.txt", "w")
n = text_file.write(final_urdf)
text_file.close()
