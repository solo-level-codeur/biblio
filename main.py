from dotenv import load_dotenv
import os 
from PyQt5.QtWidgets import QApplication
import sys 
from src.views.book_view import BookView
from src.managers.book_manager import BookManager
from src.repositories.book_repository import BookRepository
from src.controllers.book_controller import BookController



if __name__ == "__main__":


    load_dotenv()

    app = QApplication(sys.argv)

    repo = BookRepository(host=os.getenv("DB_HOST"), database=os.getenv("DB_DATABASE"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"))
    
    manager = BookManager(repo)

    view = BookView()
    
    controller = BookController(manager, view)

    view.show()

    sys.exit(app.exec_())