from Main.DB.DatabaseHandler import *


class DatabaseMerger:
    @staticmethod
    def merge_databases(db1_path, db2_path, results_path):
        """
        This function merges the two databases from the given paths, into a new database in
        the given results path.
        """
        db1 = DatabaseHandler(db1_path)
        db2 = DatabaseHandler(db2_path)
        new_db = DatabaseHandler(results_path)

        updated_run_ids = DatabaseMerger.order_run_ids(db1, db2)
        DatabaseMerger.merge_tables(db1, db2, new_db, updated_run_ids)


    @staticmethod
    def order_run_ids(db1, db2):
        """
        This function matches a new run_id to every run in db1 and db2, based on the time the run occurred,
        ordered from the first run to the last
        """
        order_run_ids_lst = []
        for run in db1.get_all_runids():
            order_run_ids_lst.append([1] + list(run))
        for run in db2.get_all_runids():
            order_run_ids_lst.append([2] + list(run))

        order_run_ids_lst.sort(key=lambda x: x[2])

        order_run_ids_dict = dict()
        for i in range(len(order_run_ids_lst)):
            run = order_run_ids_lst[i]
            order_run_ids_dict[tuple(run[:2])] = tuple([i+1])

        return order_run_ids_dict

    @staticmethod
    def merge_tables(db1, db2, new_db, updated_run_ids):
        """
        This function goes over all the coderage database tables, and inserts the merged data to the
        new database.
        """
        all_tables = {"tests_details": new_db.insert_tests_details,
                      "run_summary": new_db.insert_run_summary,
                      "coverage": new_db.insert_coverage,
                      "coverage_summary": new_db.insert_coverage_summary,
                      "functions_details": new_db.insert_functions_details}

        for table in all_tables:
            db1_data = db1.get_all_data(table)
            db2_data = db2.get_all_data(table)

            merged_data = []

            for run_data in db1_data:
                merged_data.append(updated_run_ids[(1, run_data[0])] + run_data[1:])

            for run_data in db2_data:
                merged_data.append(updated_run_ids[(2, run_data[0])] + run_data[1:])

            all_tables[table](merged_data)


