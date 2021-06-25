from os import path, makedirs


FUNCTION_TEMPLATE = """def test_{}():
    pass\n\n"""
FILE_TEMPLATE = "{}_test.py"
IMPORT_STRING = "from {} import *\n\n\n"


def create_templates(db, results_path):
    """
    This function creates template test files for untested functions.
    :param db: the database to get the functions names from
    :param results_path: the directory to save the files at
    """
    untested_funcs = db.get_last_untested()
    output_folder = path.join(results_path, "tests_templates")

    if len(untested_funcs) > 0:
        if not path.exists(output_folder):
            makedirs(output_folder)

    files_created = {}
    for name, function_name in untested_funcs:
        function_name = function_name.strip()
        file_name = name.removesuffix('.py')
        if file_name in files_created:
            files_created[file_name].append(function_name)
        else:
            files_created[file_name] = [function_name]

    for file in files_created:
        test_file_name = FILE_TEMPLATE.format(file)

        with open(path.join(output_folder, test_file_name), "w+") as test_file:
            test_file.write(IMPORT_STRING.format(file))
            for function in files_created[file]:
                test_file.write(FUNCTION_TEMPLATE.format(function))
