XPATH_LOCATORS = {
    "main_title": "//h1[text()='Do more!']",
    "sign_up_button": "//button[text()='Sign up']",
    "logo_link": "//a[@class='header_logo']",
    "contacts_title": "//h2[text()='Contacts']",
    "home_link": "//a[text()='Home']",

    "instructions_image": "//img[@alt='Instructions']",
    "guest_login_button": "//button[text()='Guest log in']",
    "instagram_icon": "//a[contains(@href, 'instagram.com')]/span[contains(@class, 'icon-instagram')]",
    "main_description": "//p[contains(text(), 'With the help of the Hillel auto project')]",
    "about_button": "//button[text()='About']",

    "hillel_website_link": "//a[text()='ithillel.ua']",
    "facebook_icon": "//a[contains(@href, 'facebook.com')]/span[contains(@class, 'icon-facebook')]",
    "log_fuel_expenses_title": "//p[text()='Log fuel expenses']",
    "logo_svg": "//a[@class='header_logo']/*[name()='svg']",
    "contacts_button": "//button[text()='Contacts']",

    "youtube_icon": "//a[contains(@href, 'youtube.com')]/span[contains(@class, 'icon-youtube')]",
    "instructions_title": "//p[text()='Instructions and manuals']",
    "support_email_link": "//a[contains(@href, 'mailto:developer@ithillel.ua')]",
    "sign_in_button": "//button[text()='Sign In']",
    "fuel_expenses_description": "//p[contains(text(), 'Keep track of your')]",

    "telegram_icon": "//a[contains(@href, 't.me')]/span[contains(@class, 'icon-telegram')]",
    "copyright_text": "//p[contains(text(), '2021 Hillel IT school')]",
    "linkedin_icon": "//a[contains(@href, 'linkedin.com')]/span[contains(@class, 'icon-linkedin')]",
    "instructions_description": "//p[contains(text(), 'Watch over 100 instructions')]",
    "footer_description": "//p[contains(text(), 'Hillel auto developed')]"
}


CSS_LOCATORS = {
    "contacts_title": "#contactsSection h2",
    "logo_link": "a.header_logo",
    "sign_in_button": "button.header_signin",
    "instagram_icon": "a[href*='instagram.com'] span[class*='icon-instagram']",
    "main_title": "h1.hero-descriptor_title",

    "contacts_button": "button[appscrollto='contactsSection']",
    "instructions_image": "img[alt='Instructions']",
    "facebook_icon": "a[href*='facebook.com'] span[class*='icon-facebook']",
    "home_link": "a.header-link[href='/']",
    "fuel_expenses_description": "p.about-block_descr",

    "linkedin_icon": "a[href*='linkedin.com'] span[class*='icon-linkedin']",
    "sign_up_button": "button.hero-descriptor_btn",
    "hillel_website_link": "a[href='https://ithillel.ua']",
    "main_description": "p.hero-descriptor_descr",
    "telegram_icon": "a[href*='t.me'] span[class*='icon-telegram']",

    "copyright_text": ".footer_item-left p",
    "about_button": "button[appscrollto='aboutSection']",
    "logo_svg": "a.header_logo svg",
    "instructions_title": "p.about-block_title.h2",
    "guest_login_button": "button.header-link.-guest",

    "youtube_icon": "a[href*='youtube.com'] span[class*='icon-youtube']",
    "support_email_link": "a[href='mailto:developer@ithillel.ua']",
    "log_fuel_expenses_title": "p.about-block_title",
    "footer_description": ".footer_item-right",
    "instructions_description": "p.about-block_descr.lead"
}