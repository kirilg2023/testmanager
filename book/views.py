from django.shortcuts import render

a_ua = 'Ласкаво просимо в Трагедії'
b_ua = 'Ласкаво просимо в Пригоди'
c_ua = 'Ласкаво просимо в Поезію'
d_ua = 'Ласкаво просимо в Жахи'

a_en = 'Welcome to Tragedy'
b_en = 'Welcome to Adventures'
c_en = 'Welcome to Poetry'
d_en = 'Welcome to Horror'

中国={#Китай
    'ua_l': {

        'title': {
            'a': a_ua,
            'b': b_ua,
            'c': c_ua,
            'd': d_ua,
        },
        'name_book': {

            'uno': 'Марс Хоробрий',
            'dos': "'UniveRsIPy': Шлях Джона",
            'tres': 'Любіть Україну',
            'cuatro': 'Я бачу, вас цікавить пітьма',
            'description': {

                'uno': 'Слідкуйте за подорожжю Марса, вірного собаки, у вигаданій історії, створеній за допомогою штучного інтелекту (ChatGPT).',
                'dos': 'Це історія про місце під назвою UniveRsIPy. Цю історію вигадано штучним інтелектом (ChatGPT).',
                'tres': 'Поетичне звернення до любові до рідної землі, свободи, гідності й духовної краси України.',
                'cuatro': 'Психологічний трилер про журналіста, що розслідує моторошні зникнення в провінційному містечку, де темрява ховає більше, ніж здається.',
                'pdf': {
                    'uno': 'main/pdf_file/storyofmars_ua.pdf',
                    'dos': 'main/pdf_file/kaka.pdf',
                    'tres': 'main/pdf_file/poetry_ua.pdf',
                    'cuatro': 'main/pdf_file/59120.pdf',
                    'read': {
                        'lol': 'Читати',
                        'img': {
                            'uno': 'main/img/uno.png',
                            'dos': 'main/img/university.png',
                            'tres': 'main/img/poetry_ua.png',
                            'cuatro': 'main/img/293.jpg',
                        },
                    },
                },
            },
        },
    },

    'en_l': {
        'title': {
            'a': a_en,
            'b': b_en,
            'c': c_en,
            'd': d_en,
        },
        'name_book': {

            'uno': 'Mars The Brave',
            'dos': "'UniveRsIPy': John's Path",
            'tres': 'The Sun and Her Flowers',
            'cuatro': 'The Ruin Of Souls Lily Wildhart',
            'description': {

                'uno': 'Follow the journey of Mars, a loyal dog in a fictional tale crafted with the help of AI (ChatGPT)',
                'dos': 'This is a story about a place called UniveRsIPy. This story is made up by AI (ChatGPT).',
                'tres': 'The Sun and Her Flowers is a poetry collection about growth, heartbreak, healing, and self-love.',
                'cuatro': 'Dark fantasy with elements of horror about a girl who fights against evil and supernatural forces to save herself and her loved ones.',
                'pdf': {
                    'uno': 'main/pdf_file/storyofmars_en.pdf',
                    'dos': 'main/pdf_file/ksks.pdf',
                    'tres': 'main/pdf_file/poetry_en.pdf',
                    'cuatro': 'main/pdf_file/horror_en.pdf',
                    'read': {
                        'lol':'Read',
                        'img': {
                            'uno': 'main/img/uno.png',
                            'dos': 'main/img/university.png',
                            'tres': 'main/img/pop.png',
                            'cuatro': 'main/img/lol.jpg',
                        }
                    }
                }
            }
        }
    }
} #словник у словнику у словнику у словнику у словнику у словнику у словнику （7 словників）



def view_book(request, language, genre):
    if language == 'en':
        enn = {'t':中国['en_l']}
        if genre == 'tragedy':
            return render(request, 'books/en/tragedy.html', enn['t'])
        elif genre == 'adventure':
            return render(request, 'books/en/adventure.html', enn['t'])
        elif genre == 'poetry':
            return render(request, 'books/en/poetry.html', enn['t'])
        elif genre == 'horror':
            return render(request, 'books/en/horror.html', enn['t'])
        else:
            return render(request, 'books/error.html')

    if language == 'ua':
        uaa = {'t':中国['ua_l']}
        if genre == 'tragedy':
            return render(request, 'books/ua/tragedy.html', uaa['t'])
        elif genre == 'adventure':
            return render(request, 'books/ua/adventure.html', uaa['t'])
        elif genre == 'poetry':
            return render(request, 'books/ua/poetry.html', uaa['t'])
        elif genre == 'horror':
            return render(request, 'books/ua/horror.html', uaa['t'])
        else:
            return render(request, 'books/error.html')

    else:
        return render(request, 'books/error.html')


