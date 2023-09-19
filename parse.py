def load_deck_file():
    with open('deck.txt', 'r', encoding='UTF-8') as f:

        data = f.read()
        list = eval(data)
        # 配列の1つ目にｎ不要なテキストがい含まれているので削除する
        del list[0]

        return list