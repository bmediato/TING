from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = txt_importer(path_file)

    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return None

    file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    instance.enqueue(file)
    print(file)


def remove(instance):
    if instance.__len__() < 0:
        print("Não há elementos")
        return None

    delete = instance.dequeue()['nome_do_arquivo']
    print(f"Arquivo {delete} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
