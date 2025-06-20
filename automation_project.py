# -*- coding: utf-8 -*-
"""selenium-automation-project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oNNVTZJctydkCCvRsuz-NxkXglX4ePPy

# Projet d’automatisation avec Playwright - foodaffairs.fr

Ce Script automatise la navigation sur le site [foodaffairs.fr](https://foodaffairs.fr/) pour tester le parcours utilisateur suivant :

- Ouverture de la page principale
- Recherche et clic sur le bouton "Réserver"
- Clic sur le bouton de confirmation sur la page suivante
- Affichage de la page finale atteinte

L'objectif est de démontrer une automatisation simple de test fonctionnel avec Playwright en Python, dans Google Colab.

---

##1. Installation des dépendances (playwright, nest_asyncio)
"""

!pip install playwright
!playwright install

"""##Import & Setup (patch asyncio pour Colab)"""

import nest_asyncio
nest_asyncio.apply()

import asyncio
from playwright.async_api import async_playwright

"""##Fonctions utilitaires / actions

"""

async def ouvrir_page(page, url):
    await page.goto(url)
    print(f"Page ouverte : {url}")
    titre = await page.title()
    print("Titre de la page :", titre)

async def cliquer_bouton(page, selector, description="bouton"):
    print(f"Clique sur {description} avec le sélecteur : {selector}")
    await page.wait_for_selector(selector)
    await page.click(selector)
    await page.wait_for_load_state("networkidle")

"""##Script principal"""

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # 1. Ouverture page principale
        await ouvrir_page(page, "https://foodaffairs.fr")

        # 2. Clique premier bouton "Réserver"
        selector1 = "#section_restaurants > div.elementor-container.elementor-column-gap-no > div > div > section.elementor-section.elementor-inner-section.elementor-element.elementor-element-9355fd5.elementor-section-full_width.elementor-section-height-default.elementor-section-height-default > div.elementor-container.elementor-column-gap-extended > div.elementor-column.elementor-col-33.elementor-inner-column.elementor-element.elementor-element-2683a6d > div > section > div > div.elementor-column.elementor-col-50.elementor-inner-column.elementor-element.elementor-element-bde8365 > div > div > div > div > a"
        await cliquer_bouton(page, selector1, "bouton Réserver principal")

        # 3. Clique deuxième bouton
        selector2 = "#post-9582 > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-a99c032.elementor-section-content-top.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div.elementor-column.elementor-col-33.elementor-top-column.elementor-element.elementor-element-72a1e38 > div > div > div > div > a"
        await cliquer_bouton(page, selector2, "bouton de confirmation")

        # 4. Résultat final
        print("Page finale URL:", page.url)
        print("Page finale Titre:", await page.title())

        await browser.close()

"""##Exécution du script"""

loop = asyncio.get_event_loop()
task = loop.create_task(run())
loop.run_until_complete(task)

"""##Affichage aprecu de la page final"""

from IPython.display import display, HTML, Image

final_url = "https://widget.thefork.com/fr/3fe2da31-4669-432b-8616-e0e81953d4a6?utm_source=foodaffairs.fr"

print(f"Page finale URL: {final_url}")
display(HTML(f'<a href="{final_url}" target="_blank">Ouvrir la page finale dans un nouvel onglet</a>'))

# Affichage iframe (peut ne pas marcher si le site bloque l’iframe)
display(HTML(f"""
<iframe src="{final_url}" width="900" height="600" style="border:1px solid #ccc;"></iframe>
"""))

# Afficher la capture d'écran si dispo
if screenshot:
    display(Image(data=screenshot))
