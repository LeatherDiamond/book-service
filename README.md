# Navigation
 
* ***[Project description](#project-description)***
* ***[Detailed functionality description](#detailed-functionality-description)***
  * ***[Book instance](#1-book-instance)***
  * ***[Author instance](#2-author-instance)***
  * ***[Product Search](#3-product-search)***
  * ***[Built-in administrative portal](#4-built-in-administrative-portal)***
  * ***[Home page](#5-home-page)***
  * ***[Directory](#6-directory)***
* ***[How to start?](#how-to-start)***
  * ***[Note](#note)***
* ***[License](#license)***


# Project description

This project is a compact web service that enables users to manage authors and books. 
With its intuitive interface, users can easily add, remove, and modify authors and books on-the-go. 
Users can quickly search for titles by entering relevant keywords. 
The service is highly flexible, allowing users to customize it to their specific requirements.  
Furthermore, this  project is equipped with a continuous integration pipeline that automatically builds the project image and launches tests every time new code is pushed to the Github repository.
This ensures the codebase remains error-free and runs smoothly, without any glitches or bugs.
The project also has in-built tets that help catch bugs early on. 
These tests are written using standard libraries and are easy to run, debug and maintain. 
This project allows uers to focus on developing new features and enhancing their book collection management experience.

***Applied technologies:*** 
- Python(>=3.9.7), 
- SQLite, 
- Django(>=4.1.7), 
- Bootstrap (>=5.0.2), 
- Docker (docker engine >=20.10.23 ), 
- GitHub Actions (checkout >=v2)

# Detailed functionality description
   
## 1. Book instance

   * ***1.1*** *Fields:*
       * ***1.1.1*** *Book title*
       * ***1.1.2*** *Photo*
       * ***1.1.3*** *Author of the book (may contain several authors) - directory*
       * ***1.1.4*** *Year of publication*
       * ***1.1.5*** *Pages*
       * ***1.1.6*** *Binding*
       * ***1.1.7*** *Format*
       * ***1.1.8*** *ISBN*
       * ***1.1.9*** *Weight (grams)*
       * ***1.1.10*** *Age restriction*
       * ***1.1.11*** *Date of addition to the database*
       * ***1.1.12*** *Date when the book was modified last time*
       
## 2. Author instance

  * ***2.1*** *Fields:*
      * ***2.1.1*** *Author's name*
      * ***2.1.2*** *Author's surname*
      * ***2.1.3*** *Description*
      * ***2.1.4*** *Related books*

## 3. Product Search

  * ***3.1*** *Search by keyword in the author's name/surname and book title*

## 4. Built-in administrative portal

   * ***4.1*** *Accessible at /admin/;*
   * ***4.2*** *Used by Administrator as a low-level interface to all web-site data;*
   
## 5. Home page

   * ***5.1*** *Navigation through the website sections (Lists, Create, Update, Delete books and authors)*
   * ***5.2*** *Books and authors search*
   * ***5.3*** *Books showcase*

## 6. Directory

   * ***6.1*** *Elements of the directoriy are used as standard values to be substituted into the forms fields*
   * ***6.2*** *Implemented a separate module for directory*
   * ***6.3*** *Elements of the directory can be edited by user*
   * ***6.4*** *Directory stores in a separate table in the database of directories module;*


# How to start?

**1. Clone current repository on your local machine:**
```
git clone https://github.com/LeatherDiamond/book_service.git
```

**2. Create and activate virtual environment on your machine:**
```

python -m venv environment_name
.\env\Scripts\activate
```

**3. Install all requirements from "requirements.txt".**
```
pip install -r requirements.txt
```

**4. Provide mandatory data in the following file:**
 - [x] settings.py:
   ***Django SECRET_KEY;***
    
    > ###### NOTE: 
    >
    > To launch the project correct without any import errors *SECRET KEY* can be provided in two ways:
    >  * ***1. You can create ".env" file at "proj" directory and put the key in standart format here. No more changes are required.***
    >  ```
    >  SECRET_KEY='your_secret_key'
    >  ```
    >  * ***2. The key can be provided in "settings.py" file directly in field "SECRET_KEY" but unused imports should be removed:***
    >
    >
    >~~***import*** os~~
    >
    >~~***from*** dotenv ***import*** load_dotenv~~
    >
    >~~load_dotenv()~~
    

**5. Apply all migrations:**
```
python manage.py migrate
```

**6. Create a superuser to have access to the admin panel.**
```
python manage.py createsuperuser
```

**7. Launch the project on a development server to see all the functionality.**
```
python manage.py runserver
```

**8 *. To run in-built tests use the following command ***(tests are located in module "product_card" in "tests.py" file)***:**
```
python manage.py test
```



# License

***This project is licensed under the MIT License - see the [LICENSE](https://github.com/LeatherDiamond/book_service/blob/master/LICENCE) file for details.***
