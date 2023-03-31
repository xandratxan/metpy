# Main section HTML template for MetPy website

def main_section_template(title, description, cards):
    # Main section HTML template for MetPy website
    text = (
        f'            <!-- Introduction -->\n'
        f'            <article class="post featured">\n'
        f'                <header class="major">\n'
        f'                    <h2>{title}</h2>\n'
        f'                    <p>{description}</p>\n'
        f'                </header>\n'
        f'            </article>\n'
        f'            <!-- Cards -->\n'
    )
    for card in cards:
        text += card_template(card['name'], card['title'], card['brief_description'], card['html_path'],
                              card['image_path'], card['image_name'])
    return text


def card_template(name, title, brief_description, href, images_path, image_name):
    # Card HTML template for main section of MetPy website
    text = (
        f'            <!-- Card {name} -->\n'
        f'            <section class="posts">\n'
        f'                <article>\n'
        f'                    <header>\n'
        f'                        <h2><a href="{href}">{title}</a></h2>\n'
        f'                        <span class="date"></span>\n'
        f'                    </header>\n'
        f'                    <div class="row">\n'
        f'                        <div class="col-4 col-12-small"></div>\n'
        f'                        <div class="col-4 col-12-small">\n'
        f'                        <a href="{href}" class="image fit"><img src="{images_path}{image_name}" alt="{image_name}"/></a>\n'
        f'                        </div>\n'
        f'                        <div class="col-4 col-12-small"></div>\n'
        f'                    </div>\n'
        f'                    {brief_description}\n'
        f'                    <p></p>\n'
        f'                    <ul class="actions special">\n'
        f'                    <li><a href="{href}" class="button">Read more</a></li>\n'
        f'                    </ul>\n'
        f'                </article>\n'
        f'            </section>\n'
    )
    return text
