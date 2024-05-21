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
 
From the image, the right side of the equation represents the Jacobian matrix depicted as J multiplied by the joint variable velocities. On the other side of the equation, we have the end effector velocities we are solving for. The Jacobian matrix size is dependent on the number of joints that the manipulator has. The values inside the Jacobian Matrix are as follows:

 
The image above shows us how many elements are inside the Jacobian Matrix. Although what we see is a 6x3 matrix, this can go up in more columns since the columns depend on the number of joints that the manipulator has. The values inside the Jacobian matrix depend on the given or desired joint variables and changes constantly in reference to those joint variables, The values in these empty boxes are as such:
 

The first three rows in the Jacobian matrix represent the Linear velocities of the Manipulator while the bottom three rows are the Rotational Velocities. We follow this table to correctly and accurately input the values needed so that when it comes to the solution, it will end up being correct and functioning as intended. Once the Jacobian Matrix is solved, we can start multiplying it by the joint velocities so that we can end up with differential equations but that will be discussed later on.

For a better understanding of how the Jacobian matrix is solved, an example will be provided below: 
