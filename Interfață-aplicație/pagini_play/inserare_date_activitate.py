from conectare_bd import conectare


def refresh_tabel_date(cnp_copil, tabel_date):
    connection = conectare()
    cursor = connection.cursor()
    try:
        query1 = "SELECT nume_activitate, data_inceput, data_sfarsit FROM activitate WHERE id_pacient_fk = %s"
        cursor.execute(query1, (cnp_copil,))
        date_copil = cursor.fetchall()

        for row in tabel_date.get_children():
            tabel_date.delete(row)

        for index, row in enumerate(date_copil, start=1):
            tabel_date.insert("", "end", values=(index,) + row)

    except Exception as e:
        print(f"Eroare la interogare: {e}")
    finally:
        cursor.close()


def insert_date(nume_activitate,data_start,data_stop,cnp_copil, tabel_date):
    connection = conectare()
    cursor = connection.cursor()
    try:
        query = "INSERT INTO activitate (nume_activitate, data_inceput, data_sfarsit, id_pacient_fk) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nume_activitate, data_start, data_stop, cnp_copil))
        connection.commit()
        print("Date inserate cu succes")
    except Exception as e:
        print(f"Eroare la interogare: {e}")
    finally:
        cursor.close()

    refresh_tabel_date(cnp_copil, tabel_date)