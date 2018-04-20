# Script generated with Bloom
pkgdesc="ROS - The mbf_costmap_nav package contains the costmap navigation server implementation of Move Base Flex (MBF). The costmap navigation server is bound to the <a href="wiki.ros.org/costmap_2d">costmap_2d</a> representation. It provides the Actions for planning, controlling and recovering. At the time of start MBF loads all defined plugins. Therefor, it loads all plugins which are defined in the lists *planners*, *controllers* and *recovery_behaviors*. Each list holds a pair of a *name* and a *type*. The *type* defines which kind of plugin to load. The *name* defines under which name the plugin should be callable by the actions. Additionally the mbf_costmap_nav package comes with a wrapper for the old navigation stack and the plugins which inherits from the <a href="wiki.ros.org/nav_core">nav_core</a> base classes. Preferably it tries to load plugins for the new API. However, plugins could even support both <a href="wiki.ros.org/move_base">move_base</a> and <a href="wiki.ros.org/move_base_flex">move_base_flex</a> by inheriting both base class interfaces located in the <a href="wiki.ros.org/nav_core">nav_core</a> package and in the <a href="mbf_costmap_core">mbf_costmap_core</a> package."
url='http://wiki.ros.org/move_base_flex'

pkgname='ros-lunar-mbf-costmap-nav'
pkgver='0.1.0_1'
pkgrel=1
arch=('any')
license=('3-Clause BSD'
)

makedepends=('ros-lunar-actionlib'
'ros-lunar-actionlib-msgs'
'ros-lunar-base-local-planner'
'ros-lunar-catkin'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-mbf-abstract-nav'
'ros-lunar-mbf-costmap-core'
'ros-lunar-mbf-msgs'
'ros-lunar-mbf-utility'
'ros-lunar-nav-core'
'ros-lunar-nav-msgs'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf'
)

depends=('ros-lunar-actionlib'
'ros-lunar-actionlib-msgs'
'ros-lunar-base-local-planner'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-mbf-abstract-nav'
'ros-lunar-mbf-costmap-core'
'ros-lunar-mbf-msgs'
'ros-lunar-mbf-utility'
'ros-lunar-move-base'
'ros-lunar-move-base-msgs'
'ros-lunar-nav-core'
'ros-lunar-nav-msgs'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf'
)

conflicts=()
replaces=()

_dir=mbf_costmap_nav
source=()
md5sums=()

prepare() {
    cp -R $startdir/mbf_costmap_nav $srcdir/mbf_costmap_nav
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

