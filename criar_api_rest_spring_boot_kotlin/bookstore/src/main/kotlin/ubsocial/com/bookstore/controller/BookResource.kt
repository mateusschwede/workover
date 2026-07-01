package ubsocial.com.bookstore.controller

import jakarta.validation.Valid
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*
import ubsocial.com.bookstore.model.entity.Book
import ubsocial.com.bookstore.model.repositories.BookRepository

@RestController
@RequestMapping("/books")
class BookResource (private val bookRepository: BookRepository) {

    @GetMapping
    fun getAll(): List<Book> = bookRepository.findAll()

    @GetMapping("/{id}")
    fun getById(@PathVariable id: Long): ResponseEntity<Book> {
        val book = bookRepository.findById(id)
        return if (book.isPresent) ResponseEntity.ok(book.get())
        else ResponseEntity.notFound().build()
    }

    @PostMapping
    fun create(@RequestBody @Valid book: Book): Book = bookRepository.save(book)

    @PutMapping("/{id}")
    fun update(@PathVariable id: Long, @RequestBody @Valid book: Book): ResponseEntity<Book> {
        val optional = bookRepository.findById(id)
        if (optional.isEmpty) return ResponseEntity.notFound().build()

        val existing = optional.get()
        existing.title = book.title
        existing.author = book.author
        existing.published_date = book.published_date
        existing.isbn = book.isbn
        existing.pages = book.pages
        existing.cover = book.cover
        existing.language = book.language

        return ResponseEntity.ok(bookRepository.save(existing))
    }

    @DeleteMapping("/{id}")
    fun delete(@PathVariable id: Long): ResponseEntity<Void> {
        return if (bookRepository.existsById(id)) {
            bookRepository.deleteById(id)
            ResponseEntity.noContent().build()
        } else {
            ResponseEntity.notFound().build()
        }
    }

}