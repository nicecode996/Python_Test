#! usr/bin/env python3
# coding=utf-8

import pytest
import yaml


class TestDate:
    # @pytest.mark.parametrize("a,b", [(10, 20), (10, 50), (1, 5)])
    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("data.yaml")))
    def test_data(self, a, b):
        print(a + b)
