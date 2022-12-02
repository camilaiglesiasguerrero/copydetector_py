CREATE TABLE IF NOT EXISTS `T_NAME`(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `is_copy` TEXT NOT NULL,
    `group_number` TEXT NOT NULL,
    `file_name` TEXT NOT NULL,
    `file_path` TEXT NOT NULL,
    `percentage` FLOAT NOT NULL CHECK(`percentage` > 59),
    `dataingestiondttm` TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
);
