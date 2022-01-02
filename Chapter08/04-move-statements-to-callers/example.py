def render_person(person):
    result = []
    result.append(f"<p>{person.name}</p>")
    result.append(render_photo(person.photo))
    result.append(emit_photo_data(person.photo))
    result.append(f"<p>Location: {person.photo.location}</p>")
    return "\n".join(result)


def render_photo(photo):
    return f"<p>(Rendered HTML of the photo '{photo.title}')</p>"


def photo_div(photo):
    return "\n".join(
        [
            "<div>",
            emit_photo_data(photo),
            f"<p>Location: {photo.location}</p>",
            "</div>",
        ]
    )


def emit_photo_data(photo):
    return "\n".join(
        [f"<p>Title: {photo.title}</p>", f"<p>Date: {photo.date}</p>",]
    )
