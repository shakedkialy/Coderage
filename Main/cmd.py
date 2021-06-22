import sys
from os import path
from Main.DB.DatabaseHandler import *
from Main.HTML.HTML import *
from Main.Parser.Parser import *


def parse_args(argv):
    """
    this function parses the command line arguments
    :param argv: array of command line arguments
    :return: arguments neccassry to run the program
    """
    code_path, test_path, output_path, extra_args, delete_out = "", "Tests", "Results", "", True
    for arg in argv[1:]:
        if "module" in arg:
            modules = arg.split("=")[1]
            code_path = modules.split(",")
        elif "tests" in arg:
            test_path = arg.split("=")[1]
        elif "out_dir" in arg:
            output_path = arg.split("=")[1]
        elif "delete_out" in arg:
            delete_out = arg.split("=")[1]
            if delete_out == "False":
                delete_out = False
        else:
            extra_args += " " + arg
    if code_path == "":
        raise Exception("Missing modules to cover")
    return code_path, test_path, output_path, delete_out, extra_args


def main():
    code_path, test_path, output_path, delete_out, extra_args = parse_args(sys.argv)

    if not os.path.exists(output_path):
        if not delete_out:
            os.system("mkdir %(output_path)s" % {"output_path": output_path})
        else:
            os.system("mkdir %(output_path)s %(annotate_path)s" % {"output_path": output_path,
                                                                 "annotate_path": path.join(output_path, "annotate")})
    elif os.path.exists(path.join(output_path, "html")):
        shutil.rmtree(path.join(output_path, "html"))

    db = DatabaseHandler(output_path, code_path, test_path)

    cov_modules = ""
    for module in code_path:
        cov_modules += ("--cov=%(code_path)s " % {"code_path": module})

    if not delete_out and os.path.exists(output_path):
        output_path += str(db.get_last_run_id() + 1)

    exit_code = os.system(
        "python -m pytest --cov-report annotate:%(cov_annotate)s --cov-report html:%(cov_html)s --cov-report xml:%(Covxml)s %(cov_modules)s"
        " %(test_path)s --junitxml=%(Testsxml)s --html=%(pytest_report)s %(extra_args)s" % {
            "cov_modules": cov_modules,
            "test_path": test_path,
            "Covxml": path.join(output_path, "coverage.xml"),
            "Testsxml": path.join(output_path, "tests.xml"),
            "cov_annotate": path.join(output_path, "annotate"),
            "cov_html": path.join(output_path, "html"),
            "pytest_report": path.join(output_path, "html", "pytest_report.html"),
            "extra_args": extra_args})

    if exit_code != 0 and exit_code != 1:
        exit()

    parser = Parser(db, output_path)
    html = HTML(path.join(output_path, "html"), db)

    if delete_out:
        os.system("rm -r -f %(Covxml)s %(Testsxml)s %(cov_annotate)s .pytest_cache" % {
            "Covxml": path.join(output_path, "coverage.xml"),
            "Testsxml": path.join(output_path, "tests.xml"),
            "cov_annotate": path.join(output_path, "annotate")
        })
    abs_path = output_path + "/html/main_index.html"
    print("To watch the results copy this path to your internet browser: \n" +
          os.path.abspath(abs_path))
    # python main.py module=. tests=Tests_Examples


if __name__ == '__main__':
    main()
