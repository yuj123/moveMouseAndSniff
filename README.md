# Feature
The module provides the following functions:
  - locate_to_screen(snapshot_file, template_file, result_file)
  - capture_mouse_move(driver, injectName="myFunc", injectVar="myVar")
  - move_mouse_to_pos_and_sniff(driver, x, y, injectVar="myVar")

#### locate_to_screen(snapshot_file, template_file, result_file)
 - This function uses OpenCV matchTemplates to find sub-image, template_file, from screenshot of the current screen.
 - If sub-image was found, the center of the sub-image returns, in the form of tuple (x, y). The result_file records the snapshot image with sub-image highlighted, for debugging.
 - If sub-image was not found, it returns None.

#### capture_mouse_move(driver, injectFunc="myFunc", injectVar="myVar")
 - This function injects Javascript function to listen to onmousemove events of the document object by Selenium WebDriver. The coordinates that results, store in an variable and attached to document object. It allows to specify the function name and result variable name.
 - PS. After calling this function, it required to move the mouse to an arbitary element (e.g. by driver.find_element_by_tag_name("input")), in order to initial mouse position.
    
#### move_mouse_to_pos_and_sniff(driver, x, y, injectVar="myVar")
 - This function move the mouse to (x, y) and returns the Selemium WebElement 

#### Result    
```
> python test_move_sniff.py
DEBUG:SimpleTestCase:-------------- test_locate_to_screen - begin --------------
DEBUG:SimpleTestCase:The center point of the sub-image is located at (217, 421)
DEBUG:SimpleTestCase:-------------- test_locate_to_screen - end --------------
.DEBUG:SimpleTestCase:-------------- test_move_mouse_to_pos_and_sniff - begin --------------
DEBUG:SimpleTestCase:mouse position before fist move=None
DEBUG:SimpleTestCase:mouse position of first move=[675, 34]
DEBUG:SimpleTestCase:mouse position of second move=[217, 421]
DEBUG:SimpleTestCase:Resulted element=<selenium.webdriver.firefox.webelement.FirefoxWebElement (session="9a0c9aa2-2372-4957-9e6d-4bf27afdfcb1", element="bbc55052-356b-4117-a842-40fb9c88e6fe")>
DEBUG:SimpleTestCase:element text=Selenium move mouse to point and sniff
DEBUG:SimpleTestCase:element css=col-11 text-gray-dark mr-2
DEBUG:SimpleTestCase:-------------- test_move_mouse_to_pos_and_sniff - end --------------
.DEBUG:SimpleTestCase:-------------- test_move_mouse_to_pos_multiply - start --------------
DEBUG:SimpleTestCase:mouse position before fist move=None
DEBUG:SimpleTestCase:mouse position before first move=[50, 50]
DEBUG:SimpleTestCase:Resulted element css=header header-logged-out position-relative f4 py-3
DEBUG:SimpleTestCase:mouse position before second move=[50, 100]
DEBUG:SimpleTestCase:Resulted element css=pagehead repohead instapaper_ignore readability-menu experiment-repo-nav
DEBUG:SimpleTestCase:-------------- test_move_mouse_to_pos_multiply - end --------------
.
----------------------------------------------------------------------
Ran 3 tests in 10.100s

OK
```


# Background
> In some occasions, crawlers meet an treacheous website uses garbage string as its CSS class name. Crawlers foresees his efforts to locate the web elements would be cancelled out by frequent obfuscating of the class name, again and again.
Crawler remembered, he holds a mouse like a dagger. He can stab into the rubbish bin and see the treasure inside.

 

