# Copy detector
# Copyright (C) <2020>  <Ernesto Gigliotti>
# Copyright (C) <2020>  <Camila Iglesias>
# Copyright (C) <2022>  <Facundo Falcone> - Improvements

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from modules import CoMa, FileManager

con = CoMa('./modules/configs.json')
fima = FileManager(con)


def test_is_not_integer():
    """Test if the percentage isn't integer type"""
    assert not type(fima.percentage) == int

def test_is_floating():
    """Test if the percentage is float type"""
    assert type(fima.percentage) == float

def test_is_boolean():
    """Test if the property returns a boolean"""
    assert type(fima.sort_by_percentage) == bool

def test_is_a_list_01():
    """Test if the excluded files are inside a list"""
    assert type(fima.excluded_files) == list

def test_is_a_list_02():
    """Test if the sufixes are inside a list"""
    assert type(fima.files_sufix) == list

def test_is_string():
    """Test if the output file path to create a csv file is string type"""
    assert type(fima.output_file_path) == str

def test_same_string():
    """Test if the output file path to create a csv file is the same that the ones declared in the json"""
    assert fima.output_file_path == './possible_copies.csv'


