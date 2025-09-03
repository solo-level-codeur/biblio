import mysql.connector

from mysql.connector import Error
from src.entities.book_entity import BookEntity

class BookRepository:
    def __init__(self, host, database, user, password):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                port=8889,
                database=database,
                user=user,
                password=password
            )
            if self.connection.is_connected():
                print("Connexion à la base de données réussie")
            else :
                print("Connexion à la base de données échouée")
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            self.connection = None

    def create(self, book_entity) -> int:
        """
        Insère un livre dans la base de données et retourne l'ID généré.
        :param book_entity: Instance de BookEntity contenant les données.
        :return: ID du livre créé.
        """
        query = """
        INSERT INTO book (title, author, published_date, genre)
        VALUES (%s, %s, %s, %s)
        """
        values = (book_entity.title, book_entity.author, book_entity.published_date, book_entity.genre)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Erreur lors de l'ajout du livre : {e}")
            return None

    def read_all(self):
        """
        Récupère tous les livres sous forme d'objets BookEntity.
        :return: Liste d'instances de BookEntity.
        """
        query = "SELECT * FROM book"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            books = cursor.fetchall()
            return [BookEntity(
                id=book["id"],
                title=book["title"],
                author=book["author"],
                published_date=book["published_date"],
                genre=book["genre"]
                ) for book in books]
        except Error as e:
            print(f"Erreur lors de la récupération des livres : {e}")
            return []

    def read_by_id(self, book_id):
        """
        Récupère un livre par son ID.
        :param book_id: ID du livre.
        :return: Instance de BookEntity ou None si non trouvé.
        """
        query = "SELECT * FROM book WHERE id = %s"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, (book_id,))
            book = cursor.fetchone()
            return BookEntity(
                id=book["id"],
                title=book["title"],
                author=book["author"],
                published_date=book["published_date"],
                genre=book["genre"]
                ) if book else None
        except Error as e:
            print(f"Erreur lors de la récupération du livre : {e}")
            return None

    def update(self, book_entity):
        print(book_entity)
        """
        Met à jour un livre existant et retourne l'entité mise à jour.
        :param book_entity: Instance de BookEntity contenant les nouvelles données.
        :return: BookEntity après mise à jour, ou None en cas d'erreur.
        """
        query = """
        UPDATE book
        SET title = %s, author = %s, published_date = %s, genre = %s
        WHERE id = %s
        """
        values = (
            book_entity.title,
            book_entity.author,
            book_entity.published_date,
            book_entity.genre,
            book_entity.id
        )
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            if cursor.rowcount > 0:
                return self.read_by_id(book_entity.id)
            return None
        except Error as e:
            print(f"Erreur lors de la mise à jour du livre : {e}")
            return None

    def delete(self, book_id):
        """
        Supprime un livre par son ID.
        :param book_id: ID du livre.
        :return: Booléen indiquant si la suppression a été effectuée.
        """
        query = "DELETE FROM book WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (book_id,))
            self.connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Erreur lors de la suppression du livre : {e}")
            return False

    def __del__(self):
        """
        Ferme la connexion à la base de données.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connexion à la base de données fermée")
        