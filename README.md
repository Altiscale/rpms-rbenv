# rpms-rbenv

RPM for rbenv and standard Altiscale rubies.

* Uses mock to install rbenv and to build rubies into rbenv with the required absolute paths.
* Uses alti_mock as a wrapper around mock to inherit curated mock configurations from the alti_build_tools gem.
* Uses fpm to package the build artifacts.

The result is a package that installs rbenv with the rubies into /opt/altiscale/rbenv
and provides usage instructions in the RPM description.
