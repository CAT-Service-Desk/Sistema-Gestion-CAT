CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255)
);

CREATE TABLE tickets (
    id INT PRIMARY KEY,
    user_id INT,
    status VARCHAR(20) DEFAULT 'OPEN',
    FOREIGN KEY (user_id) REFERENCES users(id)
);
