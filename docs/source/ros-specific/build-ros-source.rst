Building ROS Melodic from Source on Ubuntu 20.04 LTS
======================================================

Install from source requires that you download and compile the source code on your own.
ROS Melodic supports **Ubuntu Artful** and **Bionic** as well as **Debian Stretch**. Other platforms are possible to use but are not expected to work out of the box.

To Make ROS Melodic run on an unsupported Distribution of Linux, follow the steps listed below:

Prerequisites
-------------
.. note::
    Make sure `buildtools` or tools required to build packages as per your distribution is installed properly in your system, along with python3 and pip.

    For Ubuntu or Debian-based Distributions, the package **build-essential** should suffice, along with `python-is-python3`

Install build dependencies:

**Generic (pip)**:

.. code-block:: console

    $ sudo pip install -U rosdep rosinstall_generator vcstool rosinstall

Setup ROS Specific Repositories for Ubuntu
------------------------------------------

Add ROS Specific Repostiories for Ubuntu Distribution, otherwise you would have to manually search and install missing dependencies (Ref: `Installation Guide ROS Melodic <http://wiki.ros.org/melodic/Installation/Ubuntu#Installation>`_)

.. code-block:: console

    $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

    $ sudo apt install curl # if you haven't already installed curl
    $ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

    $ sudo apt update

Initializing `rosdep`
---------------------

`rosdep` must be initialized first

.. code-block:: console

    $ sudo rosdep init
    $ rosdep update

Create a `catkin` Workspace
----------------------------

In order to build the ``core packages``, you will need a catkin workspace. Create one now:

.. code-block:: console

    $ mkdir ~/ros_catkin_ws
    $ cd ~/ros_catkin_ws
    $ mkdir ~/ros_catkin_ws/src


Next we will want to fetch the ``core packages`` so we can build them.
We will use ``vcstool``` for this.

Start by building the ``core`` ROS packages and add additional packages after the build completion for essential core packages.

**ROS-Comm (Bare Bones):** ROS package, build, and communication libraries. **NO GUI** tools.

.. code-block:: console

    $ export ROS_PYTHON_VERSION=3
    $ rosinstall_generator ros_comm --rosdistro melodic --deps --tar > melodic-ros_comm.rosinstall
    $ vcs import src < melodic-ros_comm.rosinstall

This will add all of the ``catkin packages`` in the given *variant* and then fetch the sources into the ``~/ros_catkin_ws/src`` directory. The command will take a few minutes to download all of the core ROS packages into the ``src`` folder.

Resolving Dependencies
-----------------------

Before you can build your ``catkin workspace`` you need to make sure that you have all the required dependencies. We use the rosdep tool for this:

.. code-block:: console

    $ rosdep install --from-paths src --ignore-src --rosdistro melodic -y

This will look at all of the packages in the ``src`` directory and find all of the dependencies they have. Then it will recursively install the dependencies.

Building the `catkin` Workspace
--------------------------------

Once it has completed downloading the packages and resolving the dependencies you are ready to build the *catkin* packages.
We will use the **catkin_make_isolated** command because there are both *catkin* and *plain cmake* packages in the base install, when developing on your *catkin* only workspaces you may choose to use ``catkin/commands/catkin_make`` which only works with *catkin* packages.

Invoke catkin_make_isolated:

.. code-block:: console

    $ ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release

Now the packages should have been installed to ``~/ros_catkin_ws/install_isolated`` (or to wherever you specified with the ``--install-space`` argument). If you look in that directory you will see that a setup.bash file have been generated.

To utilize the packages which have been built currently by the above command, simply **source** the ``setup.bash`` file to make them available:

.. code-block:: console

    $ source ~/ros_catkin_ws/install_isolated/setup.bash

To make these packages available without sourcing everytime:

.. code-block:: console

    $ echo 'source ~/ros_catkin_ws/install_isolated/setup.bash' >> ~/.bashrc # Or ~/.zshrc Or Your shell-rc file.