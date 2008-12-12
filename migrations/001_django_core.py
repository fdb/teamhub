from dmigrations.mysql import migrations as m
import datetime
auth = m.Migration(sql_up=["""
    CREATE TABLE `auth_permission` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(50) NOT NULL,
        `content_type_id` integer NOT NULL,
        `codename` varchar(100) NOT NULL,
        UNIQUE (`content_type_id`, `codename`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `auth_group` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(80) NOT NULL UNIQUE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `auth_user` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `username` varchar(30) NOT NULL UNIQUE,
        `first_name` varchar(30) NOT NULL,
        `last_name` varchar(30) NOT NULL,
        `email` varchar(75) NOT NULL,
        `password` varchar(128) NOT NULL,
        `is_staff` bool NOT NULL,
        `is_active` bool NOT NULL,
        `is_superuser` bool NOT NULL,
        `last_login` datetime NOT NULL,
        `date_joined` datetime NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `auth_message` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `user_id` integer NOT NULL,
        `message` longtext NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `auth_message` ADD CONSTRAINT user_id_refs_id_650f49a6 FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
""", """
    CREATE TABLE `auth_group_permissions` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `group_id` integer NOT NULL,
        `permission_id` integer NOT NULL,
        UNIQUE (`group_id`, `permission_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `auth_group_permissions` ADD CONSTRAINT group_id_refs_id_3cea63fe FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
""", """
    ALTER TABLE `auth_group_permissions` ADD CONSTRAINT permission_id_refs_id_5886d21f FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
""", """
    CREATE TABLE `auth_user_groups` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `user_id` integer NOT NULL,
        `group_id` integer NOT NULL,
        UNIQUE (`user_id`, `group_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `auth_user_groups` ADD CONSTRAINT user_id_refs_id_7ceef80f FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
""", """
    ALTER TABLE `auth_user_groups` ADD CONSTRAINT group_id_refs_id_f116770 FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
""", """
    CREATE TABLE `auth_user_user_permissions` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `user_id` integer NOT NULL,
        `permission_id` integer NOT NULL,
        UNIQUE (`user_id`, `permission_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT user_id_refs_id_dfbab7d FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
""", """
    ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT permission_id_refs_id_67e79cb FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
""", """
    -- The following references should be added but depend on non-existent tables:
""", """
    -- ALTER TABLE `auth_permission` ADD CONSTRAINT content_type_id_refs_id_728de91f FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
"""], sql_down=["""
    DROP TABLE `auth_user_user_permissions`;
""", """
    DROP TABLE `auth_user_groups`;
""", """
    DROP TABLE `auth_group_permissions`;
""", """
    DROP TABLE `auth_message`;
""", """
    DROP TABLE `auth_user`;
""", """
    DROP TABLE `auth_group`;
""", """
    DROP TABLE `auth_permission`;
"""])

contenttypes = m.Migration(sql_up=["""
    CREATE TABLE `django_content_type` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `name` varchar(100) NOT NULL,
        `app_label` varchar(100) NOT NULL,
        `model` varchar(100) NOT NULL,
        UNIQUE (`app_label`, `model`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
"""], sql_down=["""
    DROP TABLE `django_content_type`;
"""])

sessions = m.Migration(sql_up=["""
    CREATE TABLE `django_session` (
        `session_key` varchar(40) NOT NULL PRIMARY KEY,
        `session_data` longtext NOT NULL,
        `expire_date` datetime NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
"""], sql_down=["""
    DROP TABLE `django_session`;
"""])

sites = m.Migration(sql_up=["""
    CREATE TABLE `django_site` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `domain` varchar(100) NOT NULL,
        `name` varchar(50) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    INSERT INTO `django_site` (`domain`, `name`) 
    VALUES ('example.com', 'example.com')
    ;
"""], sql_down=["""
    DROP TABLE `django_site`;
"""])

flatpages = m.Migration(sql_up=["""
    CREATE TABLE `django_flatpage` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `url` varchar(100) NOT NULL,
        `title` varchar(200) NOT NULL,
        `content` longtext NOT NULL,
        `enable_comments` bool NOT NULL,
        `template_name` varchar(70) NOT NULL,
        `registration_required` bool NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    CREATE TABLE `django_flatpage_sites` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `flatpage_id` integer NOT NULL,
        `site_id` integer NOT NULL,
        UNIQUE (`flatpage_id`, `site_id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    ALTER TABLE `django_flatpage_sites` ADD CONSTRAINT flatpage_id_refs_id_3f17b0a6 FOREIGN KEY (`flatpage_id`) REFERENCES `django_flatpage` (`id`);
""", """
    ALTER TABLE `django_flatpage_sites` ADD CONSTRAINT site_id_refs_id_4e3eeb57 FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`);
"""], sql_down=["""
    DROP TABLE `django_flatpage_sites`;
""", """
    DROP TABLE `django_flatpage`;
"""])

admin = m.Migration(sql_up=["""
    CREATE TABLE `django_admin_log` (
        `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `action_time` datetime NOT NULL,
        `user_id` integer NOT NULL,
        `content_type_id` integer NULL,
        `object_id` longtext NULL,
        `object_repr` varchar(200) NOT NULL,
        `action_flag` smallint UNSIGNED NOT NULL,
        `change_message` longtext NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    ;
""", """
    -- The following references should be added but depend on non-existent tables:
""", """
    -- ALTER TABLE `django_admin_log` ADD CONSTRAINT user_id_refs_id_c8665aa FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
""", """
    -- ALTER TABLE `django_admin_log` ADD CONSTRAINT content_type_id_refs_id_288599e6 FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
"""], sql_down=["""
    DROP TABLE `django_admin_log`;
"""])

migration = m.Compound([auth, contenttypes, sessions, sites, flatpages, admin])