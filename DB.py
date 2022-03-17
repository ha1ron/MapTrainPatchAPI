import sqlite3


class SQLMaker:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_edges_train(self, month, poezd):
        with self.connection:
            return self.cursor.execute("""SELECT distinct a."/BIC/STBEGIN",
                                                          b.NAME,
                                                          b.LAT,
                                                          b.LON,
                                                          a."/BIC/STBEGOUT",
                                                          c.NAME,
                                                          C.LAT,
                                                          c.LON,
                                                          a.STAGENUM
                                          FROM [/BIC/AZGO_PWAY2] a
                                          LEFT OUTER JOIN "/BIC/AZGO_GEO2" b
                                          on a."/BIC/STBEGIN" = b."/BIC/STBEG"
                                          LEFT OUTER JOIN "/BIC/AZGO_GEO2" c
                                          on a."/BIC/STBEGOUT" = c."/BIC/STBEG"
                                          where a."/BIC/MONTHGO" = ? and 
                                                a."/BIC/GO_POEZD" = ?
                                          order by a.STAGENUM;""", (month, poezd)).fetchall()

    def get_InvestigationSFSet(self, month, poezd):
        with self.connection:
            return self.cursor.execute("""SELECT distinct a."/BIC/GO_POEZD",
                                                          a."/BIC/MONTHGO",
                                                          a."RECORDMODE",
                                                          b.lat, b.lon, 
                                                          a."/BIC/ZGO_PBEG",
                                                          b.name, c.lat,
                                                          c.lon, a."/BIC/ZGO_PEND",
                                                          c.name       
                                          FROM [/BIC/AZGO_PWAY2] a
                                          LEFT OUTER JOIN "/BIC/AZGO_GEO2" b
                                          on a."/BIC/ZGO_PBEG" = b."/BIC/STBEG"
                                          LEFT OUTER JOIN "/BIC/AZGO_GEO2" c
                                          on a."/BIC/ZGO_PEND" = c."/BIC/STBEG"
                                          where a."/BIC/MONTHGO" = ? and 
                                                a."/BIC/GO_POEZD" = ?
                                          order by a.STAGENUM;""", (month, poezd)).fetchall()

    def get_StNumberingSet(self, month, poezd):
        with self.connection:
            return self.cursor.execute("""SELECT distinct a."/BIC/GO_POEZD",
                                                          a."/BIC/MONTHGO",
                                                          b.NAME, c.NAME,
                                                          a.STAGENUM, a."/BIC/ZUUCASAR", a."/BIC/PR_CHET"
                                          FROM [/BIC/AZGO_PWAY2] a
                                          LEFT OUTER JOIN "/BIC/AZGO_GEO2" b
                                          on a."/BIC/STBEGIN" = b."/BIC/STBEG"
                                          LEFT OUTER JOIN "/BIC/AZGO_GEO2" c
                                          on a."/BIC/STBEGOUT" = c."/BIC/STBEG"
                                          where a."/BIC/MONTHGO" = ? and
                                          a."/BIC/GO_POEZD" = ?
                                          order by a.STAGENUM;""", (month, poezd)).fetchall()


