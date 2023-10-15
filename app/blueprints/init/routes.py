from flask import url_for, redirect, Blueprint
from datetime import datetime, timedelta
from ...models import User, Book, Contact, Rent
from app import db

bp = Blueprint('main', __name__)

#inicjacja bazy

@bp.route('/init')
def init():
    db.create_all()
    booksCount = Book.query.count()
    userCount = User.query.count()
    contactCount = Contact.query.count()
    
    if userCount <=0:
        #password_hashed = generate_password_hash("123", 'sha256')
        user1 = User(id=1, username="Admin", email="admin@wseiz.edu.pl", password="123", photo_url="../static/photo_user.png") 
        db.session.add(user1)
        db.session.commit()
        
        user2 = User(id=2, username="Michal", email="m@wseiz.edu.pl", password="qwe", photo_url="../static/photo_user.png") 
        db.session.add(user2)
        db.session.commit()
        
    if contactCount <=0:
        contact1 = Contact(id=1, name="Kamil Zawada", email="k.zawada@wseiz.edu.pl", phone="666504034", photo_url="../static/AA.png", user_id="1", status=False, note="Ma fajną kolekcję komiksów") 
        db.session.add(contact1)
        db.session.commit()
        
        contact2 = Contact(id=2, name="Anna Figiel", email="a.figiel@wp.pl", phone="55530298", photo_url="../static/AF.png", user_id="1", status=False, note="Nie pożyczaj!") 
        db.session.add(contact2)
        db.session.commit()
        
        contact3 = Contact(id=3, name="Jakub Wronkowski", email="j.wronkowski@wseiz.edu.pl", phone="666504034", photo_url="../static/JW.png", user_id="1", status=False, note=":)") 
        db.session.add(contact3)
        db.session.commit()
        
        contact4 = Contact(id=4, name="Kinga Prasa", email="k.prasa@wseiz.edu.pl", phone="606458925", photo_url="../static/KP.png", user_id="1", status=False, note=":)") 
        db.session.add(contact4)
        db.session.commit()
        
        contact5 = Contact(id=5, name="Karolina Bednarek", email="kbednarek12@o2.pl", phone="999349023", photo_url="../static/KB.png", user_id="2", status=False, note=":)")
        db.session.add(contact5)
        db.session.commit()
        
        contact6 = Contact(id=6, name="John Desner", email="jd56@durs.eu", phone="234343478", photo_url="../static/JH.png", user_id="2", status=False, note=":)") 
        db.session.add(contact6)
        db.session.commit()
        
        contact6 = Contact(id=7, name="Olga Lenko", email="olenko@erandis.eu", phone=" 863245612", photo_url="../static/OL_DE.jpg", user_id="2", status=True, note=":)") 
        db.session.add(contact6)
        db.session.commit()
    
    if booksCount <=0: 
        book1 = Book(id=1, title='The Sultin Man', author='Brandon Sanderson', series='Cosmare',  pages='234', publisher='Fabryka Słów', publishDate='11-01-2023', volume='1', description="New York Times bestselling author Brandon Sanderson shows us a future in the Cosmere universe where a perpetual planetary wanderer must decide whether to keep running, or stay and make a difference on a struggling planet.", rate='5', status=True, cover_url='../static/BS_SM.png', cover='Hard', user_id="1", note="Dobra książka")
        db.session.add(book1)
        db.session.commit()
    
        book2 = Book(id=2, title='Yumi i Malarz Koszmarów', author='Brandon Sanderson', series='Cosmare',  pages='432', publisher='Mag', publishDate='26-07-2023', volume='1', description="Samodzielna opowieść z uniwersum Cosmere, w której dwoje ludzi pochodzących z zupełnie różnych światów musi się porozumieć i współpracować, żeby ocalić swoje społeczności przed zagładą.", rate='5', status=False, cover_url='../static/BS_YMK.png', cover='Hard', user_id="1", note="Dobra książka")
        db.session.add(book2)
        db.session.commit()
    
        book3 = Book(id=3, title='Rytmy Wojny 1', author='Brandon Sanderson', series='Archiwum Burzowego Światła (tom 4.1)',  pages='656', publisher='Mag', publishDate='24-03-2021', volume='4.1', description="Po utworzeniu koalicji ludzkich monarchów stawiających opór wrogiej inwazji, Dalinar Kholin i jego Świetliści Rycerze przez rok prowadzili przeciągającą się, brutalną wojnę. Żadna ze stron nie zyskała przewagi, a nad każdym strategicznym posunięciem wisi cień zdrady przebiegłego Taravangiana.", rate='5', status=False, cover_url='../static/BS_RM1.png', cover='Twarda', user_id="1", note="Dobra książka")
        db.session.add(book3)
        db.session.commit()
        
        book4 = Book(id=4, title='Rytmy Wojny 2', author='Brandon Sanderson', series='Archiwum Burzowego Światła (tom 4.2)',  pages='720', publisher='Mag', publishDate='30-06-2021', volume='4.2', description="W opanowanym przez pieśniarzy i Stopionych Urithiru Kaladin i Navani walczą o ocalenie Rodzeństwa, sprena wieży, przed całkowitym zepsuciem. Upadek wieży, stanowiącej główny punkt przerzutowy dla wojsk koalicji monarchów, oznaczałby katastrofę i ostateczne zwycięstwo sił Odium. Aby osiągnąć swój cel, Navani decyduje się na niebezpieczną grę z Raboniel, Stopioną zwaną niegdyś nie bez powodu Panią Bólu.", rate='5', status=False, cover_url='../static/BS_RM2.png', cover='Miękka', user_id="1", note="Dobra książka")
        db.session.add(book4)
        db.session.commit()
        
        book5 = Book(id=5, title='Strażnik', author='Paulina Hendel', series='Zapomniana księga',  pages='368', publisher='We need YA', publishDate='27-02-2019', volume='1', description="Hubert budzi się w ciemnym i zamkniętym pokoju, ubrany w starą koszulę i poprzecierane dżinsy. Zamiast w Paryżu, znajduje się teraz sto kilometrów od morza… w Polsce. Dodatkowo, jest ranny i wygląda zupełnie inaczej niż powinien. Okazuje się, że od feralnego wyjazdu do Francji minęło siedem lat, a on nie jest już zwykłym nastolatkiem. W tym czasie świat bardzo się zmienił…", rate='5', status=True, cover_url='../static/PH_ST.jpg', cover='Miękka', user_id="1", note="Dobra książka")
        db.session.add(book5)
        db.session.commit()
        
        book6 = Book(id=6, title='Tropiciel', author='Paulina Hendel', series='Zapomniana księga',  pages='576', publisher='We need YA', publishDate='04-03-2019', volume='2', description="Hubert budzi się w Paryżu w ciele siedemnastolatka, a po tragicznym początku końca świata nie ma żadnego śladu. Gdy Luwr ponownie staje w ogniu, Hubert już wie, co ma zrobić. Wyznacza sobie jeden cel: musi zdobyć księgę, która pomoże mu w walce z demonami. Jednak bieg wydarzeń jest nieco inny, niż się spodziewał. Impuls elektromagnetyczny niszczy wszystkie urządzenia, tajemnicza choroba zaczyna zabierać coraz więcej ludzi.", rate='5', status=False, cover_url='../static/PH_T.jpg', cover='Miękka', user_id="1", note="Dobra książka")
        db.session.add(book6)
        db.session.commit()
        
        book7 = Book(id=7, title='Design thinking. Methodology Book', author='Emrah Yayici', series='',  pages='116', publisher='ArtBizTech', publishDate='01-01-2016', volume='1', description="This book explains design thinking methodology that is applied by high-performing enterprises, start-ups and organizations in developing innovative products, technologies, services, business models etc. It includes easily applicable design thinking techniques and how explains how artful thinking perspectives can be applied to enhance design thinking skills.", rate='3', status=False, cover_url='../static/DT_MB.jpg', cover='Miękka', user_id="2", note="Dobra książka")
        db.session.add(book7)
        db.session.commit()
        
        book8 = Book(id=8, title='Flask. Tworzenie aplikacji internetowych w Pythonie.', author='Miguel Grinberg', series='',  pages='264', publisher='Helion', publishDate='10-03-2020', volume='1', description="Frameworki bardzo ułatwiają życie programistom. Pozwalają na szybkie tworzenie nawet rozbudowanych aplikacji, ale praca z frameworkiem najczęściej oznacza duże ograniczenia w doborze technologii.", rate='5', status=False, cover_url='../static/F.jpg', cover='Miękka', user_id="2", note="Dobra książka")
        db.session.add(book8)
        db.session.commit()
        
        book9 = Book(id=9, title='Projektowanie interfejsów. Sprawdzone wzorce projektowe', author='Jenifer Tidwell', series='',  pages='352', publisher='Helion', publishDate='12-01-2005', volume='1', description="Najważniejsze jest pierwsze wrażenie! Mimo istnienia ogromnej ilości narzędzi do tworzenia interfejsów użytkownika projektowanie dobrych interfejsów aplikacji wciąż nie jest łatwe. Ta bestsellerowa książka jest jednym z niewielu wiarygodnych źródeł, które pomogą Ci przejść przez istny labirynt wariantów projektowych. ", rate='5', status=False, cover_url='../static/PI.jpg', cover='Miękka', user_id="2", note="Dobra książka")
        db.session.add(book9)
        db.session.commit()
        
        book10 = Book(id=10, title='Designing and Prototyping Interfaces with Figma', author='Fabio Staiano', series='',  pages='720', publisher='Packt Publishing', publishDate='16-03-2022', volume='1', description="Discover user experience and user interface design best practices while mastering a wide array of tools across Figma and FigJam with this full-color guide.", rate='5', status=True, cover_url='../static/DPI_F.jpg', cover='Miękka', user_id="2", note="Dobra")
        db.session.add(book10)
        db.session.commit()
        
        book11 = Book(id=11, title='UXUI. Design Zoptymalizowany. Manual Book ', author='Chris Badura', series='Informatyka - Poradnik',  pages='344', publisher='Helion', publishDate='24-09-2019', volume='1', description="Czy wiesz, że projektowanie skutecznych produktów cyfrowych, takich jak aplikacje, strony czy systemy, to znacznie więcej niż nadanie im ładnego wyglądu? O ich sukcesie przesądza równowaga między użytecznością, zaspokajaniem potrzeb użytkownika a szatą graficzną. Jeśli chcesz się dowiedzieć, jak prawidłowo definiować funkcje takich produktów, jak dobrze je zaprojektować i prowadzić badania jakościowe z użytkownikami.", rate='3', status=True, cover_url='../static/UX_UI.png', cover='Hardcover', user_id="2", note="Polecam")
        db.session.add(book11)
        db.session.commit()
        
        book12 = Book(id=12, title='Zgroza w Dunwich', author='H.P. Lovecraft', series='Lovecraft w ilustracjach Barangera',  pages='68', publisher='Vesper', publishDate='11-09-2023', volume='1', description="W odizolowanym od społeczności gospodarstwie prostoduszna albinoska Lavinia Whateley rodzi dziecko, Wilbura. Nikt nie wie, kim jest jego ojciec. Stary Whateley, ojciec Lavinii, wychowuje Wilbura, który budzi niepokój okolicznych mieszkańców, przerażonych szybkim wzrostem dziecka i jego odrażającym wyglądem. Od zawsze krążyły pogłoski o konszachtach Whateleya z magią, a po jego śmierci dorosły już Wilbur wydaje się być zdeterminowany, aby poszerzyć zakazaną wiedzę, którą odziedziczył po dziadku. W tym celu udaje się na Uniwersytet Miskatonic w Arkham, aby wypożyczyć znajdujący się w zasobach bibliotecznych instytucji egzemplarz złowieszczego „Necronomiconu”. Po odkryciu złowrogich zamiarów swojego gościa profesor Armitage odmawia spełnienia jego prośby. Wilbur jest jednak zdecydowany zdobyć księgę za wszelką cenę.", rate='5', status=False, cover_url='../static/HL_ZD.png', cover='Hardcover', user_id="1", note="strona 123!")
        db.session.add(book12)
        db.session.commit()
               
        rent1 = Rent(id=1, borrow_date=datetime.today(), return_date=datetime.today()+timedelta(days=30), book_id=10, contact_id=7, user_id=2 )
        db.session.add(rent1)
        db.session.commit()  
        
        rent2 = Rent(id=2, borrow_date=datetime.today(), return_date=datetime.today()+timedelta(days=30), book_id=1, contact_id=1, user_id=1 )
        db.session.add(rent2)
        db.session.commit() 
        
        rent3 = Rent(id=3, borrow_date=datetime.today(), return_date=datetime.today()+timedelta(days=30), book_id=5, contact_id=2, user_id=1 )
        db.session.add(rent3)
        db.session.commit() 
              
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))