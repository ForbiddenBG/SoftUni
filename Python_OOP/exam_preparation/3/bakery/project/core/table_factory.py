from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class TableFactory:

    valid_types = {"InsideTable": InsideTable , "OutsideTable": OutsideTable}

    @staticmethod
    def create_a_table_instance(table_number, capacity, table_type):
        return TableFactory.valid_types[table_type](table_number, capacity)
