from database.DB_connect import DBConnect
from model.team import Team


class DAO:
    @staticmethod
    def get_all_years():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT t.year 
                    FROM team t
                    WHERE t.year >= 1980 """

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_teams_by_year(year):
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT t.id, t.team_code, t.name, SUM(s.salary) AS tot_salary
                    FROM team t, salary s
                    WHERE t.id = s.team_id
                    AND t.year = %s
                    GROUP BY t.id, t.team_code, t.name
                    """

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Team(**row))

        cursor.close()
        conn.close()
        return result

