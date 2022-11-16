import threading
from concurrent.futures import ThreadPoolExecutor
from work_test import work_test
from work_test import test_drag_resize
from work_test import test_full_screen_info
from work_test import test_full_screen_png


def run():
    executor = ThreadPoolExecutor(3)
    callbacks = [test_drag_resize, test_full_screen_info, test_full_screen_png]
    fs = []
    for c in callbacks:
        fs.append(executor.submit(work_test, c))
    executor.shutdown()


def work_test_mul_process():
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
