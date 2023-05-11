BEGIN;

SET client_encoding = 'LATIN1';

CREATE TABLE instagram_comments (
    id SERIAL PRIMARY KEY,
    post_url VARCHAR(255),
    username VARCHAR(255),
    comment TEXT,
    is_complaint BOOLEAN,
    sentiment VARCHAR(20),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

COMMIT;