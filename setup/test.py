from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from animais.models import Animal


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        """Estabelecer o caminho do webdriver e atribuir ao self.browser"""
        self.browser = webdriver.Chrome('C:/Users/CAJADO/Documents/projetos/tdd-django-alura/chromedriver.exe')
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'sim',
            venenoso = 'não',
            domestico = 'não'
        )

    def tearDown(self):
        """Fechar o navegador ao fim do teste"""
        self.browser.quit()
    
    '''def test_falha_proposital(self):
        """Teste exemplo de falha"""
        self.fail("Deu errado")'''

    def test_buscando_novo_animal(self):
        """
        Teste se um usuário encontra um animal pesquisando
        """
        #Usuário decida usar o site
        home_page = self.browser.get(self.live_server_url + "/")
        #Encontra e decide usar o menu do site chamado busca animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão')
        #Pesquisa por leão e clica no botão pesquisar.
        buscar_animal_input.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR, 'form button' ).click()
        #O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)
