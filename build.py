# Script to build and update documentation
import src.definitions as df
import src.functions as fnc
import src.templates.html.pages as pages


def metpy_page():
    files = [df.metpy_files['index'], df.metpy_files['projects'], df.metpy_files['server'], df.metpy_files['docs']]
    texts = [pages.index, pages.projects, pages.server, pages.documentation]
    fnc.write_files(texts, files)


# Build documentation
if __name__ == '__main__':
    metpy_page()
