#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author       : BobAnkh
# @Github       : https://github.com/BobAnkh
# @Date         : 2020-08-05 23:12:39
# @LastEditTime : ,: 2020-10-21 14:39:00
# @Description  : Tests for main.py
# @Copyright 2020 BobAnkh

import os
import sys

import pytest

sys.path.append('.')
import main


def test_get_tags():
    result = os.popen('git tag').read()
    result = result.split('\n')
    result[-1] = 'HEAD'
    assert result == main.get_tags()


@pytest.mark.parametrize("previous_version, later_version, flag, result", [(
    "v0.0.1", "v0.0.2", 1,
    [[
        '21ff26b0075845f116dfdd9c87d5a3c89fda8660',
        'chore(pytest): change name'
    ],
     [
         'f9ed121906994757e380851ef77415b48b865d13',
         'feat(changelog): add newline after list item'
     ],
     [
         'ec67d8bef6350d79fed18423eb85364c7a5ff1ec',
         'chore(template): update template style'
     ],
     [
         'b7c83f5bfd704f4dc6a46535bd68a54705586b20',
         'ci(mdl): update ignore files'
     ],
     [
         '5e7596e4d5f12c596b4ec9613dd434b4989c7a9d',
         'Merge pull request #3 from BobAnkh/feature/codecov'
     ],
     [
         '1a3e15a4bdf7850688f925dd0b1d8ace52e75fc3',
         'feat(codecov): add coverage report'
     ],
     [
         '82d2f10cf6035218e2f0898be3e09fdb41b2d144',
         'chore(gitmagic): update rules'
     ],
     [
         'dd857636e1362f78aa436f8fb75886ce2f5ba54b',
         'chore(pytest): change to self-written one'
     ],
     [
         '4cf8e46a803f8f6180691b0fd7ccf68343e7e161',
         'chore(pytest): install requirements'
     ],
     [
         '97aec2b5464db1b442b85e050f94b29f0261e7fe',
         'chore(pytest): add pytest to python convention'
     ],
     [
         '60894669e73d634d84aab1aee79476406ec60d45',
         'fix(dockerfile): use chmod to deal with   execution permission issue'
     ],
     [
         '7be84a0e5fe23f11d0caa43066f80dcfeaf90904',
         'test(main): add tests of main.py'
     ],
     [
         '94e29d3fd772cc3787143196ed0f7b62490846b3',
         'chore(gitigore): ignore python-related files'
     ],
     [
         '50cfdf32ec07b81d3140b9a06fd5275fc69f8f7b',
         'fix(main): deal with DeprecationWarning'
     ],
     [
         'f707414e48a723d78f0ee7c55eb8bc09d53328d9',
         'Merge pull request #2 from BobAnkh/dependabot/pip/pygithub-1.52'
     ],
     [
         '33e6b99411852635a61175950d6a6d59545c9f3c',
         'chore(deps): bump pygithub from 1.51 to 1.52'
     ],
     [
         '997b3c8d4f5e5253bba0d0eecbab4b6fb6e92768',
         'chore(mergify): fix a typo'
     ],
     [
         'e19c0ffcdfb553b8bb0286f8a9ee5969661638a1',
         'chore(mdl): ignore md024 and code_of_conduct'
     ],
     ['e217912f5738c8a9e7c0a7fbd2c37e546d07a4ce', 'chore(*): fix some typos'],
     [
         '0591844384a8a62f13eac0cec35d34df66dd07b9',
         'perf(main): improve regex match'
     ],
     [
         '8f73cf667125b071847588eae7aebd7c77205e6e',
         'style(action): add description of scripts'
     ],
     [
         '3294e4fb0306dd585c9264619443eaa03fc0d258',
         'style(entrypoint): add fileheader'
     ],
     [
         'de4c46091900679835c0a005435aa447b6aea1db',
         'docs(CONTRIBUTING): refactor to have styleguide'
     ],
     [
         '3d91d352f5fb9eb3bcc604c21d5729f4e06b6c50',
         'style(main): add fileheader'
     ],
     [
         '74e884d18af0cab2ddbe61554d962ef55d105d6c',
         'docs(README): change `parameters` to `inputs`'
     ],
     [
         'dd778cbc48b3e8c306e06773f499e06e46f18269',
         'perf(changelog): simplify progress of updating'
     ],
     [
         '6721474cb8d4b5d862389690981de72ad09b62cb',
         'docs(CONTRIBUTING.md): fix typo and change a word'
     ],
     [
         '6d7a16812e45d3356549e48cd916ea8433ecad59',
         'docs(CHANGELOG): update release notes'
     ]])])
def test_get_commit_log_between_versions(previous_version, later_version,
                                         flag, result):
    assert result == main.get_commit_log_between_versions(previous_version, later_version, flag)


@pytest.mark.parametrize("commits, regex, output, set", [
    ([[1, 'docs(changelog): fix a typo'], [2, 'feat(README): add it']
      ], r'^feat[(](.+?)[)]', [[2, 'feat(README): add it', 'README', 'add it']
                               ], {'README'}),
    ([[1, 'docs(*): add contributing guideline'],
      [2, 'feat(changelog): change function']], r'^docs[(](.+?)[)]', [[
          1, 'docs(*): add contributing guideline', '*',
          'add contributing guideline'
      ]], {'*'}),
    ([[1, 'docs(*): add contributing guideline'],
      [2, 'docs(changelog): fix a typo']], r'^docs[(](.+?)[)]', [[
          1, 'docs(*): add contributing guideline', '*',
          'add contributing guideline'
      ]], {'*'}),
    ([[1, 'feat(*): add contributing guideline'],
      [2, 'feat(changelog): change function']], r'^feat[(](.+?)[)]', [[
          1, 'feat(*): add contributing guideline', '*',
          'add contributing guideline'
      ], [
          2, 'feat(changelog): change function', 'changelog', 'change function'
      ]], {'changelog', '*'}),
])
def test_strip_commits(commits, regex, output, set):
    assert output, set == main.strip_commits(commits, regex)
