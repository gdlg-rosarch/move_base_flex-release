# Script generated with Bloom
pkgdesc="ROS - The mbf_abstract_nav package contains the abstract navigation server implementation of Move Base Flex (MBF). The abstract navigation server is not bound to any map representation. It provides the actions for planning, controlling and recovering. MBF loads all defined plugins at the program start. Therefor, it loads all plugins which are defined in the lists *planners*, *controllers* and *recovery_behaviors*. Each list holds a pair of a *name* and a *type*. The *type* defines which kind of plugin to load. The *name* defines under which name the plugin should be callable by the actions."
url='http://wiki.ros.org/move_base_flex'

pkgname='ros-lunar-mbf-abstract-nav'
pkgver='0.1.0_1'
pkgrel=1
arch=('any')
license=('3-Clause BSD'
)

makedepends=('ros-lunar-actionlib'
'ros-lunar-actionlib-msgs'
'ros-lunar-catkin'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-mbf-abstract-core'
'ros-lunar-mbf-msgs'
'ros-lunar-mbf-utility'
'ros-lunar-nav-msgs'
'ros-lunar-roscpp'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf'
'ros-lunar-xmlrpcpp'
)

depends=('ros-lunar-actionlib'
'ros-lunar-actionlib-msgs'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-mbf-abstract-core'
'ros-lunar-mbf-msgs'
'ros-lunar-mbf-utility'
'ros-lunar-nav-msgs'
'ros-lunar-roscpp'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf'
'ros-lunar-xmlrpcpp'
)

conflicts=()
replaces=()

_dir=mbf_abstract_nav
source=()
md5sums=()

prepare() {
    cp -R $startdir/mbf_abstract_nav $srcdir/mbf_abstract_nav
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

