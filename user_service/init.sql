CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    age INT NOT NULL
);

INSERT INTO users (username, age) VALUES ('John Doe', 30);
INSERT INTO users (username, age) VALUES ('Jane Smith', 25);
INSERT INTO users (username, age) VALUES ('Alice Johnson', 27);
INSERT INTO users (username, age) VALUES ('Bob Brown', 22);
INSERT INTO users (username, age) VALUES ('Charlie Black', 35);
INSERT INTO users (username, age) VALUES ('Daisy White', 29);
INSERT INTO users (username, age) VALUES ('Eve Green', 31);
INSERT INTO users (username, age) VALUES ('Frank Blue', 33);
INSERT INTO users (username, age) VALUES ('Grace Red', 28);
INSERT INTO users (username, age) VALUES ('Henry Orange', 40);
