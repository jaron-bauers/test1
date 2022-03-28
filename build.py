from pybuilder.core import use_plugin
from pybuilder.core import init
from pybuilder.core import Author

use_plugin('python.core')
use_plugin('python.unittest')
use_plugin('python.flake8')
use_plugin('python.coverage')
use_plugin('python.distutils')
use_plugin('pypi:pybuilder_radon')
use_plugin('pypi:pybuilder_bandit')
use_plugin('pypi:pybuilder_anybadge')

name = 'tgsver'
authors = [Author('Jaron Bauers', 'jaron.bauers@intel.com')]
summary = 'A Python script to automate the functional testing of the git-semver capability'
url = 'https://github.com/jaron-bauers/test-git-semver'
version = '0.1.0'
default_task = [
    'clean',
    'analyze',
    'publish',
    'radon',
    'bandit',
    'anybadge']
license = 'Apache License, Version 2.0'
description = summary


@init
def set_properties(project):
    project.set_property('unittest_module_glob', 'test_*.py')
    project.set_property('coverage_break_build', True)
    project.set_property('flake8_max_line_length', 120)
    project.set_property('flake8_verbose_output', True)
    project.set_property('flake8_break_build', True)
    project.set_property('flake8_ignore', 'E501, W503, F401, F841')
    project.depends_on_requirements('requirements.txt')
    project.set_property('distutils_readme_description', True)
    project.set_property('distutils_description_overwrite', True)
    project.set_property('distutils_upload_skip_existing', True)
    project.set_property('distutils_console_scripts', ['test-git-semver = tgsver.cli:main'])
    project.set_property('distutils_classifiers', [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration'])
    project.set_property('radon_break_build_average_complexity_threshold', 3.6)
    project.set_property('radon_break_build_complexity_threshold', 14)
    project.set_property('bandit_break_build', True)
    project.set_property('bandit_skip_ids', 'B404,B603')
    project.set_property('anybadge_use_shields', True)
