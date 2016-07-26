use mmh;

CREATE TABLE users (
    id int(11) NOT NULL AUTO_INCREMENT,
    handle varchar(200) DEFAULT NULL,
    email varchar(200) DEFAULT NULL,
    points int(5) DEFAULT NULL,
    created_at datetime DEFAULT NULL,
    updated_at datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE events (
    id int(11) NOT NULL AUTO_INCREMENT,
    name varchar(100) DEFAULT NULL,
    image_source varchar(200) DEFAULT NULL,
    description text DEFAULT NULL,
    location_id int(11) DEFAULT NULL,
    owner_id int(11) DEFAULT NULL,
    created_at datetime DEFAULT NULL,
    updated_at datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE user_events (
    id int(11) NOT NULL AUTO_INCREMENT,
    user_id int(11) DEFAULT NULL,
    event_id int(11) DEFAULT NULL,
    created_at datetime DEFAULT NULL,
    updated_at datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE locations (
    id int(11) NOT NULL AUTO_INCREMENT,
    url varchar(300) DEFAULT NULL,
    city varchar(300) DEFAULT NULL,
    state varchar(300) DEFAULT NULL,
    lat decimal(9,6) DEFAULT NULL,
    lon decimal(9,6) DEFAULT NULL,
    created_at datetime DEFAULT NULL,
    updated_at datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE reviews (
    id int(11) NOT NULL AUTO_INCREMENT,
    location_id int(11) DEFAULT NULL,
    user_id int(11) DEFAULT NULL,
    review text DEFAULT NULL,
    created_at datetime DEFAULT NULL,
    updated_at datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE api_keys (
    id int(11) NOT NULL AUTO_INCREMENT,
    api_key int(11) DEFAULT NULL,
    description text DEFAULT NULL,
    created_at datetime DEFAULT NULL,
    updated_at datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
);

