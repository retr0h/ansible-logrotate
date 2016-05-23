import re

import pytest


@pytest.mark.parametrize('filename', ['/etc/logrotate.d/test'])
def test_logrotate_config(File, filename):
    f = File(filename)

    assert f.exists
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644


@pytest.mark.parametrize('filename', ['/etc/logrotate.d/test'])
def test_logrotate_config_content(File, filename):
    f = File(filename)

    f.contains('/var/log/test.log')
    f.contains('daily')
    f.contains('rotate 8')

    assert re.search(r'postrotate.*exec script.*endscript', f.content,
                     re.DOTALL)


@pytest.mark.parametrize('filename', ['/etc/logrotate.d/test_multi'])
def test_logrotate_config_content_multi_file(File, filename):
    f = File(filename)

    assert re.search(r'/var/log/log1.log.*/var/log/log2.log', f.content,
                     re.DOTALL)


@pytest.mark.parametrize('filename', ['/etc/logrotate.d/missing'])
def test_logrotate_config_removed(File, filename):
    f = File(filename)

    assert not f.exists
