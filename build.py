# Script to build and update documentation
import src.definitions as df
import src.functions as fnc
import src.html.main_pages as pages


def metpy_page():
    files = [df.file_paths['index'], df.file_paths['projects'], df.file_paths['server'], df.file_paths['docs']]
    texts = [pages.index, pages.projects, pages.server, pages.documentation]
    fnc.write_files(texts, files)


# Build documentation
if __name__ == '__main__':
    metpy_page()
