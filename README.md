# Feature
The module provides the following functions:
  - locate_to_screen(template_file, result_file)
  - capture_mouse_move(injectName="myFunc", injectVar="myVar")
  - move_mouse_to_pos_and_sniff(x, y)

#### locate_to_screen(template_file, result_file)
    - This function uses OpenCV matchTemplates to find sub-image, template_file
    , from screenshot of the current screen.
    - If sub-image was found, the center of the sub-image returns, in the form 
    of tuple (x, y). If result_file was given, it records the snapshot image 
    with sub-image highlighted, for debugging.
    - If sub-image was not found, it returns None.

#### capture_mouse_move()
    - This function injects Javascript function to listen to onmousemove events 
    of the document object. The coordinates that results, store in an variable 
    and attached to document object. It allows to specify the function name and 
    result variable name.
    - PS. After calling this function, it required to move the mouse to an 
    arbitary element (e.g. by driver.find_element_by_tag_name("input")), in 
    order to initial mouse position.
    
#### move_mouse_to_pos_and_sniff(x, y)
    - This function move the mouse to (x, y) and returns the Selemium WebElement 
    
# Background
> In some occasions, crawlers meet an treacheous website uses garbage string as its CSS class name. Crawlers foresees his efforts to locate the web elements would be cancelled out by frequent obfuscating of the class name, again and again.
Crawler remembered, he holds a mouse like a dagger. He can stab into the rubbish bin and see the treasure inside.


