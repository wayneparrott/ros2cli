# Copyright 2020 Open Source Robotics Foundation, Inc.
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

from argparse import Namespace
from ros2doctor.verb.call import CallVerb
from ros2doctor.verb.call import spawn_summary_table


def test_empty_call():
    args = Namespace(once=True)
    call_verb = CallVerb()
    output_table = call_verb.main(args=args)
    assert output_table['pub'] == 20
    assert output_table['sub'] == 0
    assert output_table['send'] == 20
    assert output_table['receive'] == 0
