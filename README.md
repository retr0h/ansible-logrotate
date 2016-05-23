logrotate
=========

A library which manages log rotate configurations.

Library ready status
--------------------

[![Galaxy](http://img.shields.io/badge/galaxy-ansible--logrotate-blue.svg?style=flat-square)](https://galaxy.ansible.com/list#/roles/1131)

Requirements
------------

None

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
