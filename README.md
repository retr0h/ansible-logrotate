logrotate
=========

A role which manages the logrotate package, and provides a means to manage specific log rotate configurations.

Role ready status
-----------------

[![Build Status](https://travis-ci.org/retr0h/ansible-logrotate.png?branch=master)](https://travis-ci.org/retr0h/ansible-logstash)

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
	  roles:
		- { role: logrotate,
			logrotate_name: apache2,
			logrotate_path: /var/log/apache2/*.log }
		- { role: logrotate,
			logrotate_name: myapp,
			logrotate_path: /var/log/tomcat/myapp.log }

License
-------

MIT
