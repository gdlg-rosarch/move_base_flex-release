# Script generated with Bloom
pkgdesc="ROS - Move Base Flex (MBF) is a backwards-compatible replacement for move_base. MBF can use existing plugins for move_base, and provides an enhanced version of the planner, controller and recovery plugin ROS interfaces. It exposes action servers for planning, controlling and recovering, providing detailed information of the current state and the plugin’s feedback. An external executive logic can use MBF and its actions to perform smart and flexible navigation strategies. Furthermore, MBF enables the use of other map representations, e.g. meshes or grid_map This package is a meta package and refers to the Move Base Flex stack packages.The abstract core of MBF – without any binding to a map representation – is represented by the <a href="wiki.ros.org/mbf_abstract_nav">mbf_abstract_nav</a> and the <a href="wiki.ros.org/mbf_abstract_core">mbf_abstract_core</a>. For navigation on costmaps see <a href="wiki.ros.org/mbf_costmap_nav">mbf_costmap_nav</a> and <a href="wiki.ros.org/mbf_costmap_core">mbf_costmap_core</a>."
url='http://wiki.ros.org/move_base_flex'

pkgname='ros-lunar-move-base-flex'
pkgver='0.1.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-mbf-abstract-core'
'ros-lunar-mbf-abstract-nav'
'ros-lunar-mbf-costmap-core'
'ros-lunar-mbf-costmap-nav'
'ros-lunar-mbf-msgs'
'ros-lunar-mbf-simple-nav'
)

depends=('ros-lunar-mbf-abstract-core'
'ros-lunar-mbf-abstract-nav'
'ros-lunar-mbf-costmap-core'
'ros-lunar-mbf-costmap-nav'
'ros-lunar-mbf-msgs'
'ros-lunar-mbf-simple-nav'
)

conflicts=()
replaces=()

_dir=move_base_flex
source=()
md5sums=()

prepare() {
    cp -R $startdir/move_base_flex $srcdir/move_base_flex
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

