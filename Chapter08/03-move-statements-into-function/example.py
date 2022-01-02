def render_person(person):
    result = []
    result.append(f"<p>{person.name}</p>")
    result.append(render_photo(person.photo))
    result.append(zznew(person.photo))
    return "\n".join(result)


def render_photo(photo):
    return f"<p>(Rendered HTML of the photo '{photo.title}')</p>"


def photo_div(photo):
    return "\n".join(["<div>", zznew(photo), "</div>",])


def zznew(photo):
    return "\n".join(
        [
            f"<p>Title: {photo.title}</p>",
            f"<p>Location: {photo.location}</p>",
            f"<p>Date: {photo.date}</p>",
        ]
    )
