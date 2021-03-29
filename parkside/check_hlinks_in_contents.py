from metis import Driver
import os

driver = Driver()
driver.get("https://en.wikipedia.org/wiki/Metis_(mythology)")
status = driver.check_hlinks_in_contents("toc")
driver.print_test_status(status, os.path.basename(__file__))
driver.close()
