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
