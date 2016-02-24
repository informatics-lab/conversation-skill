#!/usr/bin/env python

from distutils.core import setup

setup(name='conversation',
      version='0.1',
      install_requires=[
          "dotmap"
      ],
      description='Conversation Skill',
      long_description='''
Coversation Skill
''',
      author='Rachel Prudden',
      author_email='rachel.prudden@informaticslab.co.uk',
      maintainer='Rachel Prudden',
      maintainer_email='rachel.prudden@informaticslab.co.uk',
      url='https://github.com/met-office-lab/conversation-skill',
      license='TBC',
      packages=['.'],
      classifiers=[
          'Programming Language :: Python :: 2.7',
      ]
     )