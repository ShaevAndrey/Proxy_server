from os import strerror


class ModifyPage:
    """
    Класс модифицирует страничку и возвращает страницу с добавлением символа по заданию
    """

    def __init__(self, page:str, letters_number:int) -> None:
        """
        получает на вход исходный текст страницы и количество букв в слове
        """
        self.letters_number = letters_number
        self.page = page

    
    def modify_page(self) -> None:
        """ 
        Изменяет исходную страницу на основании заданного условия
        """
        tag = True
        content=''
        len_word = 0
        for letter in self.page:
            if letter == '<':
                if len_word==self.letters_number:
                    letter = '™' + letter
                    len_word = 0
                content = content + letter
                tag = True
                continue
            if letter == '>' and tag:
                content = content + letter
                tag = False
                continue
            if tag:
                content = content + letter
                continue
            if letter in [' ', ';', ':', '=', '.', ',', '(', ')']: 
                if len_word==self.letters_number:
                    content = content + '™'+ letter
                    len_word = 0
                else:
                    content = content + letter
                    len_word = 0
                continue
            content = content + letter
            len_word = len_word + 1
        self.modified_page = content

    
    def get_modify_page(self) -> str:
        """
        Возвращает модифицированную страницу
        """
        return self.modified_page
