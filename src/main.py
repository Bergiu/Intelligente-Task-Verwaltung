# from master import main 
# main()
import sys

def run_slave():
    from slave import run
    run()

def run():
    print("not implemented")

def test():
    from mongo_items import test_task
    test_task()
    from master import test_executor
    test_executor()
    from master import test_executor_manager
    test_executor_manager()
    from master import test_create_time_setting
    test_create_time_setting()

def main(argv):
    if "--test" in argv:
        test()
    elif "--run-slave" in argv:
        run_slave()
    else:
        run()

if __name__ == "__main__":
    main(sys.argv)
