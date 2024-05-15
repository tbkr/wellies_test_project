Overview
========

This is a test project containing a preliminary version of a test suite using
pyflow-wellies. Currently it's configured as follows:

Everything is running on the fdbdev machine

The ECF_HOME folder is located in
`/perm/fdbdev/wellies_test/ecf-home`

The project itself is located under
`/home/fdbdev/git/wellies_test_project`

If you want to execute the creation of the suite, do as follows:
- Change directory to the git repository
- load the necessary modules (load python3/3.10.10-01)
- Run `make` 
- Follow the trackies prompt
- The new definitions are placed in the ECF_HOME folder
- Export the following environment variables
    - export ECF_HOST=ecflow-gen-fdbdev-001
    - export ECF_PORT=3141
- Run:
    - ecflow_client --load=/perm/fdbdev/suites/ecfs_flow_wellies/ecfs_flow_wellies.def
    Or in case the suite is already existing:
    - ecflow_client --replace=/ecfs_flow_wellies /perm/fdbdev/suites/ecfs_flow_wellies/ecfs_flow_wellies.def
