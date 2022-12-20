/** GNU General Public License V3
*
* Copyright (C) <2022>  <Facundo Falcone>
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

CREATE TABLE IF NOT EXISTS `T_NAME`(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `is_copy` TEXT NOT NULL,
    `group_number` TEXT NOT NULL,
    `file_name` TEXT NOT NULL,
    `file_path` TEXT NOT NULL,
    `percentage` FLOAT NOT NULL CHECK(`percentage` > 59),
    `dataingestiondttm` TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
);
