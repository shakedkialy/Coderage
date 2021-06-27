from sys import stderr

from Main.HTML.HTML import *
from Main.Parser.Parser import *
import argparse
from Main.Parser.TemplateCreator import *
from Main.DB.DatabaseMerger import *


def _str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def parse_args():
    """
    this function parses the command line arguments
    :return: arguments necessary to run the program
    """
    arg_parser = argparse.ArgumentParser(prog="Coderage", description="Usage: Coderage -m <Modules to test> -t <Test directory>")
    subparsers = arg_parser.add_subparsers(help='help for subcommand', dest='command')

    test_group = subparsers.add_parser('test', help='arguments to test your program')
    merge_group = subparsers.add_parser('merge', help='arguments to merge two databases')

    test_group.add_argument('-m', '--module', help='Path to your tested modules', nargs='+', metavar='', required=True)
    test_group.add_argument('-t', '--tests', help='Path to your tests directory', nargs='+', metavar='', required=True)
    test_group.add_argument('-o', '--out_dir', help='Path to your output directory', default='results', metavar='')
    test_group.add_argument('-d', '--delete_out', help='True/False (yes, t, y, 1, no, f, n, 0 are also applicable), '
                                                       'Deletes unnecessary pytest files from out dir', default=True,
                            metavar='')
    test_group.add_argument('-ct', '--create_template',
                            help='True/False (yes, t, y, 1, no, f, n, 0 are also applicable), '
                                 'Creates template files to help build tests for all untested functions', default=False,
                            metavar='')
    test_group.add_argument('-e', '--extra_args', help='Extra args to pass pytest', nargs=argparse.REMAINDER,
                            default='', metavar='')

    merge_group.add_argument('-f', '--first', help='Path to the first database', metavar='', required=True)
    merge_group.add_argument('-s', '--second', help='Path to the second database', metavar='', required=True)
    merge_group.add_argument('-o', '--out_dir', help='Path to your output directory', default='results', metavar='', required=True)

    return arg_parser.parse_args()


def test_mode(args):
    """
    This function manages the test mode of the program - runs the tests and creates the HTML reports, with the
    given arguments from the user.
    """
    if not os.path.exists(args.out_dir):
        if not args.delete_out:
            os.system("mkdir %(out_dir)s" % {"out_dir": args.out_dir})
        else:
            os.system("mkdir %(out_dir)s %(annotate_path)s" % {"out_dir": args.out_dir,
                                                               "annotate_path": path.join(args.out_dir, "annotate")})
    elif os.path.exists(path.join(args.out_dir, "html")):
        shutil.rmtree(path.join(args.out_dir, "html"))

    db = DatabaseHandler(args.out_dir, args.module, args.tests)

    # Convert list of modules directories to cov_modules string
    cov_modules = ""
    for module in args.module:
        cov_modules += ("--cov=%(code_path)s " % {"code_path": module})

    # Adding -- before each extra argument
    extra_args = ""
    for extra_arg in args.extra_args:
        extra_args += ("%(extra_arg)s " % {"extra_arg": extra_arg})

    # Convert list of tests directories to tests string
    tests = ""
    for test_dir in args.tests:
        tests += ("%(test_dir)s " % {"test_dir": test_dir})

    if not args.delete_out and os.path.exists(args.out_dir):
        args.out_dir += str(db.get_last_run_id() + 1)
    pytest_cmd = "python -m pytest --cov-report annotate:%(cov_annotate)s --cov-report html:%(cov_html)s " \
                 "--cov-report xml:%(Covxml)s %(cov_modules)s %(test_path)s --junitxml=%(Testsxml)s " \
                 "--html=%(pytest_report)s %(extra_args)s" % \
                 {
                     "cov_modules": cov_modules,
                     "test_path": tests,
                     "Covxml": path.join(args.out_dir, "coverage.xml"),
                     "Testsxml": path.join(args.out_dir, "tests.xml"),
                     "cov_annotate": path.join(args.out_dir, "annotate"),
                     "cov_html": path.join(args.out_dir, "html"),
                     "pytest_report": path.join(args.out_dir, "html", "pytest_report.html"),
                     "extra_args": extra_args
                 }

    exit_code = os.system(pytest_cmd)
    if exit_code != 0 and exit_code != 1:
        print("Error: pytest ended with exit code: " + str(exit_code))
        exit()

    parser = Parser(db, args.out_dir)
    html = HTML(path.join(args.out_dir, "html"), db)

    if args.create_template:
        create_templates(db, args.out_dir)

    if _str2bool(args.delete_out):
        os.remove(path.join(args.out_dir, "coverage.xml"))
        os.remove(path.join(args.out_dir, "tests.xml"))
        shutil.rmtree(path.join(args.out_dir, "annotate"))

    abs_path = args.out_dir + "/html/main_index.html"
    print("To watch the results copy this path to your internet browser: \n" +
          os.path.abspath(abs_path))


def update_db_name(db_path, results_path, idx):
    """
    This function checks if the file in the db_path exists, and changes the db name in case it in the
    results_path, to make sure the databases names won't collide.
    """
    if not os.path.exists(db_path) or not db_path.endswith("coderage.db"):
        stderr.write("The given paths are not valid coderage database paths")
        exit()

    db_dir = os.path.dirname(db_path)
    updated_db_path = db_path
    if db_dir == results_path:
        updated_db_path = os.path.join(db_dir, "coderage" + str(idx) + ".db")
        os.rename(db_path, updated_db_path)
    return updated_db_path


def merge_mode(args):
    """
    This function manages the merge mode of the program - merges the data in two databases into one, with the
    given arguments from the user.
    """
    DatabaseMerger.merge_databases(update_db_name(args.first, args.out_dir, 1),
                                   update_db_name(args.second, args.out_dir, 2),
                                   args.out_dir)

    print("A new database was created: " + os.path.join(args.out_dir, "coderage.db"))


def main():
    args = parse_args()

    if args.command == 'test':
        test_mode(args)
    else:
        merge_mode(args)


if __name__ == '__main__':
    main()
