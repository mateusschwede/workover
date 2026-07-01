package ubsocial.com.bookstore.model.entity

import com.fasterxml.jackson.annotation.JsonFormat
import jakarta.persistence.*
import jakarta.validation.constraints.NotBlank
import jakarta.validation.constraints.NotNull
import jakarta.validation.constraints.Size
import java.time.LocalDate

@Entity
class Book {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    var id: Long? = null

    @field:NotBlank
    @field:Size(min = 1, max = 255, message = "Título deve ter entre 1 e 255 caracteres")
    @Column(length = 255)
    var title: String = ""

    @field:NotBlank
    @field:Size(min = 1, max = 255, message = "Autor deve ter entre 1 e 255 caracteres")
    @Column(length = 255)
    var author: String = ""

    @field:NotNull
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd")
    @Column(name = "published_date")
    var published_date: LocalDate? = LocalDate.now()

    @field:NotBlank
    @field:Size(min = 13, max = 13, message = "ISBN precisa ter 13 caracteres")
    @Column(unique = true)
    var isbn: String = ""

    var pages: Int = 0

    @field:Size(min = 1, max = 255, message = "Capa/Gênero deve ter entre 1 e 255 caracteres")
    @Column(length = 255)
    var cover: String? = null

    @field:NotBlank
    @field:Size(min = 1, max = 255, message = "Idioma deve ter entre 1 e 255 caracteres")
    @Column(length = 255)
    var language: String = ""
}