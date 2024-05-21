# Robotics2_JacobianandPT_Group1_Spherical_2024
# Forward and Inverse Kinematics of a Spherical Manipulator
### Members:
- PL : Perilla, Aira A.
- PE : Capuno, Raphael Juno L.
- PS : Arnante, Juan Bienvinido P.
- PQ : Almonte, Ray Ivan C.
- PR : Tolentino, Gian Carl C.

##  Abstract of the Project

In the previous project, the main topics discussed were the Forward and Inverse kinematics of the Spherical Manipulator. Other topics included the computations, the essential methods for the solutions, and the development of a graphical user interface with methods that click on either a function for the inverse or the forward kinematics. In this project sequel, the focus will be on the Jacobian Matrix, the Singularities of a manipulator, the Velocity of the manipulator, and the Path and Trajectory needed for the replication of welding and pick and place movement. The goal of the project is to create a complete Calculator with elements such as the velocities and a newer and moving model and to do so, the aforementioned, as well as the previous elements from the previous project, were essential.

## Introduction
In the previous midterm project, the goal was to discuss the assigned manipulator from its degrees of freedom to its inverse kinematics solution. Ultimately, the project concluded with a **GUI Calculator** for the forward and inverse kinematics together with a model that shows how the manipulator would look and position with given position vectors or joint variables. In this sequel, which is the ***Final Project***, the focus will now shift to advanced topics. The main focus of the Final Project will be the Velocities of the manipulator. Imagine you have a manipulator of any kind and it moves as intended based on the code or desire of the creator; however, even though it moves as intended, you would notice the speed at which the manipulator moves. Sometimes, the manipulator might just be light enough that it can move swiftly but that would be expected as a small manipulator and not one that is large enough for production causes which mainly is what most manipulators are for. A better solution to manipulate the speed of the manipulator would be to incorporate it into a program that can do so wherein one of which is with the use of the ***Jacobian Matrix***.


## The Jacobain Matrix

Jacobian matrix represents the partial derivatives of a function with respect to its variables. These partial derivatives are from the forward kinematics and this matrix relates the end effector velocities to the joint velocities. This enables the calculation of each of the joint’s velocities with the use of this equation:



 ![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/2b653dbc-9bc8-4010-9827-f9fe01b89e33)

From the image, the right side of the equation represents the Jacobian matrix depicted as J multiplied by the joint variable velocities. On the other side of the equation, we have the end effector velocities we are solving for. The Jacobian matrix size is dependent on the number of joints that the manipulator has. The values inside the Jacobian Matrix are as follows:


![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/b0c52c9f-a756-4586-8c8a-32bc88c44495)

 
The image above shows us how many elements are inside the Jacobian Matrix. Although what we see is a 6x3 matrix, this can go up in more columns since the columns depend on the number of joints that the manipulator has. The values inside the Jacobian matrix depend on the given or desired joint variables and changes constantly in reference to those joint variables, The values in these empty boxes are as such:
 
![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/7f1da48e-3ea9-45a4-bbae-39b65be2a903)

The first three rows in the Jacobian matrix represent the Linear velocities of the Manipulator while the bottom three rows are the Rotational Velocities. We follow this table to correctly and accurately input the values needed so that when it comes to the solution, it will end up being correct and functioning as intended. Once the Jacobian Matrix is solved, we can start multiplying it by the joint velocities so that we can end up with differential equations but that will be discussed later on.

For a better understanding of how the Jacobian matrix is solved, an example will be provided below: 

These will be the values used for this example so as to not make the equation too lenghty:
![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/297de93f-bf09-49fe-8f6d-7dd3f33a40c7)

Now we substitute the appropriate values for the content inside the Jacobian Matrix:

![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/8d1778b5-aec4-4437-b31f-ace034203149)

Now we solve for the rotation matrix and position vector equations:


Column 1, Row 1 to 3:
![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/39ed2e4e-97f4-4134-8ea0-d41d11d16c9d)

Column 2, Row 1 to 3:

![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/7d84b842-7512-4057-84e0-fef8f19c3de9)

Column 3, Row 1 to 3:

![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/2c94c130-9f1b-4303-b654-99574223b42f)

This completes the Linear End Effector Velocities, now we head on the the equations for the Rotational End Effector Velocities:

Column 1, Row 4 to 6:

![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/00f9251f-942e-48eb-9f93-0de4fec49eb4)

Column 2, Row 4 to 6:

![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/e61caca3-7c0b-4d72-8271-aeb5daadfcc6)

Column 3, Row 4 to 6:

![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/6ee5e5bf-c355-4c63-8bca-87758a009d4c)

Now that we also have our Rotational End Effector Velocities, Our Jacobian Matrix is now complete and is shown below:

![image](https://github.com/Bien21-00590/Robotics2_JacobianandPT_Group1_Spherical_2024/assets/157681561/8013d6b8-2ab7-494b-99bf-41afda0cf158)





