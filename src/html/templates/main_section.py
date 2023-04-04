"""Main section HTML templates for MetPy website."""


def main_section_template(title, brief_description, description, image, cards):
    """Main section HTML template for MetPy website.

    Parameters
    ----------
    title : str
        Main section title.
    brief_description : str
        Main section brief description.
    description : str
        Main section description.
    image : str
        Main section image file name.
    cards : list
        Dictionaries for main section cards.
    """
    i = 12
    cards_text = ''
    for card in cards:
        cards_text += card_template(card['name'], card['title'], card['brief_description'],
                                    card['html_path'], card['image'])
    text = (
        f'{" " * i}<!-- Introduction -->\n'
        f'{" " * i}<article class="post featured">\n'
        f'{" " * i}    <header class="major">\n'
        f'{" " * i}        <h2>{title}</h2>\n'
        f'{" " * i}        <p>{brief_description}</p>\n'
        f'{" " * i}    </header>\n'
        f'{" " * i}    <div class="row">\n'
        f'{" " * i}        <div class="col-5 col-12-small"></div>\n'
        f'{" " * i}        <div class="col-2 col-12-small">\n'
        f'{" " * i}            <span class="image fit"><img src="./images/{image}" alt="{image}" /></span>\n'
        f'{" " * i}        </div>\n'
        f'{" " * i}        <div class="col-5 col-12-small"></div>\n'
        f'{" " * i}    </div>\n'
        f'{" " * i}    <p>{description}</p>'
        f'{" " * i}</article>\n'
        f'{" " * i}<!-- Cards -->\n'
        f'{" " * i}<section class="posts">\n'
        f'{cards_text}'
        f'{" " * i}</section>\n'
    )
    return text


def card_template(name, title, brief_description, href, image):
    """Template for card section of main section HTML templates for MetPy website.

    Parameters
    ----------
    name : str
        Card name.
    title : str
        Card title.
    brief_description : str
        Card brief description.
    href : str
        Card interactive link.
    image : str
        Card image file name.
    """
    i = 16
    text = (
        f'{" " * i}<!-- Card {name} -->\n'
        f'{" " * i}<article>\n'
        f'{" " * i}    <header>\n'
        f'{" " * i}        <h2><a href="{href}">{title}</a></h2>\n'
        f'{" " * i}        <span class="date"></span>\n'
        f'{" " * i}    </header>\n'
        f'{" " * i}    <div class="row">\n'
        f'{" " * i}        <div class="col-4 col-12-small"></div>\n'
        f'{" " * i}        <div class="col-4 col-12-small">\n'
        f'{" " * i}            <a href="{href}" class="image fit"><img src="./images/{image}" alt="{image}"/></a>\n'
        f'{" " * i}        </div>\n'
        f'{" " * i}        <div class="col-4 col-12-small"></div>\n'
        f'{" " * i}    </div>\n'
        f'{" " * i}    {brief_description}\n'
        f'{" " * i}    <p></p>\n'
        f'{" " * i}    <ul class="actions special">\n'
        f'{" " * i}    <li><a href="{href}" class="button">Read more</a></li>\n'
        f'{" " * i}    </ul>\n'
        f'{" " * i}</article>\n'
    )
    return text
