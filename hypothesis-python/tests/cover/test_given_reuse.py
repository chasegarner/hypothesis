# coding=utf-8
#
# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis-python
#
# Most of this work is copyright (C) 2013-2018 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.
#
# END HEADER

from __future__ import division, print_function, absolute_import

import pytest

from hypothesis import given
from hypothesis import strategies as st

given_booleans = given(st.booleans())


@given_booleans
def test_has_an_arg_named_x(x):
    pass


@given_booleans
def test_has_an_arg_named_y(y):
    pass


given_named_booleans = given(z=st.text())


def test_fail_independently():
    @given_named_booleans
    def test_z1(z):
        assert False

    @given_named_booleans
    def test_z2(z):
        pass

    with pytest.raises(AssertionError):
        test_z1()

    test_z2()
