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
    expect(author_element).to_have_text("released: 2022")

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
def test_get_album_by_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/album_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Pixies")

    title_element = page.locator(".t-title")
    print(title_element)
    expect(title_element).to_have_text("Artist: Pixies")

    author_element = page.locator(".t-genre")
    expect(author_element).to_have_text("genre: rock")

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

    # Finally we click the button with the text 'Create Albumk'
    page.click("text=Create Album")

    # Just as before, the virtual browser acts just like a normal browser and
    # goes to the next page without us having to tell it to.

    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("Title: Drukqs")

    author_element = page.locator(".t-release-year")
    expect(author_element).to_have_text("Released: 2001")

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


# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
# def test_get_emoji(page, test_web_address): # Note new parameters
#     # We load a virtual browser and navigate to the /emoji page
#     page.goto(f"http://{test_web_address}/emoji")

#     # We look at the <strong> tag
#     strong_tag = page.locator("strong")

#     # We assert that it has the text ":)"
#     expect(strong_tag).to_have_text(":)")

# === End Example Code ===
