Setting Up Catkin Workspace (ROS)
=================================

Let's create and build a catkin workspace for our custom project files/packages:

.. code-block:: console

    $ mkdir -p ~/catkin_ws/src
    $ cd ~/catkin_ws/
    $ catkin_make

The *catkin_make* command is a convenience tool for working with *catkin* workspaces.
Running it the first time in your workspace, it will create a ``CMakeLists.txt`` link in your ``'src'`` folder.

.. note::

    **Python3** users in ROS Melodic and earlier\: note, if you are building ROS from *source* to achieve *Python3* compatibility, and have setup your system appropriately (i.e. you have the *Python3* versions of all the required ROS Python packages installed, such as **catkin**) the first **catkin_make** command in a clean catkin workspace must be:

    .. code-block:: console

        $ catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3

    This will configure **catkin_make** with Python3.
    You may then proceed to use just **catkin_make** for subsequent builds.

Additionally, if you look in your current directory you should now have a ``'build'`` and ``'devel'`` folder. Inside the ``'devel'`` folder you can see that there are now several ``setup.*sh`` files. Sourcing any of these files will overlay this workspace on top of your environment.
To understand more about this see the general catkin documentation: `catkin <http://wiki.ros.org/catkin>`_.

Before continuing source your new ``setup.*sh`` file:

.. code-block:: console

    $ source devel/setup.bash

To make sure your workspace is properly overlayed by the ``setup`` script, make sure ``ROS_PACKAGE_PATH`` environment variable includes the directory you're in.

.. code-block:: console

    $ echo $ROS_PACKAGE_PATH
    /home/youruser/catkin_ws/src:/opt/ros/kinetic/share
