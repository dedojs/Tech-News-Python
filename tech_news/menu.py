import sys
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_title,
    search_by_tag,
    search_by_date
)
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories, top_5_news


# Requisito 12
def filter_options2(choice):
    if (choice == 4):
        print('Digite a categoria: ')
        answer = input()
        return search_by_category(answer)

    elif (choice == 5):
        return top_5_news()

    elif (choice == 6):
        return top_5_categories()

    elif (choice == 7):
        print('Encerrando script')

    else:
        sys.stderr.write('Opção inválida\n')


def filter_options(choice):
    if (choice == 0):
        print('Digite quantas notícias serão buscadas: ')
        answer = int(input())
        return get_tech_news(answer)

    elif (choice == 1):
        print('Digite o título: ')
        answer = input()
        return search_by_title(answer)

    elif (choice == 2):
        print('Digite a data no formato aaaa-mm-dd: ')
        answer = input()
        return search_by_date(answer)

    elif (choice == 3):
        print('Digite a tag: ')
        answer = input()
        return search_by_tag(answer)

    else:
        filter_options2(choice)


def analyzer_menu():

    MENU = (
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    )

    print(MENU)

    try:
        option = input()
        choice = int(option)

    except ValueError:
        sys.stderr.write('Opção inválida\n')
    else:
        filter_options(choice)
