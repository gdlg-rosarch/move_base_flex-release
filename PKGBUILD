# Script generated with Bloom
pkgdesc="ROS - This package provides common interfaces for navigation specific robot actions. It contains the CostmapPlanner, CostmapController and CostmapRecovery interfaces. The interfaces have to be implemented by the plugins to make them available for Move Base Flex using the mbf_costmap_nav navigation implementation. That implementation inherits the mbf_abstract_nav implementation and binds the system to a local and a global costmap."
url='http://wiki.ros.org/move_base_flex/mbf_costmap_core'

pkgname='ros-lunar-mbf-costmap-core'
pkgver='0.1.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-costmap-2d'
'ros-lunar-geometry-msgs'
'ros-lunar-mbf-abstract-core'
'ros-lunar-nav-core'
'ros-lunar-std-msgs'
'ros-lunar-tf'
)

depends=('ros-lunar-costmap-2d'
'ros-lunar-geometry-msgs'
'ros-lunar-mbf-abstract-core'
'ros-lunar-nav-core'
'ros-lunar-std-msgs'
'ros-lunar-tf'
)

conflicts=()
replaces=()

_dir=mbf_costmap_core
source=()
md5sums=()

prepare() {
    cp -R $startdir/mbf_costmap_core $srcdir/mbf_costmap_core
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

