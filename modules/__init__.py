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

from modules.common.color import Color
from modules.database.db_manager import DAOManager
from modules.models.config_manager import ConfigManager as CoMa
from modules.models.copy_detector import CopyDetectorManager
from modules.models.copy_manager import CopyManager
from modules.models.data_handler import DataHandler
from modules.models.file import File
from modules.models.file_manager import FileManager
from modules.models.group import Group
