'''PRINCIPALE
Cerca il fungo su Wikipedia a seconda del parametro desiderato
    0.1 crea un elenco di possibili funghi da wikipedia
    1.1 prende l'input della/e caratteristica/che
        1.1.1 controlla sia valido (no numeri, no caratteri speciali, no spazi)  --> Exception(ShoomBase(ShroomAttrNotExists)
    1.2 cerca su wikipedia tra le pagine dei funghi
        1.2.1 controlla esista tra le caratteristiche dei funghi --> Exception(ShroomBase(WikiNotExists))
    1.3 troppo scomodo, ricerche macchinose, meglio fare un db a documenti (piu' veloce/facile da gestire)
    {carica le pagine trovate in una lista tenendo solo nome, la descrizione, la tabella e le prime 3 immagini
        ovvero [ {nome:'nome fungo', descr: 'descrizione, habitat', tab: 'Nome comune: fabio, etc', imgs: img1,img2,img}, {altro fungo} ]}
'''
from urllib.request import urlopen
import webbrowser

URL_WIKI_IT = 'https://it.wikipedia.org/wiki/'
DICT = {
    'URL_VELENOSI' : URL_WIKI_IT + 'Categoria:Funghi_velenosi',\
    'URL_MORTALI' : URL_WIKI_IT + 'Categoria:Funghi_mortali',\
    'URL_COMMESTIBILI' : URL_WIKI_IT + 'Categoria:Funghi_commestibili',\
    'URL_QUASI_COMM' : URL_WIKI_IT + 'Categoria:Funghi_commestibili_con_riserva',\
    'URL_NON_COMM' : URL_WIKI_IT + 'Categoria:Funghi_non_commestibili',\
}

class ShroomBase(Exception):
    def __init__(self, message, shroom):
        super().__init__(message)
        self.shroom = shroom

class ShroomAttrNotEx(ShroomBase):
    def __init__(self, message, shroom_attr):
        super().__init__(message, shroom='')
        self.shroom_attr = shroom_attr

class WikiNotEx(ShroomBase):
    def __init__(self, message, shroom_attr):
        super().__init__(message, shroom='')
        self.shroom_attr = shroom_attr


class Shroom():
    def __init__(self, str_name):
        self.latin_name = str_name

    def __str__(self):
        return f'{self.latin_name}'

    @classmethod
    def validate(cls, possible_name):
        temp = possible_name.split()
        if len(temp) <=4:
            possible_name = possible_name.replace(' ', '_')
            _shroom = cls(possible_name)
            return _shroom
        else: return None

    # crea il link del fungo, ritorna una stringa
    def create_link(self):
        url_shroom = URL_WIKI_IT + self.latin_name
        return url_shroom #string
    
    # extract a shroom's table
    def html_table(self):
        return Soup_like.slice_of_html(self.create_link(), '<table class="infobox sinottico"', '</tr></tbody></table>')


class Soup_like():

    @staticmethod
    def write_html(string_with_html):
        stream = open('shroom_finder\\created_html\\provatab.html', 'w')
        stream.write(string_with_html)
        stream.close()

    @staticmethod
    def open_html(local_url):
        local_url = 'shroom_finder\\created_html\\provatab.html'
        webbrowser.open_new_tab(local_url)

    @staticmethod
    # ignore html and return a string with data
    def wash_html(html_code_as_string):
        start = html_code_as_string.find('>') +1
        end = 0
        temp_data = ''
        while end != -1:
            end = html_code_as_string.find('<', start)
            if html_code_as_string[start: end] not in ['', ' ', '  ', '\n', '\t']:
                temp_data += html_code_as_string[start: end] + '\n'
            start = html_code_as_string.find('>', end) +1
        return temp_data #string

    @staticmethod
    # more general, extract a slice of html 
    def slice_of_html(url, starting_str, ending_str):
        with urlopen(url) as opened_url:
            webpage = opened_url.read()
            webpage = webpage.decode('utf-8')
            first = webpage.find(starting_str)
            last = webpage.find( ending_str, first)
            new_page = webpage[ first : last + len(ending_str) ]
        return new_page

    @staticmethod
    # create a list of shrooms
    def list_of_cat_shrooms(url_cat_shrooms):
        cutted_webpage = Soup_like.slice_of_html(url_cat_shrooms, '<h3>A</h3>', '<noscript><img src')   
        start = cutted_webpage.find('>')
        end = 0
        list_cat_shrooms = []
        while end != -1:
            temp_shroom_name = ''
            end = cutted_webpage.find('<', start)
            if cutted_webpage.find('>', end) - end < 4:
                temp_shroom_name = cutted_webpage[start+1: end]
                if len(temp_shroom_name) > 2 and len(temp_shroom_name) < 80:
                    print(temp_shroom_name)
                    list_cat_shrooms.append(Shroom.validate(temp_shroom_name))
            start = cutted_webpage.find('>', end)
        return list_cat_shrooms #list of strings
    
    @staticmethod
    # create and open in browser an html table of the shroom
    def html_table_browser(shroom):
        Soup_like.open_html(Soup_like.write_html(Shroom.html_table(shroom)))