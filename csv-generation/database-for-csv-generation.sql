DROP TABLE IF EXISTS collaboration;
DROP TABLE IF EXISTS raw_project;

DROP INDEX IF EXISTS collaboration_raw_project_id_contributor_index;
DROP INDEX IF EXISTS collaboration_raw_project_id_fk;
DROP INDEX IF EXISTS raw_project_title_uindex;
DROP INDEX IF EXISTS raw_project_deadline_index;

create table raw_project
(
    id       integer
        constraint raw_project_pk
            primary key autoincrement,
    title    text    not null,
    manager  text    not null,
    deadline integer not null
);

create index raw_project_deadline_index
    on raw_project (deadline desc);

create unique index raw_project_title_uindex
    on raw_project (title);

create table collaboration
(
    raw_project_id integer
        constraint collaboration_raw_project_id_fk
            references raw_project (id),
    contributor    text not null,
    pie            INTEGER
);

create index collaboration_raw_project_id_contributor_index
    on collaboration (raw_project_id, contributor);

/* PURGE TABLES

DELETE
FROM collaboration
WHERE 1 = 1;
DELETE
FROM raw_project
WHERE 1 = 1;

*/
