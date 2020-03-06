import time
import requests
import urllib
import os
import mysql.connector
from mysql.connector import errorcode
from bs4 import BeautifulSoup
from bs4 import element
from threading import Thread

# --- CONSTANTS ---

TABLE_create_query = """CREATE TABLE IF NOT EXISTS `categories` (
     `obj_no` MEDIUMINT(5) UNSIGNED NOT NULL,
     `name` varchar(32) NOT NULL,
     `sub_category` varchar(120) NOT NULL,
     `description` varchar(120) NOT NULL,
     KEY `categories_obj_no_idx` (`obj_no`) USING BTREE
     ) CHARSET=utf8 ENGINE=Aria"""

# --- VARIABLES ---

buffer = []
tot_proc = 0

# --- UTILITY FUNCTIONS ---

def create_database(cursor):
    try:
        cursor.execute(
            f"CREATE DATABASE {dbname} DEFAULT CHARACTER SET 'utf8'")
    except mysql.connector.Error as err:
        print(f'Failed creating database: {err}')
        os._exit(1)

def process_file(url, name, sub_cat, description):
    global buffer, tot_proc
    # load txt file
    _file = urllib.request.urlopen(url)
    i = 0
    # TODO: Update this to use TLE class
    for _line in _file.readlines():
        # read every 3rd line
        i += 1
        line = str(_line)[2:-3]
        if i == 3:
            entry = line.split(' ')
            obj_id = entry[1]
            # populate data in memory first and batch process after
            data = (obj_id, name[:-4], sub_cat.strip(), description.strip())
            buffer.append(data)
            i = 0
    tot_proc += 1


# --- INIT ---

def main():
    CONFIG = os.path.abspath("../../trusat-config.yaml")

    # connect to server

    try:
        db = database.Database(CONFIG)
        cursor = db.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your user name or password')
        else:
            print(err)
        print('Script is shutting down.')
        os._exit(1)

    # load DB and initialize table
    try:
        cursor.execute(f'USE {dbname}')
    except mysql.connector.Error as err:
        print(f'Database {dbname} does not exist.')
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print(f'Database {dbname} created successfully.')
            cnx.database = dbname
        else:
            print(err)
            os._exit(1)
    cursor.execute(TABLE_create_query)

    # scrape main page
    URL = 'https://celestrak.com/NORAD/elements/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    tables = soup.find_all('table', class_='striped')

    tot_files = 0

    for idx, table in enumerate(tables):
        # get main category, but
        # don't change the main_cat for the 4th table
        # since it is a continuation of the 3rd table
        header = table.find('thead')
        if idx == 3:
            pass
        else:
            main_cat = header.next.next.next
            
        links = table.find("tbody").find_all(recursive=False)

        for link in links:
            _tmp_link = link.next.next
            if type(_tmp_link) != element.Tag:
                continue
            if 'href' in _tmp_link.attrs:
                name = _tmp_link['href']
                if name[-4:] == '.txt':
                    # start processing file in new thread
                    sub_cat = _tmp_link.get_text()
                    _url = URL + name
                    Thread(target=process_file, args=(_url, name, sub_cat, main_cat)).start()
                    tot_files += 1

    # Skip the supplemental for now
    if (False):
        # scrape supplemental page
        URL_SUP = 'https://celestrak.com/NORAD/elements/supplemental/'
        page = requests.get(URL_SUP)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table', class_='center outline')

        # get main category
        header = table.find('tr', class_='header')
        main_cat = header.next.next.next
        # find all links within main category
        links = header.find_next_siblings()
        for link in links:
            _tmp_link = link.next.next.next
            name = _tmp_link['href']
            if name[-4:] == '.txt':
                # start processing file in new thread
                _url = URL_SUP + name
                Thread(target=process_file, args=(_url, name, sub_cat, main_cat)).start()
                tot_files += 1

    # wait for all threads to finish while displaying progress
    while True:
        if tot_proc == tot_files: break
        print(f'Processed {tot_proc}/{tot_files} files', end='\r')
        time.sleep(0.25)

    print(f'{tot_proc} categories loaded successfully, with {len(buffer)} '
            'entries in total.\nSaving to database...', end='')
    
    # clear current records
    clear_table = ("TRUNCATE TABLE categories")
    cursor.execute(clear_table)

    # save to DB
    add_entry_query = """INSERT INTO categories 
                (obj_no, name, sub_category, description) 
                VALUES (%s, %s, %s, %s)"""

    i = 0
    entry_list = []
    for _x in buffer:
        if (i<1000):
            entry_list.append(_x)
            i+=1
        else:
            cursor.executemany(add_entry_query, entry_list)
            entry_list = []
            i = 0
    # Commit the remaining batch < 1000
    if (len(entry_list) > 0):
        cursor.executemany(add_entry_query, entry_list)
    cnx.commit()
    print('done')

    cursor.close()
    cnx.close()
    print('All satellites successfully saved to database!')

if __name__ == '__main__':
    main()
