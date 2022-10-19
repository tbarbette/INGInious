# pylint: disable=redefined-outer-name
# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.

import pytest

from inginious.common.additional_field import AdditionalField


@pytest.fixture()
def init():
    af = AdditionalField("test", "a description", "STRING")
    yield af


class TestAdditionalField(object):
    """Test for additional field class"""

    def test_additional_field_init(self, init):
        af = init
        assert af is not None
        af = AdditionalField(0, "a description", "STRING")
        try:
            af = AdditionalField("fail", "a description", "NOTCORRECT")
        except Exception:
            assert True

    def test_additional_field_get_id(self, init):
        af = init
        assert af.get_id() == "test"

    def test_additional_field_get_description(self, init):
        af = init
        assert af.get_description() == "a description"

    def test_additional_field_get_type(self, init):
        af = init
        assert af.get_type() == "STRING"
