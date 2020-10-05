#  Copyright 2020 Ocean Data Foundation AS
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import unittest

from typing import Any, Tuple, Union, Callable, Type


class TestOdpSdkImports(unittest.TestCase):

    def setUp(self) -> None:
        try:
            from cartopy import __version__
            self.deps_installed = True
        except ImportError:
            self.deps_installed = False

    def assertNotRaises(
            self,
            expected_exception: Union[Type[BaseException], Tuple[Type[BaseException], ...]],
            callable: Callable[..., Any],
            *args: Any, **kwargs: Any
    ) -> None:

        try:
            callable(*args, **kwargs)
        except expected_exception:
            self.fail(f"{str(expected_exception)} raised by {str(callable)}")

    def test_numeric_import(self):

        def cb():
            import odp_sdk.utils.numeric

        if self.deps_installed:
            assertion = self.assertNotRaises
        else:
            assertion = self.assertRaises

        assertion(ImportError, cb)

    def test_visual_import(self):

        def cb():
            import odp_sdk.utils.visual

        if self.deps_installed:
            assertion = self.assertNotRaises
        else:
            assertion = self.assertRaises

        assertion(ImportError, cb)
