import pytest
from playwright.sync_api import Page


# Test 1: Ověření, že stránka obsahuje text "Email"
def test_stranka_obsahuje_text_email(page: Page):
    page.goto("https://www.seznam.cz")
    assert "Email" in page.content()

# Test 2: Ověření, že tlačítko „Přihlásit se“ je viditelné
def test_tlacitko_prihlasit_visible(page: Page):
    page.goto("https://www.seznam.cz")
    tlacitko_prihlasit = page.locator("text=Přihlásit se")
    assert tlacitko_prihlasit.is_visible()

# Test 3: Ověří, že existuje vyhledávací políčko
def test_policko_vyhledavani_exists(page: Page):
    page.goto("https://www.seznam.cz")
    policko_vyhledavani = page.locator("input[name='q']")
    assert policko_vyhledavani.is_visible()