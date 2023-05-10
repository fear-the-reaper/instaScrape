BEGIN;

SET client_encoding = 'LATIN1';

CREATE TABLE instagram_comments (
    id SERIAL PRIMARY KEY,
    post_url VARCHAR(255),
    username VARCHAR(255),
    comment_text TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    is_complaint BOOLEAN,
    sentiment VARCHAR(20)
);

COMMIT;