# from master import main 
# main()

def test():
    from mongo_items import test_task
    test_task()
    from master import test_executor
    test_executor()
    from master import test_executor_manager
    test_executor_manager()

test()
