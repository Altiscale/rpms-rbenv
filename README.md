# rpms-rbenv

RPM for rbenv and standard Altiscale rubies.

* Uses mock to install rbenv and to build rubies into rbenv with the required absolute paths.  
* Uses fpm to package the build artifacts.

The result is a package that installs rbenv with the rubies into /opt/altiscale/rbenv
and provides usage instructions in the RPM description.
