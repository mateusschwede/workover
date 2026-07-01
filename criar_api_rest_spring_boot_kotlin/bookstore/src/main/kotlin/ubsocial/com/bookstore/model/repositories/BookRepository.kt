package ubsocial.com.bookstore.model.repositories
import org.springframework.data.jpa.repository.JpaRepository
import ubsocial.com.bookstore.model.entity.Book

interface BookRepository : JpaRepository<Book, Long>