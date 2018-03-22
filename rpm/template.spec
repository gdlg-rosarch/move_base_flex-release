Name:           ros-kinetic-mbf-msgs
Version:        0.1.0
Release:        1%{?dist}
Summary:        ROS mbf_msgs package

Group:          Development/Libraries
License:        3-Clause BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-genmsg
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-message-runtime
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-std-msgs

%description
The move_base_flex messages package providing the action definition files for
the action GetPath, ExePath, Recovery and MoveBase. The action servers providing
these action are implemented in mbf_abstract_nav.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Mar 22 2018 Jorge Santos <santos@magazino.eu> - 0.1.0-1
- Autogenerated by Bloom

* Wed Mar 21 2018 Jorge Santos <santos@magazino.eu> - 0.1.0-0
- Autogenerated by Bloom

