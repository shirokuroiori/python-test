CREATE DATABASE IF NOT EXISTS PYTESTDB collate utf8_unicode_ci;

CREATE TABLE 'USER_TABLE'
(
    'member_id' VARCHAR(30) NOT NULL,
    'member_name' VARCHAR(40) NOT NULL,
    'member_class' VARCHAR(1) NOT NULL,
    'create_date' VARCHAR(20) NOT NULL,
    'update_date' VARCHAR(20) NOT NULL,
    primary key (team_id)
) ENGINE = InnoDB
    DEFAULT CHARSET = utf8;

CREATE TABLE 'TEAM_TABLE'
(
    'team_id' VARCHAR(30) NOT NULL,
    'team_name' VARCHAR(40) NOT NULL,
    'create_date' VARCHAR(20) NOT NULL,
    'update_date' VARCHAR(20) NOT NULL,
    primary key (team_id)
) ENGINE = InnoDB
    DEFAULT CHARSET = utf8;