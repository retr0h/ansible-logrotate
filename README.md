logrotate
=========

A role which manages the logrotate package, and provides a means to manage specific log rotate configurations.

Role ready status
-----------------

[![Build Status](http://img.shields.io/travis/retr0h/ansible-logrotate.svg?style=flat-square)](https://travis-ci.org/retr0h/ansible-etcd)
[![Galaxy](http://img.shields.io/badge/galaxy-ansible--logrotate-blue.svg?style=flat-square)](https://galaxy.ansible.com/list#/roles/1131)

Requirements
------------

None

Role Variables
--------------

* `logrotate_config_dir` - Directory containing config files.
                           (default: /etc/logrotate.d)
* `logrotate_frequency` - Set the frequency for rotation. (default: daily)
* `logrotate_rotate` - Number of logs to retain. (default: 8)
* `logrotate_create` - Set creation parameters. (default: undefined)
* `logrotate_postrotate` - Set postrotate command to run. (default: undefined)

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      tasks:
        - name: Rotate /var/log/tomcat/myapp.log
          logrotate: name=myapp
                     path=/var/log/tomcat/myapp.log
          args:
            options:
              - daily
              - rotate 8
              - postrotate
              - exec script
              - endscript

Testing
-------

Tests are performed by [Molecule](http://molecule.readthedocs.org/en/latest/).

    $ make
    $ source venv/bin/activate
    $ molecule test

License
-------

MIT
