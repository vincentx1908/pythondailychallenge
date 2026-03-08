import re
def get_element_size(window_size, element_vw, element_vh):
    matches = re.findall(r'\d+', window_size)
    sizes = [int(n) for n in matches]
    w_scale = int(element_vw[:-2])
    h_scale = int(element_vh[:-2])
    width = round(sizes[0] * w_scale / 100)
    height = round(sizes[1] * h_scale / 100)
    return f"{width} x {height}"


# ChatGPT has provided a 3-line solution, even without using regex.

def get_element_size(window_size, element_vw, element_vh):
    w, h = map(int, window_size.split(" x "))
    return f"{round(w * int(element_vw[:-2]) / 100)} x {round(h * int(element_vh[:-2]) / 100)}"
