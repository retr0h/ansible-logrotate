logrotate
=========

A library which manages log rotate configurations.

Library ready status
--------------------

[![Build Status](http://img.shields.io/travis/retr0h/ansible-logrotate.svg?style=flat-square)](https://travis-ci.org/retr0h/ansible-logrotate)
[![Galaxy](http://img.shields.io/badge/galaxy-ansible--logrotate-blue.svg?style=flat-square)](https://galaxy.ansible.com/list#/roles/1131)

Requirements
------------

* Ansible 2.1

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

        - name: rotate /var/log/wibble.log
          logrotate:
            name: wibble-log
            path: '/var/log/wibble*.log'
            options:
              - daily
              - size +1M
              - rotate 7
              - missingok
              - copytruncate
              - compress


Testing
-------

Tests are performed by [Molecule](http://molecule.readthedocs.org/en/latest/).

    $ tox

License
-------

MIT
