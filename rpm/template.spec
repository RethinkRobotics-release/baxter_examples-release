Name:           ros-hydro-baxter-examples
Version:        1.1.0
Release:        0%{?dist}
Summary:        ROS baxter_examples package

Group:          Development/Libraries
License:        BSD
URL:            http://sdk.rethinkrobotics.com
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-baxter-core-msgs
Requires:       ros-hydro-baxter-interface
Requires:       ros-hydro-control-msgs
Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-rospy
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-trajectory-msgs
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-baxter-core-msgs
BuildRequires:  ros-hydro-baxter-interface
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-control-msgs
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-trajectory-msgs

%description
Example programs for Baxter SDK usage.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Feb 02 2015 Rethink Robotics Inc. <rsdk.support@rethinkrobotics.com> - 1.1.0-0
- Autogenerated by Bloom

