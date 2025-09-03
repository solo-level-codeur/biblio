-- Script de création de la base de données pour le projet Bibliothèque
-- Basé sur la structure actuelle du code

-- Création de la base de données
CREATE DATABASE IF NOT EXISTS biblio_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Utilisation de la base de données
USE biblio_db;

-- Création de la table book (structure actuelle)
CREATE TABLE IF NOT EXISTS book (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL COMMENT 'Titre du livre',
    author VARCHAR(255) NOT NULL COMMENT 'Auteur du livre',
    published_date DATE NOT NULL COMMENT 'Date de publication du livre',
    genre VARCHAR(100) NOT NULL COMMENT 'Genre du livre (roman, essai, etc.)',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Date de création de l\'enregistrement',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Date de dernière modification'
) ENGINE=InnoDB COMMENT='Table des livres de la bibliothèque';

-- Insertion de quelques données de test
INSERT INTO book (title, author, published_date, genre) VALUES
('Le Petit Prince', 'Antoine de Saint-Exupéry', '1943-04-06', 'Conte'),
('1984', 'George Orwell', '1949-06-08', 'Science-fiction'),
('L\'Étranger', 'Albert Camus', '1942-01-01', 'Roman'),
('Les Misérables', 'Victor Hugo', '1862-01-01', 'Roman'),
('Le Seigneur des Anneaux', 'J.R.R. Tolkien', '1954-07-29', 'Fantasy');

-- Affichage de la structure créée
DESCRIBE book;

-- Vérification des données insérées
SELECT * FROM book;
