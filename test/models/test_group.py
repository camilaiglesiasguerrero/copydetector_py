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

import pytest
from modules import (Group, File)

# Initializes Clases
g_1 = Group(
    File('./Repositories/test_files2/main.c', 25, 'main.c')
)
g_1.append_file(File('./Repositories/test_files2/main2.c', 25, 'main2.c'))

def test_check_if_has_copies():
    """Test if the group has copies"""
    assert g_1.has_copies

def test_check_if_hasnt_copies():
    """Test if the group hasn't copies"""
    g_2 = Group(File('./a_path/', 25, 'first_filename'))
    assert not g_2.has_copies

def test_files_str():
    """Test if all the elements in the list are string type"""
    for line in g_1.return_files:
        assert type(line) == str

@pytest.mark.parametrize(
    "new_file, expected", [
        (File('./Repositories/test_files2/main.c', 25, 'main.c'), True),
        (File('./Repositories/test_files2/main2.c', 25, 'main2.c'), True),
        (File('./Repositories/test_files2/repo3/TP_copia_repo1/funciones.c', 50, 'funciones.c'), False),
        (File('./Repositories/test_files2/repo3/TP_copia_repo1/funciones.h', 50, 'funciones.h'), False)
    ])
def test_belonging(new_file: File, expected: bool):
    """Test if the files passed by parameters belongs the the group_1"""
    assert g_1.file_belong(new_file) == expected

def test_percent_60():
    """Test if the default percentage value is 60"""
    assert g_1.same_lines_percent == 60
