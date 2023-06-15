def exists_word(word, instance):
    result = list()

    for i in range(len(instance)):
        file = instance.search(i)
        lines_with_word = []

        for j, line in enumerate(file["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                lines_with_word.append({"linha": j})

        if lines_with_word:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines_with_word,
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
