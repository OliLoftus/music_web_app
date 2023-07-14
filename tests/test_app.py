from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
test Get /albums
"""
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator('h2')
    paragraph_tags = page.locator('p')
    expect(h2_tags).to_have_text([
        'Album one',
        'Album two',
        'Album three',
        'Album four'
    ])
    expect(paragraph_tags).to_have_text([
        'released: 2022',
        'released: 2021',
        'released: 2018',
        'released: 2000'
    ])

def test_get_album_by_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Album one")

    title_element = page.locator(".t-title")
    print(title_element)
    expect(title_element).to_have_text("Title: Album one")

    author_element = page.locator(".t-release-year")
    expect(author_element).to_have_text("Released: 2022")

"""
GET /artists/
"""
def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    h2_tags = page.locator('h2')
    paragraph_tags = page.locator('p')
    expect(h2_tags).to_have_text([
        'Pixies',
        'ABBA',
        'Taylor Swift',
        'Nina Simone'
    ])
    expect(paragraph_tags).to_have_text([
        'genre: rock',
        'genre: pop',
        'genre: pop',
        'genre: jazz'
    ])

"""
GET /artists<id>
"""
def test_get_artist_by_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Pixies")

    title_element = page.locator(".t-name")
    expect(title_element).to_have_text("Artist: Pixies")

    author_element = page.locator(".t-genre")
    expect(author_element).to_have_text("Genre: rock")

"""
When we create a new album
We see it in the albums index
"""
def test_create_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/albums")

    # This time we click the link with the text 'Add a new album'
    page.click("text=Add a new album")

    # Then we fill out the field with the name attribute 'title'
    page.fill("input[name='title']", "Drukqs")

    # And the field with the name attribute 'release_year'
    page.fill("input[name='release_year']", "2001")

    # And the field with the name attribute 'release_year'
    page.fill("input[name='artist_id']", "10")

    # Finally we click the button with the text 'Create Albumk'
    page.click("text=Create Album")

    # Just as before, the virtual browser acts just like a normal browser and
    # goes to the next page without us having to tell it to.

    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("Title: Drukqs")

    release_element = page.locator(".t-release-year")
    expect(release_element).to_have_text("Released: 2001")


"""
If we create a new album without a title or release_year
We see an error message
"""
def test_create_album_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.click("text=Create Album")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Title can't be blank, Release year can't be blank")

    """
When we create a new artist
We see it in the srtists index
"""
def test_create_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/artists")

    # This time we click the link with the text 'Add a new artist'
    page.click("text=Add a new artist")

    # Then we fill out the field with the name attribute 'title'
    page.fill("input[name='name']", "Bicep")

    # And the field with the name attribute 'release_year'
    page.fill("input[name='genre']", "electronic")

    # Finally we click the button with the text 'Create Albumk'
    page.click("text=Create Artist")

    # Just as before, the virtual browser acts just like a normal browser and
    # goes to the next page without us having to tell it to.

    title_element = page.locator(".t-name")
    expect(title_element).to_have_text("Artist: Bicep")

    release_element = page.locator(".t-genre")
    expect(release_element).to_have_text("Genre: electronic")

"""
If we create a new artist without a title or genre
We see an error message
"""
def test_create_artist_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.click("text=Create Artist")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Artist can't be blank, Genre can't be blank")
