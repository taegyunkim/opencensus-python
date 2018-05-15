# Copyright 2018, OpenCensus Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import mock
from opencensus.stats import view_manager as view_manager_module


class TestViewManager(unittest.TestCase):
    def test_constructor(self):
        view_manager = view_manager_module.ViewManager()

        self.assertIsNotNone(view_manager.time)
        self.assertIsNotNone(view_manager.measure_to_view_map)

    def test_register_view(self):
        view = mock.Mock()
        view_manager = view_manager_module.ViewManager()
        view_manager.register_view(view=view)

        view_manager_mock = mock.Mock()
        view_manager = view_manager_mock

        view_manager.register_view(view=mock.Mock())
        self.assertTrue(view_manager_mock.register_view.called)

    def test_get_view(self):
        view_name = mock.Mock()
        view_manager = view_manager_module.ViewManager()
        view_manager.get_view(view_name=view_name)

        view_manager_mock = mock.Mock()
        view_manager = view_manager_mock

        view_manager.get_view(view_name=mock.Mock())
        self.assertTrue(view_manager_mock.get_view.called)

    def test_get_all_exported_views(self):
        view_manager = view_manager_module.ViewManager()
        exported_views = view_manager.get_all_exported_views()
        self.assertIsNotNone(exported_views)

        view_manager_mock = mock.Mock()
        view_manager = view_manager_mock

        view_manager.get_all_exported_views()
        self.assertTrue(view_manager_mock.get_all_exported_views.called)
