import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file in str(instance._data):
        return None

    data = txt_importer(path_file)

    data_return = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data
    }

    instance.enqueue(data_return)
    print(data_return)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")

    data = instance.dequeue()

    print(f"Arquivo {data['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
