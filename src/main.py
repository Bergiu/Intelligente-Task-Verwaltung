# from master import main 
# main()
import sys

def run_slave():
    from slave import run
    run()

def run():
    print("not implemented")

def test(slave_ip):
    from mongo_items import test_task
    test_task()
    from master import test_executor
    test_executor(slave_ip=slave_ip)
    from master import test_executor_manager
    test_executor_manager(slave_ip=slave_ip)
    from master import test_create_time_setting
    test_create_time_setting(slave_ip=slave_ip)

def main(argv):
    slave_ip=None
    if "--slave-ip" in argv:
        slave_ip = argv[argv.index("--slave-ip") + 1]
    if "--test" in argv:
        test(slave_ip)
    elif "--run-slave" in argv:
        run_slave()
    else:
        run()

if __name__ == "__main__":
    main(sys.argv)
