DROP TABLE IF EXISTS contributor;
DROP TABLE IF EXISTS project;

DROP INDEX IF EXISTS contributor_project_id_fk;
DROP INDEX IF EXISTS contributor_project_id_name_index;
DROP INDEX IF EXISTS project_title_uindex;

VACUUM;

create table project
(
    id       integer
        constraint project_pk
            primary key autoincrement,
    title    text not null,
    manager  text not null,
    deadline text not null
);

create unique index project_title_uindex
    on project (title);

create table contributor
(
    id         INTEGER
        constraint contributor_pk
            primary key autoincrement,
    project_id INTEGER not null
        constraint contributor_project_id_fk
            references project,
    name       text    not null,
    value      integer
);

create index contributor_project_id_name_index
    on contributor (project_id, name);

/*

DELETE FROM contributor WHERE 1=1
DELETE FROM project WHERE 1=1

*/
