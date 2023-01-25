CREATE TABLE firewall.ADV_ENTITY
(
    ID     bigint(20) primary key,
    STATUS varchar(295)
) charset = utf8;



CREATE TABLE firewall.ENTITY_COUNTRY
(
    ID            bigint(20) NOT NULL primary key,
    ADV_ENTITY_ID bigint(20) DEFAULT NULL,
    COUNTRY_CODE  varchar(4) DEFAULT NULL,
    EXCLUDE       tinyint(1) DEFAULT NULL,
    KEY           adv_entity_id_index (ADV_ENTITY_ID)
) charset = utf8;

CREATE TABLE firewall.ENTITY_STATE
(
    ID            bigint(11) NOT NULL,
    ADV_ENTITY_ID bigint(20) DEFAULT NULL,
    STATE_CODE    varchar(4) DEFAULT NULL,
    EXCLUDE       tinyint(1) DEFAULT NULL,
    PRIMARY KEY (ID)
) charset = utf8;


CREATE TABLE firewall.ENTITY_DMA
(
    ID            bigint(11) NOT NULL,
    ADV_ENTITY_ID bigint(20) DEFAULT NULL,
    DMA_CODE      varchar(4) DEFAULT NULL,
    EXCLUDE       tinyint(1) DEFAULT NULL,
    PRIMARY KEY (ID),
    KEY           adv_entity_id_index (ADV_ENTITY_ID)
) charset = utf8;

CREATE TABLE firewall.ENTITY_IP
(
    ID            bigint(20),
    ADV_ENTITY_ID bigint(20) DEFAULT NULL,
    IP            text,
    EXCLUDE       tinyint(1) DEFAULT NULL,
    PRIMARY KEY (ID)
) charset = utf8;

INSERT INTO firewall.ADV_ENTITY (ID, STATUS)
VALUES (10704, 'New'),
       (22, 'Active'),
       (9855, 'New'),
       (17802, 'New');

INSERT INTO firewall.ENTITY_COUNTRY (ID, ADV_ENTITY_ID, COUNTRY_CODE, EXCLUDE)
VALUES (4592, 10704, 'IN', 0);

INSERT INTO firewall.ENTITY_STATE (ID, ADV_ENTITY_ID, STATE_CODE, EXCLUDE)
VALUES (414, 9855, 'ZZ', 0);

INSERT INTO firewall.ENTITY_DMA (ID, ADV_ENTITY_ID, DMA_CODE, EXCLUDE)
VALUES (9890, 17802, '501', 0);

INSERT INTO firewall.ENTITY_IP (ID, ADV_ENTITY_ID, IP, EXCLUDE)
VALUES (26, 22, '1.1.1.1', 1);