#!/usr/bin/python3

def display(conn, login):
    cur = conn.cursor()

    query_etudiant = "SELECT prenom, nom FROM etudiant WHERE login = %s;"
    cur.execute(query_etudiant, (login,))
    etudiant = cur.fetchone()

    if etudiant is None:
        print("Étudiant inconnu")
        cur.close()
        return

    prenom, nom = etudiant
    print(f"Notes de l'étudiant {prenom} {nom} ({login})")

    query_notes = """
        SELECT d.description, d.daterendu, n.valeur
        FROM note n
        JOIN devoir d ON n.devoir = d.num
        WHERE n.etudiant = %s
        ORDER BY d.daterendu ASC;
    """
    cur.execute(query_notes, (login,))
    notes = cur.fetchall()

    if not notes:
        print("  (Aucune note enregistrée pour cet étudiant)")
        cur.close()
        return

    total_notes = 0
    for description, daterendu, valeur in notes:
        print(f"- {description} [{daterendu}] : {valeur}")
        total_notes += valeur

    moyenne = total_notes / len(notes)
    print(f"* Moyenne : {moyenne:.1f}")

    cur.close()