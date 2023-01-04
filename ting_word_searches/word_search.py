def exists_word(word, instance):
    return_data = []
    occurrency = []
    path_name = ""

    for item in instance._data:
        for index, row in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in row.lower():
                occurrency.append({"linha": index})
                path_name = item["nome_do_arquivo"]

    return_data.append({
        "palavra": word,
        "arquivo": path_name,
        "ocorrencias": occurrency
    })

    if not len(occurrency):
        return []

    return return_data


def search_by_word(word, instance):
    return_data = []
    occurrency = []
    path_name = ""

    for item in instance._data:
        for index, row in enumerate(item["linhas_do_arquivo"], start=1):
            if word.lower() in row.lower():
                occurrency.append({
                    "linha": index,
                    'conteudo': row
                })
                path_name = item["nome_do_arquivo"]

    return_data.append({
        "palavra": word,
        "arquivo": path_name,
        "ocorrencias": occurrency
    })

    if not len(occurrency):
        return []

    return return_data
